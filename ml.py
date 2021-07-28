import os
from random import random, randint
from mlflow import log_metric, log_param, log_artifacts

import sys
sys.path.append(os.path.abspath(os.path.join('..')))
import dvc.api

import mlflow
import mlflow.sklearn
from urllib.parse import urlparse

path = 'data/AdSmartABdata.csv'
repo = 'https://github.com/NatnaelSisay/abtest-mlops.git'
data_url = dvc.api.get_url(path=path, repo=repo)


# reading data
# this is not the right waytody , but cml is showing me error
file_name = './data/store.csv'
ad_df = pd.read_csv(file_name)
df = ad_df.copy()
df['conversion'] = df.yes


if __name__ == "__main__":
    # Log a parameter (key-value pair)
    log_param("param1", randint(0, 100))

    # Log a metric; metrics can be updated throughout the run
    log_metric("foo", random())
    log_metric("foo", random() + 1)
    log_metric("foo", random() + 2)

    # Log an artifact (output file)
    if not os.path.exists("outputs"):
        os.makedirs("outputs")
    with open("outputs/test.txt", "w") as f:
        f.write("hello world!")
    log_artifacts("outputs")