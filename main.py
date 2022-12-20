import requests
import datetime
from config import t_bot, open_weather_token
import logging
from aiogram import Bot, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

button1 = KeyboardButton('Hi!')
button2 = KeyboardButton("Picture")
button3 = KeyboardButton('Song')
keyboard1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(button1, button2, button3)


bot = Bot(token=t_bot)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply("Hello!\nI'm bot by Nurdin\nSend me a name of city to get know the weather", reply_markup=keyboard1)


@dp.message_handler()
async def kb_answer(message: types.Message):
    if message.text == 'Hi!':
        await message.answer('Hello! How are you?')
    elif message.text == 'Picture':
        r = open('1.jpg', 'rb')
        await bot.send_photo(message.chat.id, photo=r)
    elif message.text =='Song':
        r2 = open('2.mp3', 'rb')
        await bot.send_audio(message.chat.id, audio=r2)


@dp.message_handler()
async def send_weather(message: types.Message):
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
                f"https://api.openweathermap.org/data/2.5/weather?q={message.text}&&appid={open_weather_token}&units=metric"
            )
            data = r.json()


            city = data['name']

            weather_description = data['weather'][0]['main']

            if weather_description in emojis:
                wd = emojis[weather_description]
            else:
                wd = "Look out the window, I do not know what weather is outside"
            
            curr_weather = data['main']['temp']
            wind = data['wind']['speed']
            sunrise_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
            sunset_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunset'])

            await message.reply(f'Weather in: {city}\nTemperature: {curr_weather}C° {wd}\n'
            f'Speed of wind is: {wind}\n'
            f'Sunrise at: {sunrise_timestamp}\n'
            f'Sunset at: {sunset_timestamp}\n'
            f'Have a good day!'
            )

        except: 
            await message.reply('\U00002620 Check name of city \U00002620')



if __name__ == '__main__':
   executor.start_polling(dp, skip_updates=True)