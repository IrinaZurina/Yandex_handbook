"""Разработайте класс Point, который при инициализации принимает координаты точки на декартовой плоскости и сохраняет
их в поля x и y соответственно."""


class Point:

    def __init__(self, x_coord, y_coord):
        self.x = x_coord
        self.y = y_coord


point = Point(3, 5)
print(point.x, point.y)
