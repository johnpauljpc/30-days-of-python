from flask import Flask
from scrape import run as run_scrapper
from logger import trigger_log_save

app = Flask(__name__)

# @app.route("/", "GET")
@app.get("/")
def helloworld():
    return ("Hello world")#: "yeao"}

@app.route("/scrape-mojo", methods = ['GET'])
def scrape_mojo():
    trigger_log_save()
    run_scrapper()
    return {"data":"Done"}


if __name__ == "__main__":
    app.run(debug=True)