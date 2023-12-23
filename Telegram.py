import telebot
from secret import telegram_token

class Telegram:
    def __init__(self):
        self.bot = telebot.TeleBot(telegram_token)

    def create_image_list(self):
        ...

    def create_post(self):
        #self.bot.send_media_group("@nic1102_test", [telebot.types.InputMediaPhoto(photo) for photo in photos])
        ...




