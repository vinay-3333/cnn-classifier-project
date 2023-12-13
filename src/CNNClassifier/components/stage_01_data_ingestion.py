import os       #interact with os
import urllib.request as request    #interact with server and i want to request with server and i want ot response
from zipfile import ZipFile
from CNNClassifier import logger   
from pathlib import pathlib
from tqdm import  tqdm    #for creating a progesses path 
from CNNClassifier.entity import DataIngestionConfig
from CNNClassifier.utils import utils


class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config = config
        

    def download_file(self):
        pass


    def get_updated_list_of_files(self):
        pass


    def preprocess(self):
        pass

    def unzip_and_clean(self):
        pass
