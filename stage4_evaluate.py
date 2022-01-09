from src.utils.all_utils import read_config, save_reports
import argparse
import pandas as pd
import os
from sklearn.metrics import mean_squared_error,mean_absolute_percentage_error,r2_score
import joblib

def evalue_metrics(actual_values, predicted_values):
    mse = mean_squared_error(actual_values, predicted_values)
    mape = mean_absolute_percentage_error(actual_values, predicted_values)
    r2_error = r2_score(actual_values, predicted_values)
    return  mse, mape, r2_error

def evaluate_model(config_path, params_path):
    config = read_config(config_path)

    artifcats_dir = config["artifacts"]["artifcats_dir"]
    split_data_dir = config["artifacts"]["split_data_dir"]
    test_file_path= config["artifacts"]["test"]
    loaded_model_path = config["artifacts"]["model_save_path"]
    model_name = config["artifacts"]["model_name"]

    test_local_dir = os.path.join(artifcats_dir, split_data_dir, test_file_path)
    test = pd.read_csv(test_local_dir, sep=";")

    loaded_model_file = os.path.join(loaded_model_path, model_name)

    test_X = test.drop('quality', axis=1)
    test_y = test['quality']

    loaded_model = joblib.load(loaded_model_file)
    result = loaded_model.predict(test_X)

    error = mean_squared_error(test_y, result)

    scores_dir = config["artifacts"]["reports_dir"]
    scores_file = config["artifacts"]["scores"]

    mse, mape, r2_error = evalue_metrics(test_y, result)
    scores = {
        "mean_squared_error" : mse,
        "mean_absolute_percentage_error": mape,
        "r2_score": r2_error
    }

    score_file_path = os.path.join(scores_dir,scores_file)
    save_reports(scores, score_file_path)

if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--config", "-c", default="configuration/config.yaml")
    args.add_argument("--params", "-p", default="params.yaml")
    parsed_args = args.parse_args()

    evaluate_model(config_path=parsed_args.config, params_path=parsed_args.params)
