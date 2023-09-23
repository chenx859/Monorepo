import logging 
import os  
from datetime import datetime 



#Define the variables for Logging  (Directory Name/File Log Name) : 
Directory_Name=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}" # Directory Name 
File_Log_Name=Directory_Name+".log" 
Directory_path=os.path.join(os.getcwd(),"logs",Directory_Name) # Directory Path 
os.makedirs(Directory_path,exist_ok=True)  # create a directory for the log file 
LOG_FILE_PATH=os.path.join(Directory_path,File_Log_Name) # 
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)


print(os.getcwd())