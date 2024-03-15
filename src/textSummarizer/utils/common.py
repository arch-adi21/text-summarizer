import os
from textSummarizer.logging import logger
from box.exceptions import BoxException
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import yaml

@ensure_annotations
def read_yaml(path_to_yaml : path) -> ConfigBox:
    """
    Read a yaml file and return a ConfigBox object.

    Parameters
    ----------
    path_to_yaml : path
        The path to the yaml file.

    Returns
    -------
    ConfigBox
        A ConfigBox object.
    """
    with open(path_to_yaml, 'r') as f:
        try:
            return ConfigBox(yaml.safe_load(f))
            logger.info(f"Read yaml file {path_to_yaml}")
        except yaml.YAMLError as e:
            logger.error(f"Error reading yaml file {path_to_yaml}: {e}")
            raise BoxException(f"Error reading yaml file {path_to_yaml}: {e}")


@ensure_annotations
def create_directories(path_to_dir : list , verbose = True) : 
    """
    Create a list of directories.

    Parameters
    ----------
    path_to_dir : list
        A list of paths to directories.
    verbose : bool, optional
        Whether or not to print a message. The default is True.

    Returns
    -------
    None.
    """
    for path in path_to_dir :
        os.makedirs(path, exist_ok=True)
        if verbose :
            logger.info(f"Created directory {path}")
