import requests, os
import datetime
import pandas as pd
from requests_html import HTML

now = datetime.datetime.now()
year = now.year
# print(now)
# print('-----------')
# print(year)
base_dir = os.path.dirname(os.path.abspath(__file__))
def url_to_html(url, filename = "mojo.html"):
    req = requests.get(url)
    if(req.status_code == 200):
        htm_source_code = req.text
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(htm_source_code)
        return htm_source_code
    return " "

def url_txt(url, filename = "world.html", save = False):
    req = requests.get(url)
    txt = req.text
    if req.status_code == 200:
        if save:
            with open(f"world-{year}.html", "w") as f:
                f.write(txt)

        return txt
    return ""

def parse_and_extract(url, name):
    html2txt = url_txt(url)
    html_r = HTML(html=html2txt)
    tableClass = ".imdb-scroll-table"
    r_table = html_r.find(tableClass)
# print(r_table)

    table_data = []
    header_names = []
    if len(r_table) == 1:
    # print(r_table[0].text)
        parsed_table = r_table[0]
        rows = parsed_table.find("tr")
        header_row = rows[0]
        header_cols = header_row.find("th")
        header_names = [x.text for x in header_cols]

    
        for row in rows[1:]:
            cols = row.find("td")
            row_data = []
            for i, col in enumerate(cols):
            # print(i, col.text, "\n")
                row_data.append(col.text)
            table_data.append(row_data)

# defining the data frame
      
    path  = os.path.join(base_dir, 'data')
    os.makedirs(path, exist_ok=True)
    df = pd.DataFrame(table_data, columns=header_names)
    df.to_csv(f'data/{name}.csv', index=False)