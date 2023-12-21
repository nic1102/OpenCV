from Triangulation import Triangulation

if __name__ == "__main__":
    ex = Triangulation("images/096.JPG")
    ex.do_triangulation(100000, 0.0003, 100)
