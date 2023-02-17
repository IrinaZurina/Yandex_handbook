"""Ещё одной полезной коллекцией является стек реализующий принцип «Последний пришёл – первый ушёл». Его часто
представляют как стопку карт или магазин пистолета, где приходящие элементы закрывают выход уже находящимся в коллекции.
Реализуйте класс Stack, который не имеет параметров инициализации, но поддерживает методы:
push(item) — добавить элемент в конец стека;
pop() — «вытащить» первый элемент из стека;
is_empty() — проверяет стек на пустоту"""


class Stack:

    def __init__(self):
        self.waiting_list = []
        self.empty = True

    def push(self, item):
        self.waiting_list.append(item)
        return self.waiting_list

    def pop(self):
        item = self.waiting_list.pop(-1)
        return item

    def is_empty(self):
        if len(self.waiting_list) == 0:
            self.empty = True
        else:
            self.empty = False
        return self.empty


stack = Stack()
for item in ("Hello,", "world!"):
    stack.push(item)
while not stack.is_empty():
    print(stack.pop())