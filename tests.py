class Auto:
    model = 'Wish'
    auto_count = 0

    def __init__(self, year, model):
        print('Конструктор с инициализацие года выпуска авто')
        self.year = year
        self.model = model
        self._color = 'blue'
        self.__max_speed = 180

    def on_start(self):
        print('Go', self.year)
        auto_count = 1
        # Auto.auto_count = 10

    @staticmethod
    def _on_destroyed():
        print('Destroy')

    @staticmethod
    def stop():
        print('Stop Auto')

    def __add__(self, other):
        return self.year + other.year

    def __str__(self):
        return f'{self.model}_{self.year}'


a = Auto(2004, 'Wish')
b = Auto(2004, 'Nadya')

print(a + b)
print(a)
print(b)

a.on_start()
print(a.auto_count)

a.auto_count2 = 12
print(a.auto_count2)
print(Auto.auto_count)

# print(a._color)
a._on_destroyed()
print(a._Auto__max_speed)

# a.stop()
#
# a.on_start()
# print(Auto.auto_count)
# print(a.auto_count)
#
# a.on_start()
# print(Auto.auto_count)
# print(a.auto_count)
#
