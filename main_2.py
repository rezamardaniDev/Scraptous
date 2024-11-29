import  requests


parametrs = {'q' : 'salad', 'mark' : 'samsung', 'pages' : [1]}
response = requests.get('https://httpbin.org/get', params=parametrs)
print(response.text)


data = {'username' : 'reza', 'password': '1234'}
# OR
# data = [('username', 'reza'), ('password', '1234')]
response = requests.post(url='https://httpbin.org/post', data=data)
print(response.text)

