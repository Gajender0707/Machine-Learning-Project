import logging
import os
from datetime import datetime

#create the log file
LOG_FILE=f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"
print(LOG_FILE)


##giving the log path for append the all logs in that perticular file.
logs_Path=os.path.join(os.getcwd(),"LOGS",LOG_FILE)
os.makedirs(logs_Path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_Path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format="%(asctime)s-%(lineno)d %(name)s-%(levelname)s-%(message)s",
)