"""Разработайте класс Rectangle.
При инициализации класс принимает два кортежа рациональных координат противоположных углов прямоугольника
(со сторонами параллельными осям координат).
Класс должен реализовывать методы:
perimeter — возвращает периметр прямоугольника;
area — возвращает площадь прямоугольника."""


class Rectangle:

    def __init__(self, coord1: tuple, coord2: tuple):
        self.a = coord1
        self.c = coord2
        self.side1 = coord2[1] - coord1[1] if coord2[1] > coord1[1] else coord1[1] - coord2[1]
        self.side2 = coord2[0] - coord1[0] if coord2[0] > coord1[0] else coord1[0] - coord2[0]

    def perimeter(self):
        return round(self.side1 * 2 + self.side2 * 2, 2)

    def area(self):
        return round(self.side1 * self.side2, 2)


rect = Rectangle((3.2, -4.3), (7.52, 3.14))
print(rect.perimeter())
rect = Rectangle((7.52, -4.3), (3.2, 3.14))
print(rect.area())