"""
Задание 1.

Создать класс TrafficLight (светофор)
и определить у него один приватный атрибут color (цвет) и публичный метод running (запуск).

В рамках метода running реализовать переключение светофора в режимы:
красный, желтый, зеленый. Продолжительность первого состояния (красный)
составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
на ваше усмотрение.
Для имитации "горения" каждого цвета испольщуйте ф-цию sleep модуля time

Переключение между режимами должно осуществляться только
в указанном порядке (красный, желтый, зеленый).

Проверить работу примера, создав экземпляр и вызвав описанный метод.
"""

from time import sleep


class TrafficLight:
    __color = [{'color': 'Красный', 'duration': 7}, {'color': 'Желтый', 'duration': 2},
               {'color': 'Зеленый', 'duration': 10}]

    @staticmethod
    def running():
        for i in range(0, len(TrafficLight.__color)):
            print(TrafficLight.__color[i]['color'])
            sleep(TrafficLight.__color[i]['duration'])


traffic_light = TrafficLight()
traffic_light.running()
