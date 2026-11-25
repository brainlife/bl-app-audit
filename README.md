<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset=".github/brand/brainlife-mark-on-dark.svg">
    <img src=".github/brand/brainlife-mark-on-light.svg" alt="brainlife.io" width="140">
  </picture>
</p>

<h1 align="center">bl-app-audit</h1>

<p align="center">
  A 2024 audit of brainlife.io Apps, their datatypes and compute resources.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Status-dormant-yellow.svg" alt="Status: dormant">
  <a href="https://brainlife.io"><img src="https://img.shields.io/badge/brainlife.io-site-3b9fd0.svg" alt="brainlife.io"></a>
  <a href="https://brainlife.io/docs"><img src="https://img.shields.io/badge/Docs-brainlife.io%2Fdocs-005981.svg" alt="Documentation"></a>
  <a href="https://doi.org/10.1038/s41592-024-02237-2"><img src="https://img.shields.io/badge/DOI-10.1038%2Fs41592--024--02237--2-e57536.svg" alt="Nature Methods paper"></a>
</p>

## 🧠 At a glance

| | |
|---|---|
| 🧭 **What** | `app_audit.py` (written for a notebook) plus CSV/JSON exports of Apps, datatypes, compute resources and sample data |
| 🕰️ **Last change** | 2024-01-25 |

## 🚀 Using it

Open `app_audit.py` in a Jupyter notebook (it uses notebook `!` commands), with the CSV files next to it. It reads `apps_df_with_resources.csv`, `datatypes_df.csv`, `resources_df.csv` and `sample_data2.csv` and builds input and `config.json` strings for each App.

## 🔗 Related

[abcd-spec](https://github.com/brainlife/abcd-spec) (current App manifest and catalog) · [pybrainlife](https://github.com/brainlife/pybrainlife)

## 📚 Citing

If you use brainlife.io in your work, please cite:

> Hayashi S, Caron BA, Heinsfeld AS, et al. brainlife.io: a decentralized and open-source cloud platform to support neuroscience research. *Nature Methods* 21:809–813 (2024). [doi:10.1038/s41592-024-02237-2](https://doi.org/10.1038/s41592-024-02237-2)

## 🤝 Contributing

Issues and pull requests are welcome in this repository. For help using brainlife.io, see the [documentation](https://brainlife.io/docs).

## ⚖️ License

This repository does not include a license file yet.

<p align="center"><sub>brainlife.io · Brain data across scales. One place to analyze, share and publish it. · The University of Texas at Austin</sub></p>
