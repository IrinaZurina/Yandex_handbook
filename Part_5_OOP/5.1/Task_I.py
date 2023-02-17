"""В программировании существует потребность не только в изученных нами коллекциях. Одна из таких очередь.
Она реализует подход к хранению данных по принципу «Первый вошёл – первый ушел».
Реализуйте класс Queue, который не имеет параметров инициализации, но поддерживает методы:
push(item) — добавить элемент в конец очереди;
pop() — «вытащить» первый элемент из очереди;
is_empty() — проверят очередь на пустоту."""


class Queue:

    def __init__(self):
        self.waiting_list = []
        self.empty = True

    def push(self, item):
        self.waiting_list.append(item)
        return self.waiting_list

    def pop(self):
        item = self.waiting_list.pop(0)
        return item

    def is_empty(self):
        if len(self.waiting_list) == 0:
            self.empty = True
        else:
            self.empty = False
        return self.empty


queue = Queue()
for item in ("Hello,", "world!"):
    queue.push(item)
while not queue.is_empty():
    print(queue.pop())