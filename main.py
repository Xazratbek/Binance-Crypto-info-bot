import datetime as dt
import logging
import random
from crypto_pairs_list import valyuta_juftliklari
from aiogram import Bot, Dispatcher, executor, types
import requests
import markups as nav
import functions as func

API_TOKEN = "5175704595:AAEncGR-YPozBesfdIpcYsKZnm6iLlnIvg4"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)

dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def send_welcome(message: types.Message):
    await message.reply(f"Assalomu Alaykum {message.from_user.first_name} botimizga Xush kelibsiz botga shunchaki valyuta juftliklarini nomini yuboring botimizda 1971-ta Valyuta juftliklari mavjud\nMisol uchun ETHBTC,BNBBTC,BTCUSDT va hkz\nBot haqida ma'lumot oling /help",reply_markup=nav.mainmenu)

@dp.message_handler(commands='help')
async def send_welcome(message: types.Message):
    await message.reply("Botga shunchaki valyuta juftliklarini nomini yuboring\nYoki pastdagi tugmalar orqali eng trenddaagi 📈 Valyuta juftliklar haqida ma'lumot oling\n",reply_markup=nav.mainmenu)


@dp.message_handler()
async def crypto_pair_info(message: types.Message):
    time = dt.datetime.now()
    try:
        if message.text.isalpha():
                await message.reply(func.get_response(message.text),reply_markup=nav.mainmenu)

        elif message.text == "Asosiy menuga 🔙":
            await message.reply("Asosiy Menu 🖥",reply_markup=nav.mainmenu)

        elif message.text == "Eng Qimmat 🤑💲":
            await message.answer("O'zingizga kerakli bo'limni tanlang",reply_markup=nav.expensive_crypto_menu)

        elif(message.text == "BTCUSDT 💲" or message.text == "BTCUSDT" or message.text == "btcusdt"):
            await message.reply(func.get_response("BTCUSDT"))
#             Pastdagi kod Binance.comdan BTCUSDT-ning 💲 ayni vaqtdagi diagrammasini yuborish uchun edi ammo bu botni ishlashiga ta'sir qilgani uchun o'chirib qo'yildi
#             new_message = await message.answer("BTCUSDT-ning 💲 ayni vaqtdagi diagrammasi yuborilmoqda kuting...")
#             url = f"https://api.screenshotbird.com/screenshot?token=nVAxLrfJZlYYStC86ENZ9TLO&url=https://www.binance.com/ru/trade/BTCUSDT&fresh=true&block_ads=true&block_cookie_banners=true&block_tracking=true"
#             r = requests.get(url)
#             res = r.json()
#             await message.reply_photo(res['url'],caption="BTCUSDT-ning 💲 ayni vaqtdagi diagrammasi rasmi 📊📸")
#             await bot.delete_message(message.from_user.id,message_id=new_message.message_id)

        elif (message.text == "ETHUSDT 💲" or message.text == "ETHUSDT" or message.text == "ethusdt"):
            await message.reply(func.get_response("ETHUSDT"))
#           Pastdagi kod Binance.comdan BTCUSDT-ning 💲 ayni vaqtdagi diagrammasini yuborish uchun edi ammo bu botni ishlashiga ta'sir qilgani uchun o'chirib qo'yildi
#             new_message = await message.answer("ETHUSDT-ning 💲 ayni vaqtdagi diagrammasi yuborilmoqda kuting...")
#             url = f"https://api.screenshotbird.com/screenshot?token=nVAxLrfJZlYYStC86ENZ9TLO&url=https://www.binance.com/ru/trade/ETHUSDT&fresh=true&block_ads=true&block_cookie_banners=true&block_tracking=true"
#             r = requests.get(url)
#             res = r.json()
#             await message.reply_photo(res['url'],caption="ETHUSDT-ning 💲 ayni vaqtdagi diagrammasi rasmi 📊📸")
#             await bot.delete_message(message.from_user.id,message_id=new_message.message_id)


        elif message.text == "BNBUSDT 💲":
            await message.reply(func.get_response("BNBUSDT"))

        elif message.text == "LINKUSDT 💲":
            await message.reply(func.get_response("LINKUSDT"))

        elif message.text == "BTCBUSD 💲":
            await message.reply(func.get_response("BTCBUSD"))

        elif message.text == "BTCEUR 💲":
            await message.reply(func.get_response("BTCEUR"))

        elif message.text == "BTCTRY 💲":
            await message.reply(func.get_response("BTCTRY"))

        elif message.text == "BTCBRL 💲":
            await message.reply(func.get_response("BTCBRL"))

        elif message.text == "BTCAUD 💲":
            await message.reply(func.get_response("BTCAUD"))

        elif message.text == "BTCGBP 💲":
            await message.reply(func.get_response("BTCGBP"))

        elif message.text == "LTCUSDT 💲":
            await message.reply(func.get_response("LTCUSDT"))

        elif message.text == "SOLUSDT 💲":
            await message.reply(func.get_response("SOLUSDT"))

        elif message.text == "LUNAUSDT 💲":
            await message.reply(func.get_response("LUNAUSDT"))

        elif message.text == "ADAUSDT 💲":
            await message.reply(func.get_response("ADAUSDT"))

        elif message.text == "MANAUSDT 💲":
            await message.reply(func.get_response("MANAUSDT"))

        elif message.text == "AVAXUSDT 💲":
            await message.reply(func.get_response("AVAXUSDT"))

        elif message.text == "Ixtiyoriy juftlik 🎲":
            crypto_pair = random.choice(valyuta_juftliklari)
            await message.reply(func.get_response(crypto_pair))

        elif message.text == "Eng Tranddagi 📈":
            await message.answer("O'zingizga kerakli bo'limni tanlang",reply_markup=nav.trand_crypto_menu)

    except KeyError:
        await message.reply(f"{message.text.upper()}-valyuta juftligi mavjud emas 🙅‍♂️\n\nXozirgi vaqt: {time.hour}:{time.minute}:{time.second} ⌚️")

    except Exception as e:
        await message.reply(f"Botda xatolik yuz berdi ⚠️\nQayta urunib ko'ring",reply_markup=nav.mainmenu)

if __name__=="__main__":
    executor.start_polling(dp)
