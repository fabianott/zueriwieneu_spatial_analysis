# ZüriWieNeu

## Description
The objective of this SDS project is to analyze the **Züri wie neu** dataset 
provided by Open Data Zürich, which contains all recorded reports of damage 
to the city's urban infrastructure. The study specifically focuses on 
identifying and evaluating spatial and temporal patterns within these reports, 
and investigates whether the spatial distribution of waste containers is 
related to the frequency of waste-related reports across districts and investigates whether the spatial distribution of waste containers and urban activity intensity (proxied by gastronomy establishments) are related to the frequency of waste-related reports across districts.

---

## Project Structure

```bash
zueriwieneu_spatial_analysis
├── data/
│   ├── raw/                        # Original downloaded datasets
│   └── processed/                  # Cleaned and preprocessed data
├── notebooks/
│   ├── src                         # Costum python modules (.py scripts)
│       ├── bar_charts.py           
│       ├── choropleth_maps.py
│       └── point_distribution.py 
│   ├── data_cleaning.ipynb         # Data preprocessing
│   └── spatial_analysis.ipynb      # Main analysis
├── outputs/                        # Generated maps and figures
├── environment.yml                 # Required phython packages
└── README.md
```

---

## Data Sources
- **Reports:** Citizen-reported infrastructure issues (e.g. potholes, graffiti, waste). https://data.stadt-zuerich.ch/dataset/geo_zueri_wie_neu
- **Districts:** Statistical district boundaries of the city of Zurich. https://data.stadt-zuerich.ch/dataset/geo_statistische_quartiere
- **Lakes:** Water body polygons of Zurich. https://data.stadt-zuerich.ch/dataset/ktzh_av_gewaesser__ogd_
- **Waste Containers:** Point locations of all registered public waste containers in the city of Zurich. https://data.stadt-zuerich.ch/dataset/geo_abfallgefaesse
- **Gastronomy:** Point locations of all registered gastronomy establishments (restaurants, bars, cafes) in the city of Zurich. https://data.stadt-zuerich.ch/dataset/geo_gastwirtschaftsbetriebe 

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
conda activate zueriwieneu_env
```

---

## Execution Order

Run the notebooks in the following order:

1. `data_cleaning.ipynb`: loads raw data, handles missing values, 
    reprojects CRS, and exports processed files to `data/processed/`
2. `spatial_analysis.ipynb`: performs all spatial, temporal, 
    and statistical analyses and saves outputs to `outputs/`

Helper functions used in `spatial_analysis.ipynb` are located in `notebooks/src/` 
and are imported automatically when the notebook is executed.