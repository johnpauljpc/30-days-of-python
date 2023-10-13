import requests
import functions
from requests_html import HTML
import pandas as pd
from functions import parse_and_extract





url = "https://www.boxofficemojo.com/year/world/"
# functions.url_to_html(url)

jp = parse_and_extract(url, "newMovie2")