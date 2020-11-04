"""
Задание 2.

Реализовать класс Road (дорога), в котором определить защищенные атрибуты:
length (длина в метрах), width (ширина в метрах).

Значения данных атрибутов должны передаваться при создании экземпляра класса.

Реализовать публичный метод расчета массы асфальта, необходимого для покрытия
всего дорожного полотна.

Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв
метра дороги асфальтом, толщиной в 1 см * число м толщины полотна.
Массу и толщину сделать публичными атрибутами.
Проверить работу метода.

Например: 20м*5000м*25кг*0.05м = 125000 кг = 125 т
"""


class Road:
    weight_square_meter = None
    thickness = None

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc_weight(self):
        if not self.weight_square_meter or not self.thickness:
            print("Перед расчетом массы асфальта укажите массу асфальта на 0,01 метр и толщину дороги")
            return
        return self._length * self._width * self.weight_square_meter * self.thickness


road = Road(5000, 20)
road.calc_weight()

road.weight_square_meter = 25
road.thickness = 0.05
print(road.calc_weight())
