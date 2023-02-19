"""А теперь модернизируем уже новый класс PatchedPoint. Реализуйте магические методы _str__ и _repr__.
При преобразовании в строку точка представляется в формате (x, y).
Репрезентация же должна возвращать строку для инициализации точки двумя параметрами."""


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


point = PatchedPoint()
print(point)
point.move(2, -3)
print(repr(point))
