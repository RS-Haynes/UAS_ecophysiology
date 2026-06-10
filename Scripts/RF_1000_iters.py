"""
@author:         Ryan Haynes
@organization:   TerraLuma (University of Tasmania)
@detail:         This is an example script that runs 1000 iterations of Random Forest regression on lab-based
                 spectroscopy data to assess model stability. Each iteration uses
                 a random train/test split. Summary statistics and feature
                 importances are reported across all iterations.
@Notes:          This script is computed only for the laboratory dataset. To incorporate field observations, 
                 additional code will need to be added to bring the data in and apply the model. Example code
                 to implement this is given at the end of the script.

"""

# %% IMPORTS
import os
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

# %% LOAD DATA
data_path = os.path.join("Data", "Lab_spectra", "C_rhomboidea_spectra_DF.csv")
df = pd.read_csv(data_path)

# Assumes first column is WP (target) and remaining columns are spectral features
X = df.iloc[:, 1:]
y = df.iloc[:, 0]

num_sites, num_vars = X.shape
percent_training    = 0.75
n_iterations        = 1000
n_bins              = 3

# Define stratification bins once so each iteration samples across the WP range
_, bin_edges = pd.qcut(y, q=n_bins, retbins=True, duplicates="drop")
y_binned = pd.cut(y, bins=bin_edges, include_lowest=True)

# %% RUN ITERATIONS
results = []
all_importances = np.zeros((n_iterations, num_vars))

print(f"Running {n_iterations} RF iterations...")

for iteration in range(n_iterations):
    # Stratified train/test split across water potential bins
    x_train, x_test, y_train, y_test = train_test_split(
        X,
        y,
        train_size=percent_training,
        random_state=iteration,
        stratify=y_binned
    )

    # Train model
    rf = RandomForestRegressor(
        n_estimators=512,
        max_depth=None,
        max_features=1.0,
        random_state=iteration,
        n_jobs=-1,
        oob_score=True
    )
    rf.fit(x_train, y_train)

    # Evaluate
    y_pred_train = rf.predict(x_train)
    y_pred_test  = rf.predict(x_test)

    rmse_train = np.sqrt(mean_squared_error(y_train, y_pred_train))
    rmse_test  = np.sqrt(mean_squared_error(y_test,  y_pred_test))
    r2_train   = r2_score(y_train, y_pred_train)
    r2_test    = r2_score(y_test,  y_pred_test)

    results.append({
        "iteration"  : iteration + 1,
        "rmse_train" : rmse_train,
        "rmse_test"  : rmse_test,
        "r2_train"   : r2_train,
        "r2_test"    : r2_test,
        "oob_r2"     : rf.oob_score_
    })

    all_importances[iteration, :] = rf.feature_importances_

    if (iteration + 1) % 100 == 0:
        print(f"  Completed {iteration + 1} / {n_iterations} iterations")

results_df = pd.DataFrame(results)

# %% SUMMARY STATISTICS
print("\n" + "=" * 50)
print(f"Summary over {n_iterations} iterations")
print("=" * 50)
metrics = ["rmse_train", "rmse_test", "r2_train", "r2_test", "oob_r2"]
for metric in metrics:
    vals = results_df[metric]
    print(f"  {metric:12s}  mean={vals.mean():.4f}  std={vals.std():.4f}  "
          f"min={vals.min():.4f}  max={vals.max():.4f}")

# %% RETRAIN FINAL MODEL ON ALL DATA
print("\nRetraining final model on full dataset...")

rf_final = RandomForestRegressor(
    n_estimators=512,
    max_depth=None,
    max_features=1.0,
    random_state=42,
    n_jobs=-1,
    oob_score=True
)
rf_final.fit(X, y)

y_pred_full = rf_final.predict(X)
rmse_full   = np.sqrt(mean_squared_error(y, y_pred_full))
r2_full     = r2_score(y, y_pred_full)

print("\n" + "=" * 50)
print("Final Model (trained on all data)")
print("=" * 50)
print(f"  RMSE         : {rmse_full:.4f}")
print(f"  R²           : {r2_full:.4f}")
print(f"  OOB R²       : {rf_final.oob_score_:.4f}")


# %% SAVE FINAL MODEL
#model_dir  = os.path.join("Data", "Model_pkls")
#model_path = os.path.join(model_dir, "_rf_model.pkl")

#with open(model_path, "wb") as f:
#    pickle.dump(rf_final, f)

#print(f"\nFinal model saved to: {model_path}")


