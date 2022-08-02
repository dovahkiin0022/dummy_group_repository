# dummy_group_repositiory
Reinhart group project template

# Problem Statement
Based on preliminary data exploration, decided to use 'Ultimate Tensile Strength' as the property to predict.

# Setup
Setup a new conda environment for this project:
`conda env create --file environment.yml`

Or update an existing conda environment (e.g., between updates of this repository):
`conda env update --file environment.yml --prune`

## Note about creating yml files
You may want to leave the requirements very loosely defined so conda can locate correct dependencies on different platforms. This is achieved using the `--from-history` flag, like so:
`conda env export -n dummy_repository -f environment.yml --from-history`
