import requests
import os
import shutil
from download_utils import download_file

this_path = os.path.abspath(__file__)
base_dir = os.path.dirname(this_path)
downloads = os.path.join(base_dir, "downloads")

os.makedirs(downloads, exist_ok=True)

url = "https://1.bp.blogspot.com/-pJzmLLEF1Hw/YUCnHLBT-pI/AAAAAAAAOuc/NFmPGuXOye8vFd8K_kSI70izl7l3g6X-wCPcBGAsYHg/s737/2348160384086_status_48ee16f1889f412e91e7497320258bbc.jpg"
dl_filename = os.path.basename(url)
file_download = os.path.join(downloads, dl_filename)

data = requests.get(url, stream=True)
data.raise_for_status()


# with open(file_download, "wb") as f:
#     f.write(data.content)
#     print("downloaded successfully!")

download_file(url, downloads)
