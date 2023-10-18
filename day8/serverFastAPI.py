from fastapi import FastAPI
from scrape import run as run_scrapper
from logger import trigger_log_save

app = FastAPI()

# @app.route("/", "GET")
@app.post("/")
def helloworld():
    return ("Hello world")#: "yeao"}

@app.route("/scrape-mojo", methods = ['POST'])
def scrape_mojo():
    trigger_log_save()
    run_scrapper()
    return {"data":"Done"}