from sensor.exception import SensorException
import sys,os
from sensor.logger import logging
from sensor.utils import dump_csv_file_to_mongodb_collection

# def test_exception():
#     try:
#         logging.info("Checking logging")
#         a=1/0
#     except Exception as e:
#         raise SensorException(e,sys)

if __name__ == "__main__":
    # try:
    #     test_exception()
    # except Exception as e:
    #     print(e)

    file_path= os.path.join(os.getcwd(),'aps_failure_training_set1.csv')
    database_name= "sensor"
    collection_name= "sensor_data"
    try:
        dump_csv_file_to_mongodb_collection(file_path, database_name, collection_name)
    
    except Exception as e:
        raise SensorException(e,sys)