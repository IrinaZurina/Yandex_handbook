"""Начнём разработку класса Fraction, который реализует предлагаемые дроби.
Предусмотрите возможность инициализации дроби с помощью двух целых чисел или строки в формате <числитель>/<знаменатель>.
В случаях наличия общего делителя у числителя и знаменателя, дробь следует сократить.
А также реализуйте методы:
numerator() — возвращает значение числителя;
numerator(number) — изменяет значение числителя и производит сокращение дроби, если это необходимо;
denominator() – возвращает значение знаменателя;
denominator(number) — изменяет значение знаменателя и производит сокращение дроби, если необходимо;
__str__ — возвращает строковое представление дроби в формате <числитель>/<знаменатель>;
__repr__ — возвращает описание объекта в формате Fraction(<числитель>, <знаменатель>)."""


class Fraction:

    def __init__(self, *other):
        if type(other[0]) is str:
            self.num = int(other[0].split('/')[0])
            self.denom = int(other[0].split('/')[1])
        else:
            self.num = other[0]
            self.denom = other[1]
        gcd = []
        for i in range(2, max(self.denom, self.num) // 2 + 1):
            if self.num % i == 0 and self.denom % i == 0:
                gcd.append(i)
        if len(gcd) != 0:
            self.num //= max(gcd)
            self.denom //= max(gcd)

    def numerator(self, *number):
        if len(number) != 0:
            self.num = number[0]
            gcd = []
            for i in range(2, max(self.denom, self.num) // 2 + 1):
                if self.num % i == 0 and self.denom % i == 0:
                    gcd.append(i)
            if len(gcd) != 0:
                self.num //= max(gcd)
                self.denom //= max(gcd)
        return self.num

    def denominator(self, *number):
        if len(number) != 0:
            self.denom = number[0]
            gcd = []
            for i in range(2, max(self.denom, self.num) // 2 + 1):
                if self.num % i == 0 and self.denom % i == 0:
                    gcd.append(i)
            if len(gcd) != 0:
                self.num //= max(gcd)
                self.denom //= max(gcd)
        return self.denom

    def __str__(self):
        return f'{self.num}/{self.denom}'

    def __repr__(self):
        return f'Fraction({self.num}, {self.denom})'




fraction = Fraction(3, 210)
print(fraction, repr(fraction))
fraction.numerator(10)
print(fraction.numerator(), fraction.denominator())
fraction.denominator(2)
print(fraction.numerator(), fraction.denominator())

