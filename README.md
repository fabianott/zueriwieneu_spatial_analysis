# ZüriWieNeu

## Description
The objective of this SDS project is to analyze the **Züri wie neu** dataset provided by Open Data Zürich, which contains all recorded reports of damage to the city's urban infrastructure. The study specifically focuses on identifying and evaluating spatial and temporal patterns within these reports.

---

## Data Sources
- Reports: https://data.stadt-zuerich.ch/dataset/geo_zueri_wie_neu
- Districts: https://data.stadt-zuerich.ch/dataset/geo_statistische_quartiere
- Lakes: https://data.stadt-zuerich.ch/dataset/ktzh_av_gewaesser__ogd_
- Waste Container: https://data.stadt-zuerich.ch/dataset/geo_abfallgefaesse

---

## Setup Instructions

To run the project, the following software is required:

- Python 3.12.11
- Miniconda or Anaconda
- VS Code

---

### Environment Setup

All required packages are defined in the `environment.yml` file.

Create the environment:

```bash
conda env create -f environment.yml
```
Activate the environment: 
```bash
conda activate sds210_project_env
````

---

## Execution Order
Run the `data_cleaning.ipynb` notebook first, followed by `spatial_analysis.ipynb`.