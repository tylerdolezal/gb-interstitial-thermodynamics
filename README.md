# Grain Boundary Thermodynamics & Solute Segregation Analysis

This repository contains the processed datasets and Python plotting scripts required to reproduce the figures for the manuscript. To ensure computational efficiency and reproducibility, high-volume Molecular Dynamics (MD) and Monte-Carlo (MC) trajectory data have been consolidated into structured `.csv` files.

> **Complementary Thermodynamic Mechanisms of Boron and Carbon Segregation at Grain Boundaries in Nickel Alloys**  
> Tyler D. Doležal, Rodrigo Freitas, Ju Li

The intent of this repository is to ensure **transparency and reproducibility of the reported results**.

## 📂 Repository Organization

* **`data/`**: Consolidated datasets containing thermodynamic, spectral, and convergence histories.
* **`plots/`**: Output directory for publication-quality PDF figures.
* **`scripts`**: Python post-processing and plotting scripts.

---

## 📊 Dataset Descriptions (`data/`)

These files act as the data source for all manuscript and supplemental figures.

| File Name | Description | Related Figure |
| :--- | :--- | :--- |
| `figure_1e_thermodynamics.csv` | GB width, interfacial excess ($\Gamma$), and grand potential excess ($\Omega$) with propagated error bars. | Figure 1e |
| `figure_2_kde_curves.csv` | Normalized probability density functions (PDFs) for segregation energy ($E_{seg}$) distributions. | Figure 2 |
| `figure_3_sro_curves.csv` | Local Short-Range Order (SRO) distribution curves ($\alpha$) for B and C systems. | Figure 3 |
| `figure_2_spectral_summary.csv`| Summary metrics: weighted average $E_{seg}$ and strong-site fractions ($E_{seg} \leq -2$ eV). | Figure S6 |
| `figure_3_sro_summary.csv` | Summary metrics for SRO: weighted mean $\alpha$ and highly-ordered fractions. | Figure S7 |
| `figure_s2_history.csv` | Cohesive energy (eV/atom) and bulk solute concentration (at.%) history from calibration runs. | Figure S2 |
| `figure_s3_delta_mu_fit.csv` | Actual vs. predicted solute chemical potentials ($\Delta\mu$) from the bilinear calibration model. | Figure S3 |
| `mc_convergence_data.csv` | Structural and energy convergence history for grain boundary regions during SGC-MC production. | Figure S4, S5 |

---

## 🐍 Plotting Scripts

Run these scripts to generate the figures from the provided `.csv` data.

### Main Text Figures
* **`figure_1e.py`**: Plots the primary thermodynamic isotherms (GB Width, $\Gamma$, and $\Omega$).
* **`figure_2_ridge.py`**: Generates the segregation energy ($E_{seg}$) spectral ridge plots.
* **`figure_3_ridge.py`**: Generates the Short-Range Order (SRO) spectral ridge plots.

### Supplemental Figures
* **`figure_s2.py`**: Visualizes SGC-MC convergence of energy and bulk composition for the Cr-solute calibration.
* **`figure_s3.py`**: Validates the bilinear chemical potential fit using residual analysis.
* **`figure_s4_s5.py`**: Visualizes the equilibration of the grain boundary region (Total Energy and $X_{GB}$).
* **`figure_s6.py` / `figure_s7.py`**: Plot Supplemental trend lines for spectral energy and SRO summary metrics across all concentrations/temperatures.
---
