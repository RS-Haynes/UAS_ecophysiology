# 🌿 UAS Ecophysiology: Imaging spectroscopy can map canopy water potential in a diverse forest ecosystem

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![DOI](https://img.shields.io/badge/DOI-10.xxxx%2Fxxxxx-blue.svg)](https://doi.org/)
[![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)

---

## 📖 About

This repository contains example code and data for analysis presented in:

> **[Haynes RS, Lucieer A, Turner D, Cimoli E, Sivanandam P, Brodribb T], [2026].** *UAS Ecophysiology: Imaging spectroscopy can map canopy water potential in a diverse forest ecosystem.* [Journal Name]. [DOI]

We demonstrate that Unoccupied Aerial System (UAS)-based imaging spectroscopy can reliably infer **leaf and canopy water potential (Ψ)** across a structurally and taxonomically diverse forest landscape — linking remotely sensed spectral signatures to plant hydraulic status at an ecologically meaningful scale.

---

## 📁 Data Availability

| Dataset | Format | Size | DOI / Link |
|---------|--------|------|-----------|
| UAS hyperspectral imagery subset | ENVI | ~XX MB | Included in `/Data/Example_imagery/` |
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
