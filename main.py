import sql
import telebot
import requests
from aiogram.types import *

from tokens import sDAYegebot_token
from obrmes import conv_to_dict
import sys
sys.path.insert(0, '/Users/pluttan/Desktop/проекты/sDAYege/sql/')

URL = 'https://api.telegram.org/bot'
bot = telebot.TeleBot(sDAYegebot_token)


def dobutton(d, name, url):
    message_data = {
        'chat_id': d["from_user"]["id"],
        'menu_button':
        '{"type":"web_app","text":"'+name+'","web_app":{"url":"'+url+'"}}'
    }
    request = requests.post(URL + sDAYegebot_token +
                            '/setChatMenuButton', data=message_data)
    return(request.content)


def dobuttonwithzadan(d, no):
    no = str(no)
    while len(no) < 6:
        no = "0"+no
    return dobutton(d, no, 'https://pluttan.github.io/sdayege/fipi/zadania/'+no+'.html')


def bot_forvwrd(d, id):
    bot.forward_message(d["from_user"]["id"], 1325241900, id)


@bot.message_handler()
def send(message):
    d = conv_to_dict(message)
    if d != "err":
        if d["content_type"] == "text":
            text(d)
            print(dobuttonwithzadan(d, d["text"]))
    else:
        print("err")
        bot.reply_to(
            message, """К сожалению, в этом сообщении использованы символы, которые мы распознать пока не можем :(""")


def text(d):
    id = d["from_user"]["id"]
    name = d["from_user"]["first_name"]
    text = d["text"]
    #print(sql.getuser(d))
    print(id, name, text)
    # sql.newmessage(d)


bot.infinity_polling()
