# Grain Boundary Interstitial Thermodynamics

This repository contains the **processed datasets and analysis scripts** required to reproduce the **figures and numerical results reported in the main text and Supplemental Information** of the manuscript:

> **Complementary Thermodynamic Mechanisms of Boron and Carbon Segregation at Grain Boundaries in Nickel Alloys**  
> Tyler D. Doležal, Rodrigo Freitas, Ju Li

The intent of this repository is to ensure **transparency and reproducibility of the reported results**.

---

## Repository overview

The repository is organized into processed data and lightweight analysis scripts that regenerate all plots and tabulated values appearing in the manuscript.

```

data/
main/
supplemental/

scripts/
main/
supplemental/

````

---

## `data/`

### `data/main/`
Processed datasets underlying all **main-text figures and tables**, including:

- Interfacial grand potential excess values
- Gibbsian interfacial excesses for interstitial and substitutional species
- Grain boundary width measurements
- Segregation energy spectra
- Short-range order (Warren–Cowley) statistics
- Associated metadata (temperature, composition, boundary type, interstitial species)

These datasets are sufficient to reproduce every main-text plot and reported numerical value.

---

### `data/supplemental/`
Additional processed datasets required to reproduce figures and tables presented in the **Supplemental Information**, including extended spectra, additional boundary conditions, and confirmatory analyses.

Raw atomistic trajectories and intermediate Monte Carlo configurations are **not included**.

---

## `scripts/`

### `scripts/main/`
Python scripts used to generate the **main-text figures** from the processed datasets.

Typical usage:
```bash
python scripts/main/make_fig1_state_variables.py
python scripts/main/make_fig2_segregation_spectra.py
python scripts/main/make_fig3_sro_spectra.py
python scripts/main/make_fig4_summary.py
````

Each script reads directly from `data/main/` and produces publication-quality figures consistent with those shown in the manuscript.

---

### `scripts/supplemental/`

Python scripts used to generate figures and numerical results reported in the **Supplemental Information**.

These scripts follow the same analysis framework as the main-text scripts and read from `data/supplemental/`.

---

## Software requirements

The analysis and plotting scripts require a standard scientific Python environment:

* Python ≥ 3.9
* NumPy
* Pandas
* Matplotlib
* SciPy

No proprietary software is required to run the scripts provided in this repository.

---

## Notes on atomistic sampling workflows

The atomistic simulations used to generate the processed datasets (hybrid semi-grand canonical / grand canonical Monte Carlo combined with molecular dynamics) were executed using a **licensed universal machine-learned interatomic potential (uMLIP)** on a commercial platform.

Because these components require access to licensed software, the corresponding simulation drivers and model files are **not distributed**. The processed datasets provided here are sufficient to reproduce all reported figures, tables, and numerical values without rerunning the atomistic simulations.

---

## Scope of reproducibility

This repository enables reproduction of:

* All **main-text figures**
* All **supplemental figures and tables**

---

## Citation

If you use the data or scripts provided in this repository, please cite the associated manuscript.
