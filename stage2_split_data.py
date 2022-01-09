from src.utils.all_utils import read_config, create_directory
import argparse
import pandas as pd
import os
from sklearn.model_selection import train_test_split

def split_save(config_path, params_path):
    config = read_config(config_path)
    params = read_config(params_path)
    # remote_data_path = config["data_source"]

    # Save data set in local
    artifcats_dir = config["artifacts"]["artifcats_dir"]
    raw_file_dir = config["artifacts"]["raw_local_dir"]
    raw_local_file = config["artifacts"]["raw_local_file"]
    split_data_dir = config["artifacts"]["split_data_dir"]
    split_data_train= config["artifacts"]["train"]
    split_data_test = config["artifacts"]["test"]

    raw_local_dir = os.path.join(artifcats_dir,raw_file_dir)
    raw_local_dir_path = os.path.join(raw_local_dir, raw_local_file)

    df = pd.read_csv(raw_local_dir_path, sep=";")


    split_ratio = params["base"]["test_size"]
    random_state = params["base"]["random_state"]

    train, test = train_test_split(df, test_size=split_ratio, random_state=random_state)

    create_directory([os.path.join(artifcats_dir, split_data_dir),
                      os.path.join(artifcats_dir, split_data_dir)])

    train_data_path1 = os.path.join(artifcats_dir, split_data_dir)
    train_data_path2 = os.path.join(train_data_path1, split_data_train)
    train.to_csv(train_data_path2, sep=";", index=False)

    test_data_path1 = os.path.join(artifcats_dir, split_data_dir)
    test_data_path2 = os.path.join(test_data_path1, split_data_test)
    test.to_csv(test_data_path2, sep=";", index=False)


if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--config", "-c", default="configuration/config.yaml")
    args.add_argument("--params", "-p", default="params.yaml")
    parsed_args = args.parse_args()

    split_save(config_path=parsed_args.config, params_path=parsed_args.params)
