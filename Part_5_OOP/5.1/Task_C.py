"""Если написать предупреждение «Не нажимай красную кнопку!», то её сразу безумно хочется нажать.
Напишите класс RedButton, который описывает красную кнопку.
Класс должен реализовывать методы:
click() — эмулирует нажатие кнопки, выводит сообщение "Тревога!";
count() — возвращает количество раз, которое была нажата кнопка."""


class RedButton:

    def __init__(self, count=0):
        self.color = 'red'
        self.counter = count

    def click(self):
        self.counter += 1
        print('Тревога!')

    def count(self):
        return self.counter


first_button = RedButton()
second_button = RedButton()
for time in range(5):
    if time % 2 == 0:
        second_button.click()
    else:
        first_button.click()
print(first_button.count(), second_button.count())