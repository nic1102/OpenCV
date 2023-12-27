from Triangulation import Triangulation

if __name__ == "__main__":
    tr = Triangulation("images/heart.png")
    tr.do_triangulation(1000, 0.000004, 45)