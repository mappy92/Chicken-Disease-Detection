import os
import sys
import logging

# custom logging string
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# create a log directory 
log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir, exist_ok=True)

#intialize the logger 
logging.basicConfig(
    level= logging.INFO,
    format= logging_str,

    handlers=[
        logging.FileHandler(log_filepath), # handle the file path for the logging
        logging.StreamHandler(sys.stdout) # print the log in terminal
    ]
)

logger = logging.getLogger("cnnClassifierLogger")
