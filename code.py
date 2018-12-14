import config
import requests
import telebot
from telebot import apihelper
from telebot import types
import logging
import os
import time


bot = telebot.TeleBot(config.token)

user_inf = []

@bot.message_handler(commands = ['start'])
def start(message):
    print('User is connected')
    bot.send_message(message.chat.id,"Здравствуйте вас приветствует SailetBot")
    questioning(message)

    
def questioning(message):
    bot.send_message(message.chat.id,"Пожалуйста введите ваше имя")
    bot.register_next_step_handler(message,get_name)


def get_name(message):
    
    bot.send_message(message.chat.id,"Пожалуйста введите компанию которую вы представляете")
    bot.register_next_step_handler(message,get_company)
    user_inf.append(message.text)
    
def get_company(message):
    
    bot.send_message(message.chat.id,"Пожалуйста введите ваш номер телефона")
    print(message.chat.id)
    bot.register_next_step_handler(message,get_phone)
    user_inf.append(message.text)

def get_phone(message):
    
    bot.send_message(message.chat.id,"Какова цель вашего обращения")
    bot.register_next_step_handler(message, send_inf_to_admin)
    user_inf.append(message.text)

def send_inf_to_admin(message):
    print(user_inf)
    main_stroke = "Имя: " + user_inf[0] + " \nКомпания: " + user_inf[1] + " \nТелефон: " + user_inf[2]
    bot.send_message(410680216, main_stroke)

    bot.send_message(message.chat.id, "Спасибо ваше обращение успешно подано, если вы захотите отправить нам ещё одно, то воспользуйтесть командой /start")


    
    


if __name__ == '__main__':
    bot.polling(none_stop = True)









