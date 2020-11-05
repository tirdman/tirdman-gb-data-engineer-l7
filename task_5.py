"""
Задание 5.

Реализовать класс Stationery (канцелярская принадлежность).

Определить в нем публичный атрибут title (название) и публичный метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.”

Создать три дочерних класса: Pen (ручка), Pencil (карандаш), Handle (маркер).

В каждом из классов реализовать переопределение метода draw.

Для каждого из классов метод должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:

    def __init__(self, title):
        self.title = title

    @staticmethod
    def draw():
        print(f"Запуск отрисовки")


class Pen(Stationery):

    def draw(self):
        print(f"Запуск отрисовки в классе Pen с заголовком: {self.title}")


class Pencil(Stationery):

    def draw(self):
        print(f"Запуск отрисовки в классе Pencil с заголовком: {self.title}")


class Handle(Stationery):

    def draw(self):
        print(f"Запуск отрисовки в классе Handle с заголовком: {self.title}")


stationery_list = [Pen('Ручка'), Pencil('Карандаш'), Handle('Маркер')]

for next_stationery in stationery_list:
    next_stationery.draw()
