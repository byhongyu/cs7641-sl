from pathlib import Path
from sklearn.utils import Bunch
import numpy as np

def create_dataset(file_list, description=""):
    dataset = Bunch()
    data_all = [np.load(fname) for fname in file_list]
    x_all = [np.squeeze(data['x']) for data in data_all]
    y_all = [data['y'] for data in data_all]

    dataset.data = np.concatenate(x_all)
    dataset.target = np.concatenate(y_all)
    dataset.DESCR = description
    dataset.feature_names = [f'time_{t}' for t in range(len(dataset.data.shape[1]))]
    dataset.target_names = ["sleep_stage"]
    return dataset


