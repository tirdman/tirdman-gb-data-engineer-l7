"""
Задание 4.

Реализуйте базовый класс Car. У данного класса должны быть следующие публичные атрибуты:
speed, color, name, is_police (булево).

А также публичные методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).

Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.

Добавьте в базовый класс публичный метод show_speed,
который должен показывать текущую скорость автомобиля.

Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar)
и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self):
        return self.speed

    @staticmethod
    def go():
        return "Машина поехала"

    @staticmethod
    def stop():
        return "Машина остановилась"

    @staticmethod
    def turn(direction):
        return f"Машина повернула {direction}"


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            return f"{self.speed}. Автомобиль превышает скорость"
        return self.speed


class SportCar(Car):
    pass


class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            return f"{self.speed}. Автомобиль превышает скорость"
        return self.speed


class PoliceCar(Car):
    pass


# speed, color, name, is_police
town_car = TownCar(90, 'blue', 'Городской автомобиль', False)
sport_car = SportCar(90, 'red', 'Гоночный автомобиль', False)
work_car = WorkCar(90, 'white', 'Раюочий автомобиль', False)
police_car = PoliceCar(90, 'black', 'Полицейский автомобиль', True)

cars_list = [town_car, sport_car, work_car, police_car]

for next_car in cars_list:
    print(
        f"{next_car.name}. "
        f"Цвет: {next_car.color}. "
        f"Скорость: {next_car.speed}. "
        f"Полицейская: {'Да' if next_car.is_police else 'Нет'}. "
        f"Скорость: {next_car.show_speed()}")
