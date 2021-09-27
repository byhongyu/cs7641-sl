# Setup environment
Create virtual environment.
Using `conda`:
1. install 'conda' or 'miniconda'
2. navigate to the project root folder and create conda env.
`conda env create -f environment.yaml`
3. activate environment:
`conda activate cs7641`

Note that `PyCharm` IDE provides convenient integration with `venv`, 'conda' and 'pipenv'. It allows one to create and install packages using graphical user interface.

# Code structure
High level code organization:
.
├── data
├── docs
├── environment.yaml
├── playground
├── pysleep
├── README.md
├── setup.py
├── hyu81-analysis.pdf

`data` folder: raw data and processed data.
`pysleep`: python package developed for this project
`setup.py`: installation script for pysleep package.
`environment.yaml`: configuration file for setting up virtual environment.
`cs7641-sl.ipynb`: scripts for eda, run models, plot etc. Code for both classification problems are contained in this notebook.
README.md: quick introduction.


# Classification Problem 1: HR Analytics
Data is already downloaded and included in this repo. Path to data: repo_root/data/HR/aug_train.csv
Data source: https://www.kaggle.com/arashnic/hr-analytics-job-change-of-data-scientists
Analysis script can be found in the notebook `cs7641-sl.ipynb`
# Classification Problem 2: Sleep stage classification
