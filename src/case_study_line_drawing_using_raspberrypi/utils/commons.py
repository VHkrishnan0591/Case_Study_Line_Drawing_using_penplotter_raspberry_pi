import yaml 
import os
from pathlib import Path
from src.case_study_line_drawing_using_raspberrypi import logger


def read_yaml(file_path:Path):
    with open(file_path, 'r') as file:
        try:
            # Load the YAML content
            data = yaml.safe_load(file)
            logger.info(f"yaml file: {file_path} loaded successfully")
            return data
        except yaml.YAMLError as e:
            print(f"Error reading YAML file: {e}")
            return None

def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")
