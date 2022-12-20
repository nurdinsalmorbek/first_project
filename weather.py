import requests
import datetime
from pprint import pprint
from config import open_weather_token

def get_weather(city,open_weather_token):

    emojis = {
        'Clear' : 'Clear \U00002600',
        'Clouds':'Cloudy \U00002601',
        'Rain':'Rainy \U00002614',
        'Thunder':'Thunder \U000026A1',
        'Snow': 'Snow \U0001F328',
        'Fog':'Fog \U0001F32B' 
    }


    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&&appid={open_weather_token}&units=metric"
        )
        data = r.json()
        pprint(data)

        city = data['name']
        curr_weather = data['main']['temp']

        weather_description = data['weather'][0]['main']

        if weather_description in emojis:
            wd = emojis[weather_description]
        else:
            wd = "Look out the window, I do not know what weather is outside"
        
        curr_weather = data['main']['temp']
        wind = data['wind']['speed']
        sunrise_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        sunset_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunset'])

        print(f'Weather in: {city}\nTemperature: {curr_weather}C° {wd}\n'
        f'Speed of wind is: {wind}\n'
        f'Sunrise at: {sunrise_timestamp}\n'
        f'Sunset at: {sunset_timestamp}\n'
        f'Have a good day!'
        )

    except Exception as ex:
        print(ex)
        print('Check name of city')

def main():
    city = input("Enter your city: ")
    get_weather(city,open_weather_token)

if __name__ == '__main__':
    main( )