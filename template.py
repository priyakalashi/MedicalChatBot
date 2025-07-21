import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')
list_of_files=[
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    "setup.py",
    "app.py",
    "research/trials.ipynb"
]


for filepath in list_of_files:
     filepath = Path(filepath)
     filedir,filename = os.path.split(filepath)

     if filedir !="":
          os.makedirs(filedir,exist_ok=True)
          logging.info(f"Creating directory; {filedir} for the file: {filename} ")
          logging.info(f"Name of dir :{filedir}")

    # if (os.path.exists(filepath)):
          f1 = open(filepath,"w")
          logging.info(f"creating empty file: {filepath}")

     #else:
      #  logging.info(f"{filename} already exists")


          
               
