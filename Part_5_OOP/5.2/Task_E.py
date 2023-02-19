"""Предусмотрите возможность задать отрицательные числитель и/или знаменатель.
А также перепишите методы __str__ и __repr__ таким образом, чтобы информация об объекте
согласовывалась с инициализацией строкой.
Далее реализуйте оператор математического отрицания — унарный минус."""


class Fraction:

    def __init__(self, *other):
        if type(other[0]) is str:
            self.num = int(other[0].split('/')[0])
            self.denom = int(other[0].split('/')[1])
        else:
            self.num = other[0]
            self.denom = other[1]
        self.num, self.denom = find_gcd(self.num, self.denom)
        self.num, self.denom = check_minus(self.num, self.denom)

    def numerator(self, *number):
        self.num = number[0] if len(number) != 0 else self.num
        self.num, self.denom = find_gcd(self.num, self.denom)
        self.num, self.denom = check_minus(self.num, self.denom)
        return abs(self.num)

    def denominator(self, *number):
        self.denom = number[0] if len(number) != 0 else self.denom
        self.num, self.denom = find_gcd(self.num, self.denom)
        self.num, self.denom = check_minus(self.num, self.denom)
        return abs(self.denom)

    def __str__(self):
        if self.num == 0 or self.denom == 1:
            return f"{self.num}"
        if self.denom < 0 < self.num:
            return f'{-1 * self.num}/{-1 * self.denom}'
        return f'{self.num}/{self.denom}'

    def __repr__(self):
        if self.num == 0 or self.denom == 1:
            return f"Fraction('{self.num}')"
        if self.denom < 0 < self.num:
            return f"Fraction('{-1 * self.num}/{-1 * self.denom}')"
        return f"Fraction('{self.num}/{self.denom}')"

    def __neg__(self):
        return Fraction(-self.num, self.denom)


def find_gcd(x, y):
    gcd = []
    for i in range(2, max(abs(x), abs(y)) // 2 + 1):
        if x % i == 0 and y % i == 0:
            gcd.append(i)
    if len(gcd) != 0:
        x //= max(gcd)
        y //= max(gcd)
        return x, y
    return x, y


def check_minus(a, b):
    if a < 0 and b < 0:
        a *= -1
        b *= -1
    return a, b


a = Fraction(1, 3)
b = Fraction(-2, -6)
c = Fraction(-3, 9)
d = Fraction(4, -12)
print(a, b, c, d)
print(*map(repr, (a, b, c, d)))
print()
a = Fraction('-1/2')
b = -a
print(a, b, a is b)
b.numerator(-b.numerator())
a.denominator(-3)
print(a, b)
print(a.numerator(), a.denominator())
print(b.numerator(), b.denominator())
