# 🌿 UAS Ecophysiology: 

> **Imaging spectroscopy can map canopy water potential in a diverse forest ecosystem**

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![DOI](https://img.shields.io/badge/DOI-10.xxxx%2Fxxxxx-blue.svg)](https://doi.org/)
[![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![R](https://img.shields.io/badge/R-4.x-276DC3?logo=r&logoColor=white)](https://www.r-project.org/)

---

## 📖 About

This repository contains example code, data, and workflows for analysis presented in:

> **[Author(s)], [Year].** *UAS Ecophysiology: Imaging spectroscopy can map canopy water potential in a diverse forest ecosystem.* [Journal Name]. [DOI]

We demonstrate that Unoccupied Aerial System (UAS)-based imaging spectroscopy can reliably retrieve **leaf and canopy water potential (Ψ)** across a structurally and taxonomically diverse temperate forest — linking remotely sensed spectral signatures to plant hydraulic status at ecologically meaningful scales.

---

## 📁 Data Availability

| Dataset | Format | Size | DOI / Link |
|---------|--------|------|-----------|
| UAS hyperspectral imagery | ENVI/HDF5 | ~XX GB | [Repository link] |
| Field water potential measurements | CSV | <1 MB | Included in `/data/raw/field/` |
| Processed spectral features | CSV / NetCDF | ~XX MB | Included in `/data/processed/` |


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

If you use this code or data, please cite:

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


## 👥 Authors & Acknowledgements

- **[Lead Author]** — [Institution]
- **[Co-author(s)]** — [Institution(s)]

Fieldwork was conducted at [Site Name]. We thank [field assistants, collaborators]. Funding was provided by [funding bodies / grant numbers].

---

<p align="center">
  <em>Questions? Open an issue or contact [corresponding author email]</em>
</p>