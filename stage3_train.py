from src.utils.all_utils import read_config, create_directory
import argparse
import pandas as pd
import os
from sklearn.linear_model import ElasticNet
import joblib

def train_model(config_path, params_path):
    config = read_config(config_path)
    params = read_config(params_path)

    artifcats_dir = config["artifacts"]["artifcats_dir"]
    split_data_dir = config["artifacts"]["split_data_dir"]
    train_file_path= config["artifacts"]["train"]

    random_state = params["base"]["random_state"]
    l1_ratio = params["models"]["ElasticNet"]["l1_ratio"]
    alpha = params["models"]["ElasticNet"]["alpha"]

    train_local_dir = os.path.join(artifcats_dir, split_data_dir, train_file_path)
    train = pd.read_csv(train_local_dir, sep=";")

    train_X = train.drop('quality', axis=1)
    train_y = train['quality']

    lr = ElasticNet(alpha=alpha, l1_ratio=l1_ratio, random_state=random_state)
    print("Training .........")
    lr.fit(train_X, train_y)
    print("Done ......")

    # save the model to disk
    model_path = config["artifacts"]["model_save_path"]
    filename = 'Elastic_Model.sav'
    model_name = os.path.join(model_path,filename)
    joblib.dump(lr, model_name)
    print(f"Model saved at {model_path}")

if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--config", "-c", default="configuration/config.yaml")
    args.add_argument("--params", "-p", default="params.yaml")
    parsed_args = args.parse_args()

    train_model(config_path=parsed_args.config, params_path=parsed_args.params)
