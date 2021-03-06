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
```
.
├── data
├── docs
├── environment.yaml
├── playground
├── pysleep
├── README.md
├── setup.py
├── hyu81-analysis.pdf
```

`data` folder: raw data and processed data.
`pysleep`: python package developed for this project
`setup.py`: installation script for pysleep package.
`environment.yaml`: configuration file for setting up virtual environment.
`cs7641-sl.ipynb`: scripts for eda, run models, plot etc. Code for both classification problems are contained in this notebook.
README.md: quick introduction.


# Classification Problem 1: HR Analytics
## Introduction
This dataset contains information about candidates from the signup forms when the register for certain events provided by a company. It can be used to build models that predict where a candidate is actively looking for jobs.

## Data
Data is already downloaded and included in this repo. Path to data: repo_root/data/HR/aug_train.csv
Data source: https://www.kaggle.com/arashnic/hr-analytics-job-change-of-data-scientists

Here are the features contained in the dataset:

- enrollee_id : Unique ID for candidate
- city: City code
- city_ development _index : Developement index of the city (scaled)
- gender: Gender of candidate
- relevent_experience: Relevant experience of candidate
- enrolled_university: Type of University course enrolled if any
- education_level: Education level of candidate
- major_discipline :Education major discipline of candidate
- experience: Candidate total experience in years
- company_size: No of employees in current employer's company
- company_type : Type of current employer
- lastnewjob: Difference in years between previous job and current job
- training_hours: training hours completed

Here is the label:
target: 0 – Not looking for job change, 1 – Looking for a job change

Analysis script can be found in the notebook `cs7641-sl.ipynb`, under the section "Classification Problem 1: HR Analytics"

## Analysis
### Decision Tree

### KNN
GridSearch validation curves:
![hr_knn_vc](media/hr_knn_val_curve.png)
Learning curves:
![hr_knn_lc](media/hr_knn.png)
### Compare 5 models
![comparison_5_models](media/hr_5_models.png)

# Classification Problem 2: Sleep stage classification
## Introduction
Sleep is vital to human health. The quality of sleep can be used as an indicator or precursor of certain diseases, such as Alzheimer and Parkinson’s disease.
According to American Academy of Sleep Medicine (AASM) manual,
sleep can be divided into five stages: Wake (W), Non-Rapid Eye Movement stages N1 (for drowsiness or transitional sleep), N2 (for light sleep), and N3 (for deep sleep), and Rapid Eye Movement (REM),
which can be determined by analyzing polysomnograms (PSG) data of patients during sleep. PSG data is a collection of data collected from various sensors, including electroencephalography (EEG),
Electromyogram (EMG) and Electrocardiogram (ECG) recordings.

## Data
Raw data if the Sleep-EDF Database Expanded provided at PhysioNet (https://physionet.org/content/sleep-edfx/1.0.0/).
The sleep-edf database contains 197 whole-night PolySomnoGraphic sleep recordings, containing EEG, EMG and ECG recordings and event markers (manually labeled).
These signals are collected at 100Hz.
### Preprocessing
This is a comprehensive dataset and can be a bit overwhelming. Due to the scope limit of this project, I simplified the dataset (a lot):
- I limit the exploration to one EEG channel.
- Each raw data record includes a few hours worth of time series data. The time series data is mannually labeled by trainned physicians or technicians. I devided the dataset into 30-second segments, and treat each segment as a data record.
Connections between time segments are not considered.

The code for extracting eeg signals from the raw dataset is modified from [1].
The processed data is included in this repo and can be found here: `repo_root/data/Sleep/processed/eeg_fpz_cz/`

## Analysis 
### Code
Code for this problem can be found in the `cs7641-sl.ipynb` notebook, under the section "Classification Problem 2: Sleep stage classification"
### Decision Tree
![sleep DT learning curve](media/sleep_dt_lc.png)
### Preliminary results
![ROC_curves](media/sleep_models.png)

# References
[1] https://github.com/MousaviSajad/SleepEEGNet 