import pandas as pd
from src.logger import logging 
from src.exception import CustomException
import sys
import os

class Data_Loader:
    """
        this class loads the data and transform it to make it ready for modeling 
    """
    def __init__(self,path):
        logging.info("initialize data loader object")
        self.path=path

    def get_data(self):
        """
        this function loads the data from its source

        Raises:
            CustomException: raise exception if any error occurs 

        Returns:
            data : dataframe
        """
        
        try:
            logging.info("getting data from source")
            self.data= pd.read_csv(self.path) # reading the data file
            return self.data
        except Exception as e:
          raise CustomException(e,sys)
      
      
    def convert_timestamp(self) : 
        """
        this function converts a feature of unknown type to timestamp

        Raises:
            CustomException: raise exception if any error occurs 

        Returns:
            data : dataframe
        """
        try : 
            logging.info('convert field to timestamp')
            self.data['timestamp'] = pd.to_datetime(self.data['timestamp']) 
            return self.data 
        except Exception as e : 
            raise CustomException(e,sys) 
    
     
     


