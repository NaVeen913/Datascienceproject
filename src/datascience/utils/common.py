import os
import json
import joblib
import yaml
from pathlib import Path
from typing import Any, List


from box import ConfigBox
from box.exceptions import BoxValueError

from src.datascience import logger



def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a YAML file and returns its content as a ConfigBox.
    """
    try:
        with open(path_to_yaml, "r") as yaml_file:
            content = yaml.safe_load(yaml_file) or {}
            logger.info(f"YAML file loaded successfully: {path_to_yaml}")
            return ConfigBox(content)

    except BoxValueError:
        raise ValueError("YAML file is empty")

    except Exception as e:
        logger.error(f"Error while reading YAML file: {path_to_yaml} - {e}")
        raise e



def create_directories(path_to_directories: list, verbose: bool = True) -> None:
    """
    Create multiple directories if they do not exist.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory: {path}")
