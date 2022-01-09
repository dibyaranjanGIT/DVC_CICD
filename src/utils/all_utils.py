import yaml
import os
import json

def read_config(path_to_yaml: str):
    with open(path_to_yaml) as yaml_file:
        content = yaml.safe_load(yaml_file)

    return content

def create_directory(dirs: list):
    for dir_path in dirs:
        os.makedirs(dir_path, exist_ok=True)
        print(f"{dir_path} is created")

def save_local_df(data, data_path, index_status=False):
    data.to_csv(data_path, index_status)
    print(f"data is save at {data_path}")

def save_reports(reports:dict, report_path:str):
    with open(report_path, "w") as f:
        json.dump(reports, f, indent=5)