"""Напишите класс Programmer, который инициализируется именем и должностью (отработка у нового работника равна нулю).
Класс реализует следующие методы:
work(time) — отмечает новую отработку в количестве часов time;
rise() — повышает программиста;
info() — возвращает строку для бухгалтерии в формате: <имя> <количество отработанных часов>ч. <накопленная зарплата>тгр.
Junior — с окладом 10 тугриков в час;
Middle — с окладом 15 тугриков в час;
Senior — с окладом 20 тугриков в час по умолчанию и +1 тугрик за каждое новое повышение."""


class Programmer:

    def __init__(self, name: str, position: str):
        self.name = name
        self.position = position
        self.working_hours = 0
        self.count_rise = 0
        self.salary = 0

    def work(self, time):
        self.working_hours += time
        if self.position == 'Junior':
            self.salary += 10 * time
        elif self.position == 'Middle':
            self.salary += 15 * time
        else:
            self.salary += (20 + self.count_rise) * time
        return self.working_hours

    def rise(self):
        if self.position == 'Junior':
            self.position = 'Middle'
        elif self.position == 'Middle':
            self.position = 'Senior'
        elif self.position == 'Senior':
            self.count_rise += 1
        return self.position

    def info(self):
        return f'{self.name} {self.working_hours}ч. {self.salary}тгр.'


programmer = Programmer('Васильев Иван', 'Junior')
programmer.work(750)
print(programmer.info())
programmer.rise()
programmer.work(500)
print(programmer.info())
programmer.rise()
programmer.work(250)
print(programmer.info())
programmer.rise()
programmer.work(250)
print(programmer.info())