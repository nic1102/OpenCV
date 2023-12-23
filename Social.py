from abc import ABC, abstractmethod


class Social(ABC):
    @abstractmethod
    def send_post(self):
        ...