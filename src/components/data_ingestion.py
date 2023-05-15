import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass


# Initially, without use of @dataclass, you have to use __init__ to define variables in the class.
@dataclass # this is decorator, by use of this you can directly  able to define your class variables.
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts',"train.csv")
    # train_data_path is a path link where your output will be save. we write STR because it would be str type,and we create artifact folder and this we create train.csv file.
    # so this hole is the input we are giving, later on the data ingestion will save the train.csv file in this path.
    train_data_path: str=os.path.join('artifacts',"test.csv")
    train_data_path: str=os.path.join('artifacts',"data.csv")
    # so we have defined our data ingestion config. these all are inputs but later on we knows that where the data ingestion files will save.

class DataIngestion:
    def __init__(self)
        self.ingestion_config=DataIngestionConfig() # here i created class varable neame Ingestion_config and this all the above dataclass variables will be save.
        # inside this variable (DataIngestionConfig), there will be sub variables and sub objects.

    def initiate_data_ingestion(self): # this is the self function we create to extract our data from different resources, you can extract data from mongoDB also.
        logging.info("Entered the data ingestion method or component") # logging is also important because it is a way to store information about your script and track events that occur.
        # Setting the log level to INFO will include INFO, WARNING, ERROR, and CRITICAL messages.
        try:                                                      # now this is the way you can exctract data from any source.
            df= pd.read_csv('notebook\Data\StudentsPerformance.csv')   # here we are exctracting our data from a CSV file.
            logging.info('Read the dataset as dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            def.to_csv(self.ingestion_config.raw_data_path, index=False,header=True)
            
            logging.info('Train test split initiated')
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path, index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False,header=True)

            logging.info('Ingestion of the data is completed')

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            raise CustomException(e,sys)
        
# if __name__=="__main__":
#     obj=DataIngestion()
#     obj.initiate_data_ingestion()