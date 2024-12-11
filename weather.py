import logging
import requests
from aiogram import Bot, Dispatcher, types
from aiogram import F
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import asyncio

API_TOKEN = '7813164153:AAEfFHBmE78m5FVEYUeAoh20sNwO4Jww2OA'
WEATHER_API_KEY = 'cbfcbbc16d787fbf7bcaf00f330bdf67'

logging.basicConfig(level=logging.INFO)

bot = Bot('7813164153:AAEfFHBmE78m5FVEYUeAoh20sNwO4Jww2OA')
dp = Dispatcher()

keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Toshkent"), KeyboardButton(text="Farg'ona")],
        [KeyboardButton(text="Namangan"), KeyboardButton(text="Andijon")],
        [KeyboardButton(text="Buxoro"), KeyboardButton(text="Samarqand")],
        [KeyboardButton(text="Xiva"), KeyboardButton(text="Qarshi")],
        [KeyboardButton(text="Termiz"), KeyboardButton(text="Navoiy")],
        [KeyboardButton(text="Jizzax"), KeyboardButton(text="Guliston")],
        [KeyboardButton(text="Qoraqalpog'iston"), KeyboardButton(text="Angren")],
        [KeyboardButton(text="yakkatut")]
    ],
    resize_keyboard=True
)

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Salom! Ob-havo ma'lumotlarini olish uchun biror shaharni tanlang yoki shahar nomini kiriting.", reply_markup=keyboard)

@dp.message(Command("help"))
async def cmd_help(message: types.Message):
    await message.answer("Shahar nomini tanlang yoki kiriting va men sizga ob-havo ma'lumotlarini beraman.", reply_markup=keyboard)

@dp.message(F.text)
async def get_weather(message: types.Message):
    city_name = message.text
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={WEATHER_API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather = data['weather'][0]
        
        temperature = main['temp']
        description = weather['description']
        await message.answer(f"{city_name} shahrida ob-havo: {temperature}°C, {description}.")
    else:
        await message.answer("Shahar topilmadi. Iltimos, yana urinib ko'ring.")

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
