from Triangulation import Triangulation
from Telegram import Telegram
if __name__ == "__main__":
    tr = Triangulation("images/heart.png")
    tr.do_triangulation(1000, 0.00003, 45)
    #s = Telegram()