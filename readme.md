# 🌿 UAS Ecophysiology: Imaging spectroscopy can map canopy water potential in a diverse forest ecosystem

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![DOI](https://img.shields.io/badge/DOI-10.xxxx%2Fxxxxx-blue.svg)](https://doi.org/10.1016/j.rse.2026.115532)
[![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)

---

## 📖 About

This repository contains example code and data for analysis presented in:

> **[Haynes RS, Lucieer A, Turner D, Cimoli E, Sivanandam P, Brodribb T], [2026].** *UAS Ecophysiology: Imaging spectroscopy can map canopy water potential in a diverse forest ecosystem.* [Remote Sensing of Environment]. [[DOI](https://doi.org/10.1016/j.rse.2026.115532)]

We demonstrate that Unoccupied Aerial System (UAS)-based imaging spectroscopy can reliably infer **leaf and canopy water potential (Ψ)** across a structurally and taxonomically diverse forest landscape, linking remotely sensed spectral signatures to plant hydraulic status at an ecologically meaningful scale.

---

🗂️ Code Structure
.
├── Scripts/
│   ├── Build_RFM_model.py      # Simple script to train a random forest model on lab spectra
│   ├── RFM_1000_iters.py       # Run 1000 iterations to test parameters and inputs
│   └── Apply_RFM_model.py      # Apply trained model to UAS imagery pixel values
└── README.md

---

## 📁 Data in this repo

| Dataset | Format | Size | DOI / Link |
|---------|--------|------|-----------|
| UAS hyperspectral imagery subset | ENVI | ~23 MB | Included in `/Data/Example_imagery/` |
| Lab spectra with water potential measurements | CSV | <1 MB | Included in `/Data/Lab_spectra/` |

---

## 🧪 Methods Summary

```
UAS Flight Campaign
      │
      ▼
Laboratory experiment
      │
      ▼
Model development
      │
      └──► Random forest lab model
                    │
                    ▼
           Scaled and validated to UAS hyperspectral imagery
```

---

## 📬 Citation

If you found this code or data useful, please cite the pubished manuscript:

```bibtex
@article{[citekey][year],
  author  = {[Authors]},
  title   = {UAS Ecophysiology: Imaging spectroscopy can map canopy water potential in a diverse forest ecosystem},
  journal = {[Journal]},
  year    = {[Year]},
  volume  = {[Vol]},
  pages   = {[Pages]},
  doi     = {[DOI]}
}
```

---
