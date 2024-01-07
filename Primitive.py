class Triangle:
    """
    triangle = [(x1,y1), (x2,y2), (x3,y3)]
    sides = [
             ((x1,y1),(x2,y2)),
             ((x2,y2),(x3,y3)),
             ((x3,y3),(x1,y1))
            ]
    fill = (red, green, blue)
    """

    def __init__(self, triangle: tuple, fill: tuple, number: int):
        self.sides = list()
        self.neighbors = list()
        self.triangle = triangle
        self.sides.append((triangle[0], triangle[1]))
        self.sides.append((triangle[1], triangle[2]))
        self.sides.append((triangle[2], triangle[0]))
        self.fill = fill
        self.is_counted = False
        self.number = number
        self.odc = fill[0] * 256 ** 2 + fill[1] * 256 + fill[2]


class Point:
    def __init__(self, xy: tuple):
        self.x = xy[0]
        self.y = xy[1]




