import requests, datetime, sqlalchemy 
import pandas as pd
from sqlalchemy import create_engine


def user_input():
    city = input(str("input a city: "))
    print('--------------------------------------')
    print(city)
    return city
    
def get_url(city):
    APIkey = '9d6461f964a087d98456d732ea7c5374'
    url = 'https://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=' + APIkey
    print('--------------------------------------')
    print(url)
    return url
  
def get_json(url):
    response = requests.post(url)
    r = response.json()
    json = r['main']
    print('--------------------------------------')
    print(json)
    return json

def build_dataframe(json):
    col_names = ['timestamp', 'temp', 'feels_like']
    df = pd.DataFrame(columns  = col_names)
    df.loc[len(df.index)] = [datetime.datetime.now(), json['temp'], json['feels_like']]
    engine = create_engine('mysql://root:codio@localhost/weather')
    df.to_sql('weather_table', con=engine, if_exists='replace', index=False)
    

def main():
    city = user_input()
    url = get_url(city)
    json = get_json(url)
    build_dataframe(json)
    
main()