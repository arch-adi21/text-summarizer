import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,filemode='w' , format='%(asctime)s - %(levelname)s - %(name)s - %(message)s',filename='template.log')

project_name = 'textSummarizer'
list_of_files = ['.github/workflows/.gitkeep' , 
                    f"src/{project_name}/__init__.py",
                    f"src/{project_name}/components/__init__.py",
                    f"src/{project_name}/utils/__init__.py",
                    f"src/{project_name}/utils/common.py",
                    f"src/{project_name}/logging/__init__.py",
                    f"src/{project_name}/config/__init__.py",
                    f"src/{project_name}/config/configuration.py",
                    f"src/{project_name}/pipeline/__init__.py",
                    f"src/{project_name}/entity/__init__.py",
                    f"src/{project_name}/constants/__init__.py" , 
                    'config/config.yaml' , 
                    "params.yaml" , 
                    "app.py" , 
                    "main.py" , 
                    "Dockerfile" , 
                    "requirements.txt" , 
                    "setup.py" , 
                    "notebooks/trial.ipynb"]

for filepath in list_of_files :
    filepath = Path(filepath)
    filedir , filename = os.path.split(filepath)

    if filedir != "" :
        os.makedirs(filedir , exist_ok=True)
        logging.info(f"created directory {filedir} , for the file {filename}")

    if (not os.path.exists(filename)) or (os.path.getsize == 0) :
        with open(filepath , 'w') as f:
            logging.info(f"created file {filename}")
            pass
    else :
        logging.info(f"file {filename} already exists")
