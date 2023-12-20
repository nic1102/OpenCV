from Triangulation import Triangulation

if __name__ == "__main__":
    ex = Triangulation("images/list.jpg")
    ex.do_triangulation(10000, 0.003, 50)
