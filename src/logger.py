# import logging

# import os

# from datetime import datetime


# LOG_FILE = f"{datetime.datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
# log_path = os.path.join(os.getcwd(), "logs",LOG_FILE)
# os.makedirs(log_path,exist_ok=True)
# LOG_FILE_PATH = os.path.join(log_path,LOG_FILE)

# logging.basicConfig(
#     filename=LOG_FILE_PATH,
#     format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
#     level=logging.INFO,
# )




import logging
import os
from datetime import datetime

# Create a log file name based on the current date and time
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Create a directory path for logs
log_dir = os.path.join(os.getcwd(), "logs")

# Ensure the log directory exists
os.makedirs(log_dir, exist_ok=True)

# Full path for the log file
LOG_FILE_PATH = os.path.join(log_dir, LOG_FILE)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
