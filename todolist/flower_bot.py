from todolist.secret import tgtoken 
import telebot
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todolist.settings')
import django
django.setup()
from search_cat.models import Kitten

class MyBot(telebot.TeleBot):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__users = {}
        try:
            self.__load_users()
        except:
            print('No users')
    
    def add_user(self, msg):
        if msg.chat.id not in self.__users:
            self.__users[msg.chat.id] = ''
            self.__save_users()

    def __save_users(self):
        f = open('my_users.txt', 'w')
        for u in self.__users:
            f.write(str(u) + '\n')
        f.close()
    
    def __load_users(self):
        f = open('my_users.txt')
        for line in f:
            self.__users[line] = ''
        f.close()



bot = MyBot(tgtoken)

@bot.message_handler(commands= ['start'])
def start(message):
    print ("У меня начался рабочий день!")
    bot.add_user(message)
    bot.send_message(
        message.chat.id,
        '<b>Я Вас слушаю)</b>', parse_mode='html')
    

@bot.message_handler()
def zdraste(message):
    if message.text == 'ищу котенка':
        k = Kitten.objects.all()
        s = ''
        for i in k:
            s += i.namecat
        bot.send_message(
           message.chat.id,
          'Это не ваш '+ s + '?'
        )

    else:
      

        bot.send_message(
            message.chat.id,
            'И тебе '+ message.text
        )


bot.polling(none_stop=True)
