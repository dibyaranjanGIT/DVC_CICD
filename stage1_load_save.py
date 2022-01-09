from src.utils.all_utils import read_config,create_directory
import argparse
import pandas as pd
import os

def get_data(config_path):
    config = read_config(config_path)
    remote_data_path = config["data_source"]
    df = pd.read_csv(remote_data_path, sep=";")

    # Save data set in local
    artifcats_dir = config["artifacts"]["artifcats_dir"]
    raw_file_dir = config["artifacts"]["raw_local_dir"]
    raw_local_file = config["artifacts"]["raw_local_file"]

    raw_local_dir_path = os.path.join(artifcats_dir, raw_file_dir)
    create_directory(dirs=[raw_local_dir_path])

    raw_local_file_path = os.path.join(raw_local_dir_path, raw_local_file)
    df.to_csv(raw_local_file_path, sep=";", index=False)

if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--config", "-c", default="configuration/config.yaml")
    parsed_args = args.parse_args()

    get_data(config_path=parsed_args.config)
