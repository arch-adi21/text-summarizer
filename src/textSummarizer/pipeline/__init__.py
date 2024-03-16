import os
import urllib.request as request
import zipfile
from pathlib import Path
from textSummarizer.logging import logger
from textSummarizer.utils.common import get_size
from textSummarizer.entity import DataIngestionConfig

class DataIngestion :
    def __init__ (self , config:DataIngestionConfig) :
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename , header = request.urlretrieve(
                url = self.config.source_url,
                filename= self.config.local_data_file
            )
            logger.info(f"Downloaded {filename} to {self.config.local_data_file}")
        else:
            logger.info(f"{self.config.local_data_file} already exists of size : {get_size(Path(self.config.local_data_file))}")

    def extract_zip_file(self):
        """
        zip_file_path : str
        Extracts the zip file into the data directory
        function returns none
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)