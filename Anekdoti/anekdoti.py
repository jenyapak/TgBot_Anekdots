import requests
import random
import telebot
from bs4 import BeautifulSoup as B

URL = "https://www.anekdot.ru/last/good/"
API_KEY = "6045352405:AAGB9yEjRGuiwdU1SuR3BtajEmvnZ-XMOBI" #TOKEN который взяли у BotFather
def parser(URL): #Создаем функцию
    #Создаем get запрос
    response = requests.get(URL)
    #Запускаем xtml Парсер
    soup = B(response.text, "html.parser")
    #Получаем коллекция анектдотов с тегами div and class=text#
    anekdots = soup.find_all("div", class_="text")
    #Очищаем от лищнего мусора, чтобы был один текст
    return [i.text for i in anekdots]

list_of_jokes = parser(URL)
random.shuffle(list_of_jokes)

bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=["start"])

def hello(message):
    bot.send_message(message.chat.id, "Здравствуйте, чтобы посмеяться введите людую цифру(от 1 до 9): ")

@bot.message_handler(content_types=["text"])
def jokes(message):
    if message.text.lower() in "123456789":
        bot.send_message(message.chat.id, list_of_jokes[0])
        del list_of_jokes[0]
    else:
        bot.send_message(message.chat.id, "Введите любую цифру")


#Чтобы обновлял все входящие сообщения от пользователя
bot.polling()