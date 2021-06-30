import sqlalchemy 
from sqlalchemy import create_engine
import requests, datetime
import pandas as pd


APIkey = '9d6461f964a087d98456d732ea7c5374'

city = input("input a city: ")

url = 'https://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=' + APIkey

response = requests.post(url)
r= response.json()
main = r['main']
print(main)

col_names = ['name','timestamp', 'temp', 'feels_like']
df = pd.DataFrame(columns  = col_names)
df.loc[len(df.index)] = [datetime.datetime.now(), main['temp'], main['feels_like']]

engine = create_engine('mysql://root:codio@localhost/weather')
df.to_sql('weather_table', con=engine, if_exists='replace', index=False)
