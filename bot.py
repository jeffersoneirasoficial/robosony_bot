import telebot

bot = telebot.TeleBot('366039663:AAGVVoNeUqAJamxHJ6ZCuO3_TnAaWPU03Xs')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Bem-vindo ao Bot!")

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, "Posso ajudar?")

@bot.message_handler(commands=['information'])
def send_welcome(message):
    bot.reply_to(message, "Oi eu sou o Bot Robo Sony e estou aqui para lhe ajudar!")

bot.polling()
