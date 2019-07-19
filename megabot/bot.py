import sys
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters    #Updater - абстрактное описание абстрактного бота
import logging

import settings



logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def greet_user(bot, update):
    text = 'Вызван /start'
    logging.info(text)
    update.message.reply_text(text)

def talk_to_me(bot, update):
    user_text = "Привет {}! Ты написал: {}".format(update.message.chat.first_name, update.message.text)
    logging.info("User: %s, Chat id: %s, Message: %s", update.message.chat.username, update.message.chat.id,
                update.message.text)
    print(update.message)
    update.message.reply_text(user_text)

def main():
    #mybot = Updater(API_KEY, request_kwargs=PROXY) #конкретный бот, который будет ломиться на платформу
    mybot = Updater(settings.API_KEY) #конкретный бот, который будет ломиться на платформу
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user)) 
    dp.add_handler(MessageHandler(Filters.text, talk_to_me)) 
    
    mybot.start_polling()   #начни регулярно ходить на платформу телеграмм и проверять наличие сообщений
    mybot.idle()            #mybot будет работать пока его принудительно не остановим



if __name__ == "__main__":
    sys.exit(int(main() or 0))


