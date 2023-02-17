

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


rect = Rectangle((3.2, -4.3), (7.52, 3.14))
print(rect.get_pos(), rect.get_size())
rect.move(1.32, -5)
print(rect.get_pos(), rect.get_size())
print()
rect = Rectangle((7.52, -4.3), (3.2, 3.14))
print(rect.get_pos(), rect.get_size())
rect.resize(23.5, 11.3)
print(rect.get_pos(), rect.get_size())
print(rect.get_size())
print(rect.perimeter())