# 🌿 UAS Ecophysiology: Imaging spectroscopy can map canopy water potential in a diverse forest ecosystem

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![DOI](https://img.shields.io/badge/DOI-10.xxxx%2Fxxxxx-blue.svg)](https://doi.org/)
[![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)

---

## 📖 About

This repository contains example code and data for analysis presented in:

> **[Author(s)], [Year].** *UAS Ecophysiology: Imaging spectroscopy can map canopy water potential in a diverse forest ecosystem.* [Journal Name]. [DOI]

We demonstrate that Unoccupied Aerial System (UAS)-based imaging spectroscopy can reliably infer **leaf and canopy water potential (Ψ)** across a structurally and taxonomically diverse forest landscape — linking remotely sensed spectral signatures to plant hydraulic status at an ecologically meaningful scale.

---

## 📁 Data Availability

| Dataset | Format | Size | DOI / Link |
|---------|--------|------|-----------|
| UAS hyperspectral imagery subset | ENVI/HDF5 | ~XX GB | [Repository link] |
| Lab spectra with water potential measurements | CSV | <1 MB | Included in `/data/raw/field/` |

---

## 🧪 Methods Summary

```
UAS Flight Campaign
      │
      ▼
Radiometric Calibration (empirical line method)
      │
      ▼
Atmospheric Correction (ATCOR / QUAC)
      │
      ├──► Spectral Indices (WBI, NDWI, DATT)
      │
      ├──► Continuum Removal & Absorption Features
      │
      └──► PLSR / Random Forest ──► Canopy Ψ Maps
                    │
                    ▼
           Field Validation (pressure bomb)
```

---

## 📬 Citation

If you use this code or data, please cite the pubished manuscript:

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
