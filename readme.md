# UAS Ecophysiology: Imaging spectroscopy can map canopy water potential in a diverse forest ecosystem

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![DOI](https://img.shields.io/badge/DOI-10.1016%2Fj.rse.2026.115532-blue.svg)](https://doi.org/10.1016/j.rse.2026.115532)
[![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)

---

## About

This repository contains example code and data for analysis presented in:

> Haynes RS, Lucieer A, Turner D, Cimoli E, Sivanandam P, Brodribb T. 2026. *UAS Ecophysiology: Imaging spectroscopy can map canopy water potential in a diverse forest ecosystem.* Remote Sensing of Environment. https://doi.org/10.1016/j.rse.2026.115532

The workflow links lab spectra and water potential measurements with UAS hyperspectral imagery to explore canopy water potential across a diverse forest ecosystem.

---

## Code Structure

Two analysis and visualisation scripts are available within this repo:

```text
Scripts/
|-- RF_1000_iters.py          # Runs repeated stratified random forest models on lab spectra
|-- data_exploration.ipynb    # Simple notebook for spectra, imagery, mask, and RF prediction exploration
```

Supporting example data are included under:

```text
Data/
|-- Lab_spectra/        # Spectra CSVs with water potential as the first column
|-- Example_imagery/    # Small ENVI imagery subsets and vegetation/shadow mask
|-- Model_pkls/         # Example trained random forest model files
```

---

## Citation

If you use this code or data, please cite the published manuscript:

```bibtex
@article{Haynes2026UASEcophysiology,
  author  = {Haynes, R. S. and Lucieer, A. and Turner, D. and Cimoli, E. and Sivanandam, P. and Brodribb, T.},
  title   = {UAS Ecophysiology: Imaging spectroscopy can map canopy water potential in a diverse forest ecosystem},
  journal = {Remote Sensing of Environment},
  year    = {2026},
  pages   = {115532},
  doi     = {10.1016/j.rse.2026.115532}
}
```
