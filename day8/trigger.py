import requests 

ngrok_url = 'https://6b3b-102-89-46-43.ngrok-free.app'
endpoint = f'{ngrok_url}/scrape-mojo'

r = requests.get(endpoint)
print(r.status_code)
print(r.json()['data'])