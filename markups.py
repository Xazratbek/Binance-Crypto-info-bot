from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

btnrandom = KeyboardButton("Ixtiyoriy juftlik 🎲")
expensive_crypto = KeyboardButton("Eng Qimmat 🤑💲")
trand_crypto = KeyboardButton("Eng Tranddagi 📈")
btnmainmenu = KeyboardButton("Asosiy menuga 🔙")
#Eng qimmat Crypto Valyutalar uchun tugmalar yaratib olamiz
expensive_crypto_btn1 = KeyboardButton("BTCUSDT 💲")
expensive_crypto_btn2 = KeyboardButton("ETHUSDT 💲")
expensive_crypto_btn3 = KeyboardButton("BNBUSDT 💲")
expensive_crypto_btn4 = KeyboardButton("LINKUSDT 💲")
expensive_crypto_btn5 = KeyboardButton("BTCBUSD 💲")
expensive_crypto_btn6 = KeyboardButton("BTCEUR 💲")
expensive_crypto_btn7 = KeyboardButton("BTCTRY 💲")
expensive_crypto_btn8 = KeyboardButton("BTCBRL 💲")
expensive_crypto_btn9 = KeyboardButton("BTCAUD 💲")
expensive_crypto_btn10 = KeyboardButton("BTCGBP 💲")

#Eng tranddagi Crypto Valyutalar uchun tugmalar yaratib olamiz
trand_crypto_bnt1 = KeyboardButton("BTCUSDT 💲")
trand_crypto_bnt2 = KeyboardButton("ETHUSDT 💲")
trand_crypto_bnt3 = KeyboardButton("BNBUSDT 💲")
trand_crypto_bnt4 = KeyboardButton("LTCUSDT 💲")
trand_crypto_bnt5 = KeyboardButton("SOLUSDT 💲")
trand_crypto_bnt6 = KeyboardButton("LUNAUSDT 💲")
trand_crypto_bnt7 = KeyboardButton("ADAUSDT 💲")
trand_crypto_bnt8 = KeyboardButton("MANAUSDT 💲")
trand_crypto_bnt9 = KeyboardButton("AVAXUSDT 💲")
trand_crypto_bnt10 = KeyboardButton("LINKUSDT 💲")

#Eng qimmat Crypto Valyutalar uchun menu yaratib olamiz
expensive_crypto_menu = ReplyKeyboardMarkup(resize_keyboard=True).add(expensive_crypto_btn1,expensive_crypto_btn2,expensive_crypto_btn3,expensive_crypto_btn4,expensive_crypto_btn5,expensive_crypto_btn6,expensive_crypto_btn7,expensive_crypto_btn8,expensive_crypto_btn9,expensive_crypto_btn10,btnrandom).row(btnmainmenu)

#Eng tranddagi Crypto Valyutalar uchun menu yaratib olamiz
trand_crypto_menu = ReplyKeyboardMarkup(resize_keyboard=True).add(trand_crypto_bnt1,trand_crypto_bnt2,trand_crypto_bnt3,trand_crypto_bnt4,trand_crypto_bnt5,trand_crypto_bnt6,trand_crypto_bnt7,trand_crypto_bnt8,trand_crypto_bnt9,trand_crypto_bnt10,btnrandom).row(btnmainmenu)

#Asosiy menu uchun 🎲 expensive_crypto_menu va trand_crypto_menu larni qo'shib olamiz
mainmenu = ReplyKeyboardMarkup(resize_keyboard=True).add(expensive_crypto,trand_crypto,btnrandom)