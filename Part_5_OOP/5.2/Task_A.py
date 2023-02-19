"""Давайте расширим функционал класса, написанного вами в задаче «Классная точка 2.0».
Создайте класс PatchedPoint — наследника уже написанного вами Point.
Требуется реализовать следующие виды инициализации нового класса:
параметров не передано — координаты точки равны 0;
передан один параметр — кортеж с координатами точки;
передано два параметра — координаты точки"""


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




point = PatchedPoint()
print(point.x, point.y)
point.move(2, -3)
print(point.x, point.y)
# first_point = PatchedPoint((2, -7))
# second_point = PatchedPoint(7, 9)
# print(first_point.length(second_point))
# print(second_point.length(first_point))