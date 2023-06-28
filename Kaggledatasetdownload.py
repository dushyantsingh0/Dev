import kaggle
import pandas as pd


# Set the dataset identifier
dataset_identifier = 'i191796majid/human-genetic-data'

# Download the dataset files 
data = kaggle.api.dataset_download_files(dataset_identifier,path='C:/Users/dushy/OneDrive/Documents/Python_Projects/Dev/Kaggle_Datasets', unzip=True)