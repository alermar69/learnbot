import sys

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, RegexHandler    #Updater - абстрактное описание абстрактного бота
import settings
from handlers import change_avatar, greet_user, talk_to_me, send_cat_picture, get_contact, get_location







def main():
    #mybot = Updater(API_KEY, request_kwargs=PROXY) #конкретный бот, который будет ломиться на платформу
    mybot = Updater(settings.API_KEY) #конкретный бот, который будет ломиться на платформу
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user, pass_user_data=True)) 
    dp.add_handler(CommandHandler('cat', send_cat_picture, pass_user_data=True)) 
    dp.add_handler(RegexHandler('^(Прислать котика)$', send_cat_picture, pass_user_data=True)) 
    dp.add_handler(RegexHandler('^(Сменить аватарку)$', change_avatar, pass_user_data=True)) 
    dp.add_handler(MessageHandler(Filters.contact, get_contact, pass_user_data=True)) 
    dp.add_handler(MessageHandler(Filters.location, get_location, pass_user_data=True)) 


    dp.add_handler(MessageHandler(Filters.text, talk_to_me, pass_user_data=True)) 
    
    mybot.start_polling()   #начни регулярно ходить на платформу телеграмм и проверять наличие сообщений
    mybot.idle()            #mybot будет работать пока его принудительно не остановим



if __name__ == "__main__":
    sys.exit(int(main() or 0))


