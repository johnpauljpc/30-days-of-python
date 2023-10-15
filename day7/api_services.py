# using API service to scrape data


import requests
import pprint
import pandas as pd
api_key = "fbcdaf7c391fedf2d8d129e9da9d44d0"
api_key_v4 = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmYmNkYWY3YzM5MWZlZGYyZDhkMTI5ZTlkYTlkNDRkMCIsInN1YiI6IjY1MmJhMjk5ZWE4NGM3MDBlYmEyMDU5MyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.lMNptNHgoNbEake4igJJqOsSJBDTRCRO5KV5nOFMB0o"


movie_id = 500
api_version = 3

headers = {
    "accept": None,
    "Authorization": f"Bearer {api_key_v4}"
}
base_url = f"https://api.themoviedb.org/{api_version}"
endpoint_path = f"/movie/{movie_id}"
search_path = "/search/movie"
query = "matrix"

endpoint = f"{base_url}{endpoint_path}?api_key={api_key}"
searchEndpoint = f"{base_url}{search_path}?api_key={api_key}&query={query}"

r = requests.get(searchEndpoint)
if r.status_code in range(200, 299):
    data = r.json()
    results = data['results']
    movie_ids = set()

    if (len(results) > 0):
        for result in results:
            _id = result['id']
            # print(result['title'], _id)
            movie_ids.add(_id)

        # print(list(movie_ids))
# Get full details of each searched result
output = "movies.csv"
movie_data = []
for movie_id in movie_ids:
    endpoint_path = f"/movie/{movie_id}"
    endpoint = f"{base_url}{endpoint_path}?api_key={api_key}"
    r = requests.get(endpoint)
    if r.status_code in range(200, 299):
        data = r.json()
        movie_data.append(data)

df = pd.DataFrame(movie_data)
df.to_csv(output, index=False)
        



