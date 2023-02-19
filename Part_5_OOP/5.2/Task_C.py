"""Давайте вспомним о реализованном нами методе move(x, y) и напишем ему альтернативу в виде операторов + и +=.
При выполнении кода point + (x, y), создаётся новая точка, которая отличается от изначальной на
заданное кортежем расстояние по осям x и y.
При выполнении кода point += (x, y) производится перемещение изначальной точки.
Напомним, что сейчас мы модернизируем только класс PatchedPoint."""


class Point:

    def __init__(self, x_coord, y_coord):
        self.x = int(x_coord)
        self.y = int(y_coord)

    def move(self, distance_x, distance_y):
        self.x += distance_x
        self.y += distance_y

    def length(self, point2):
        distance = round(((point2.x - self.x) ** 2 + (point2.y - self.y) ** 2) ** 0.5, 2)
        return distance


class PatchedPoint(Point):

    def __init__(self, *other, x_coord=0, y_coord=0):
        if len(list(other)) == 1:
            self.x = list(other)[0][0]
            self.y = list(other)[0][1]
        elif len(list(other)) == 2:
            self.x = list(other)[0]
            self.y = list(other)[1]
        else:
            self.x = x_coord
            self.y = y_coord

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __repr__(self):
        return f'PatchedPoint({self.x}, {self.y})'

    def __add__(self, other: tuple):
        new_point = PatchedPoint(self.x + other[0],
                                 self.y + other[1])
        return new_point

    def __iadd__(self, other: tuple):
        self.x += other[0]
        self.y += other[1]
        return self


first_point = second_point = PatchedPoint((2, -7))
first_point += (7, 3)
print(first_point, second_point, first_point is second_point)

