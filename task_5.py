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
    title = None

    @staticmethod
    def draw():
        print(f"Запуск отрисовки")


class Pen:

    @staticmethod
    def draw():
        print(f"Запуск отрисовки в классе Pen")


class Pencil:

    @staticmethod
    def draw():
        print(f"Запуск отрисовки в классе Pencil")


class Handle:

    @staticmethod
    def draw():
        print(f"Запуск отрисовки в классе Handle")


stationery_list = [Pen(), Pencil(), Handle()]

for next_stationery in stationery_list:
    next_stationery.draw()
