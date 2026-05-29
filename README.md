# dummy_group_repositiory
Reinhart group project template

# Problem Statement

## Data files
* `data/hw5-iron-alloy.csv`: a tabulated data file for about 1300 different iron alloys and their properties

## Objective
We want to predict the `Ultimate Tensile Strength` of alloys as a function of their composition.

# Workflows
* Data preprocessing: `notebooks/0_data_preprocessing.ipynb`
* Exploratory data analysis: ...
* Model fitting: ...
* Hyperparameter tuning: ...

# Setup
Setup a new conda environment for this project:
`conda env create --file environment.yml`

Or update an existing conda environment (e.g., between updates of this repository):
`conda env update --file environment.yml --prune`

## Note about creating yml files
You may want to leave the requirements very loosely defined so conda can locate correct dependencies on different platforms. This is achieved using the `--from-history` flag, like so:
`conda env export -n dummy_repository -f environment.yml --from-history`
