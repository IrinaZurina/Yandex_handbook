""" Разработайте методы:
turn() — поворачивает прямоугольник на 90&deg; по часовой стрелке вокруг его центра;
scale(factor) — изменяет размер в указанное количество раз, тоже относительно центра.
Все вычисления производить с округлением до сотых."""


class Rectangle:

    def __init__(self, coord1: tuple, coord2: tuple):
        self.a = list(coord1)
        self.c = list(coord2)
        self.side1 = coord2[1] - coord1[1] if coord2[1] > coord1[1] else coord1[1] - coord2[1]
        self.side2 = coord2[0] - coord1[0] if coord2[0] > coord1[0] else coord1[0] - coord2[0]

    def perimeter(self):
        return round(self.side1 * 2 + self.side2 * 2, 2)

    def area(self):
        return round(self.side1 * self.side2, 2)

    def get_pos(self):
        bx = min(self.a[0], self.c[0])
        by = max(self.a[1], self.c[1])
        return round(bx, 2), round(by, 2)

    def get_size(self):
        return round(self.side2, 2), round(self.side1, 2)

    def move(self, dx, dy):
        self.a[0] += dx
        self.a[1] += dy
        self.c[0] += dx
        self.c[1] += dy
        return self.a, self.c

    def resize(self, width, length):
        if self.a[0] < self.c[0]:
            self.c[0] = self.a[0] + width
        else:
            self.a[0] = self.c[0] + width
        if self.a[1] == min(self.a[1], self.c[1]):
            self.a[1] = self.c[1] - length
        else:
            self.c[1] = self.a[1] - length
        self.side2 = width
        self.side1 = length
        return self.side2, self.side1, self.a, self.c

    def turn(self):
        if self.a[0] < self.c[0] and self.a[1] < self.c[1]:
            self.a[0] = round(self.a[0] + 0.5 * self.side2 - 0.5 * self.side1, 2)
            self.a[1] = round(self.a[1] + 0.5 * self.side1 + 0.5 * self.side2, 2)
            self.c[0] = round(self.c[0] - 0.5 * self.side2 + 0.5 * self.side1, 2)
            self.c[1] = round(self.c[1] - 0.5 * self.side1 - 0.5 * self.side2, 2)
        elif self.a[0] < self.c[0] and self.a[1] > self.c[1]:
            self.a[0] = round(self.a[0] + 0.5 * self.side2 + 0.5 * self.side1, 2)
            self.a[1] = round(self.a[1] - 0.5 * self.side1 + 0.5 * self.side2, 2)
            self.c[0] = round(self.c[0] - 0.5 * self.side2 - 0.5 * self.side1, 2)
            self.c[1] = round(self.c[1] + 0.5 * self.side1 - 0.5 * self.side2, 2)
        elif self.a[0] > self.c[0] and self.a[1] > self.c[1]:
            self.c[0] = round(self.c[0] + 0.5 * self.side2 - 0.5 * self.side1, 2)
            self.c[1] = round(self.c[1] + 0.5 * self.side1 + 0.5 * self.side2, 2)
            self.a[0] = round(self.a[0] - 0.5 * self.side2 + 0.5 * self.side1, 2)
            self.a[1] = round(self.a[1] - 0.5 * self.side1 - 0.5 * self.side2, 2)
        else:
            self.c[0] = round(self.c[0] + 0.5 * self.side2 + 0.5 * self.side1, 2)
            self.c[1] = round(self.c[1] - 0.5 * self.side1 + 0.5 * self.side2, 2)
            self.a[0] = round(self.a[0] - 0.5 * self.side2 - 0.5 * self.side1, 2)
            self.a[1] = round(self.a[1] + 0.5 * self.side1 - 0.5 * self.side2, 2)
        self.side1, self.side2 = self.side2, self.side1

    def scale(self, factor):
        if self.a[0] < self.c[0] and self.a[1] < self.c[1]:
            self.a[0] = round(self.a[0] - (self.side2 / 2) * (factor - 1), 2)
            self.a[1] = round(self.a[1] - (self.side1 / 2) * (factor - 1), 2)
            self.c[0] = round(self.c[0] + (self.side2 / 2) * (factor - 1), 2)
            self.c[1] = round(self.c[1] + (self.side1 / 2) * (factor - 1), 2)
        elif self.a[0] < self.c[0] and self.a[1] > self.c[1]:
            self.a[0] = round(self.a[0] - (self.side2 / 2) * (factor - 1), 2)
            self.a[1] = round(self.a[1] + (self.side1 / 2) * (factor - 1), 2)
            self.c[0] = round(self.c[0] + (self.side2 / 2) * (factor - 1), 2)
            self.c[1] = round(self.c[1] - (self.side1 / 2) * (factor - 1), 2)
        elif self.a[0] > self.c[0] and self.a[1] > self.c[1]:
            self.a[0] = round(self.a[0] + (self.side2 / 2) * (factor - 1), 2)
            self.a[1] = round(self.a[1] + (self.side1 / 2) * (factor - 1), 2)
            self.c[0] = round(self.c[0] - (self.side2 / 2) * (factor - 1), 2)
            self.c[1] = round(self.c[1] - (self.side1 / 2) * (factor - 1), 2)
        else:
            self.a[0] = round(self.a[0] + (self.side2 / 2) * (factor - 1), 2)
            self.a[1] = round(self.a[1] - (self.side1 / 2) * (factor - 1), 2)
            self.c[0] = round(self.c[0] - (self.side2 / 2) * (factor - 1), 2)
            self.c[1] = round(self.c[1] + (self.side1 / 2) * (factor - 1), 2)
        self.side1 *= round(factor, 2)
        self.side2 *= round(factor, 2)



rect = Rectangle((3.14, 2.71), (-3.14, -2.71))
print(rect.get_pos(), rect.get_size(), sep='\n')
rect.turn()
print(rect.get_pos(), rect.get_size(), sep='\n')
print()
rect = Rectangle((3.14, 2.71), (-3.14, -2.71))
print(rect.get_pos(), rect.get_size(), sep='\n')
rect.scale(2.0)
print(rect.get_pos(), rect.get_size(), sep='\n')