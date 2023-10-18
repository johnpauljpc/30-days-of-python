import os
import datetime

now = str(datetime.datetime.now())
BASE_DIR = os.path.dirname(__file__)
log_dir = os.path.join(BASE_DIR, "logs")
os.makedirs(log_dir, exist_ok=True)
now = str(datetime.datetime.now()).replace(":",".")
def trigger_log_save():

    filename = f"{now}.txt"
    print("------------------------>")
    print(type(filename))
    print("log dir  ", log_dir)
    
    filepath = os.path.join(log_dir, filename)
    print("--------------------==>>")
    print(filepath)
    with open(filepath, "w+") as f:
        f.write("")

