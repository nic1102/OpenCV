from abc import ABC, abstractmethod


class Social(ABC):
    """
    Неследуют:
                  Telegram
                  Vkontakte
                  Pinterest
    """

    @abstractmethod
    def send_post(self):
        ...