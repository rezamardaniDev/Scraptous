import requests

response = requests.get(url='https://api.codeyad.com/api/course/getByFilter?pageId=1&take=12&filterBy=all&orderBy=visit')

mydict = dict(response.json())

for data in mydict['data']['data']:
    print(data)