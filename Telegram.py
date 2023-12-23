import telebot
from Social import Social
from secret import telegram_token


class Telegram(Social):

    def __init__(self, channel_name="@nic1102_test"):
        self.bot = telebot.TeleBot(telegram_token)
        self.channel_name = channel_name
        self.image_list = list()

    def create_image_list(self):
        ...

    def send_post(self):
        # self.bot.send_media_group(channel_name, [telebot.types.InputMediaPhoto(photo) for photo in photos])
        ...

