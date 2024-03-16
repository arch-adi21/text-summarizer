import os
from textSummarizer.logging import logger
from box.exceptions import BoxValueError
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import yaml

@ensure_annotations
def read_yaml(path_to_yaml : Path) -> ConfigBox:
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
    try:
        with open(path_to_yaml, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file : {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        logger.error(f"could not load yaml file: {path_to_yaml}")
        raise ValueError("could not load yaml file: {path_to_yaml}")
    except Exception as e:
        logger.error(f"some unnowkn error: {e}")
        return e


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

def get_size(path:Path) -> str:
    """
    Get the size of a file.

    Parameters
    ----------
    path : path
        The path to the file.

    Returns
    -------
    str
        The size of the file.
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"{size_in_kb} KB"