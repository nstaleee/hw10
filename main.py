from pprint import pprint

import requests

url = 'https://dummyjson.com/todos'

params = {
    'limit': 150,
    'skip': 0,
}

response = requests.get(url=url, params=params)

result = response.json()

todos = result['todos']

for todo in todos:
    if not todo['completed']:
        pprint(todo['todo'])