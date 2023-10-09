import os, shutil, requests
def download_file(url, directory):
    dl_filename = os.path.basename(url)
    new_dl_path= os.path.join(directory, dl_filename)

    with requests.get(url, stream=True) as r:
        with open(new_dl_path, "wb") as f_obj:
            shutil.copyfileobj(r.raw, f_obj)

    return new_dl_path #or print (new_dl_path)

