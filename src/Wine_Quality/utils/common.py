import os
from box.exceptions import BoxValueError
import yaml
from Wine_Quality import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml: Path)-> ConfigBox:
    """
    Read YAML file and convert it to a ConfigBox.
    """
    try:
        with open(path_to_yaml, 'r') as file:
            content = yaml.safe_load(file)
            logger.info(f"File read successfully: {path_to_yaml}")
            return ConfigBox(content)
        
    except BoxValueError as e:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directory(path_to_directory: list, verbose=True):
    """
    Create directory if it does not exist.
    """
    for path in path_to_directory:
        if not os.path.exists(path):
            os.makedirs(path)
            if verbose:
                logger.info(f"Directory created: {path}")
        else:
            if verbose:
                logger.info(f"Directory already exists: {path}")

@ensure_annotations
def save_json(path: Path, data: dict):
    """
    Save dictionary as JSON file.
    """
    with open(path, 'w') as file:
        json.dump(data, file, indent=4)
    logger.info(f"File saved successfully: {path}")
    
@ensure_annotations
def load_json(path: Path)-> ConfigBox:
    with open(path) as f:
        content = json.load(f)

    logger.info(f"File loaded successfully: {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any, path: Path):
    """
    Save data as binary file.
    """
    joblib.dump(value = data, filename=path)
    logger.info(f"File saved successfully: {path}")

@ensure_annotations
def load_bin(path: Path)-> Any:
    """
    Load binary file.
    """
    data = joblib.load(filename=path)
    logger.info(f"File loaded successfully: {path}")
    return data

@ensure_annotations
def get_size(path: Path)-> str:
    """
    Get size of file.
    """
    size_in_kb =  round(os.path.getsize(path)/1024)
    return f"~{size_in_kb} KB"