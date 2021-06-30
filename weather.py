import requests


APIkey = '9d6461f964a087d98456d732ea7c5374'

city = input("input a city: ")

url = 'https://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=' + APIkey

response = requests.post(url)
r= response.json()
print(r)