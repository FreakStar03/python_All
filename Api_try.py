import requests


url = 'https://en.wikipedia.org/api/rest_v1/page/summary/Indian_Ocean'

json_data = requests.get(url).json()

json_status = json_data['extract']
print('retrived_data: '+ '\n' + json_status )
