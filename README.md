# ZüriWieNeu

## Description
The objective of this SDS project is to analyze the **Züri wie neu** dataset 
provided by Open Data Zürich, which contains all recorded reports of damage 
to the city's urban infrastructure. The study specifically focuses on 
identifying and evaluating spatial and temporal patterns within these reports, 
and investigates whether the spatial distribution of waste containers is 
related to the frequency of waste-related reports across districts.

---

## Project Structure

```bash
├── data/
│   ├── raw/                   # Original downloaded datasets
│   └── processed/             # Cleaned and preprocessed data
├── notebooks/
│   ├── data_cleaning.ipynb    # Data preprocessing
│   └── spatial_analysis.ipynb # Main analysis
├── outputs/                   # Generated maps and figures
├── environment.yml
└── README.md
```

---

## Data Sources
- Reports: https://data.stadt-zuerich.ch/dataset/geo_zueri_wie_neu
- Districts: https://data.stadt-zuerich.ch/dataset/geo_statistische_quartiere
- Lakes: https://data.stadt-zuerich.ch/dataset/ktzh_av_gewaesser__ogd_
- Waste Containers: https://data.stadt-zuerich.ch/dataset/geo_abfallgefaesse

---

## Setup Instructions

**Requirements:**
- Miniconda or Anaconda
- VS Code (recommended)

### Environment Setup

```bash
# Create the environment
conda env create -f environment.yml
````

```bash
# Activate the environment
conda activate sds210_project_env
```

---

## Execution Order

Run the notebooks in the following order:

1. `data_cleaning.ipynb`: loads raw data, handles missing values, 
    reprojects CRS, and exports processed files to `data/processed/`
2. `spatial_analysis.ipynb`: performs all spatial, temporal, 
    and statistical analyses and saves outputs to `outputs/`