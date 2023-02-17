"""Давайте расширим функционал класса, написанного в прошлой задаче.
Реализуйте методы:
- move, который перемещает точку на заданное расстояние по осям x и y;
- length, который определяет до переданной точки расстояние, округлённое до сотых."""


class Point:

    def __init__(self, x_coord, y_coord):
        self.x = x_coord
        self.y = y_coord

    def move(self, distance_x, distance_y):
        self.x += distance_x
        self.y += distance_y

    def length(self, point2):
        distance = round(((point2.x - self.x) ** 2 + (point2.y - self.y) ** 2) ** 0.5, 2)
        return distance


point = Point(3, 5)
print(point.x, point.y)
point.move(2, -3)
print(point.x, point.y)

first_point = Point(2, -7)
second_point = Point(7, 9)
print(first_point.length(second_point))
print(second_point.length(first_point))
