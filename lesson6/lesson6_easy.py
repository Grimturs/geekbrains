# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)

# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.


class Car:
    def __init__(self, name, color, speed, is_police):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go(self):
        print(f'Машина {self.name}, цвет {self.color} проехала со скоростью {self.speed}')

    def stop(self):
        print(f'Машина {self.name} остановилась')

    def turn(self):
        print(f'Машина {self.name} повернула направо')


class TownCar(Car):
    def turn(self):
        print(f'Машина {self.name} повернула налево')


class SportCar(Car):
    pass


class WorkCar(Car):
    def turn(self):
        print(f'Машина {self.name} повернула налево')


class PoliceCar(Car):
    def go(self):
        print(f'Полицейская машина {self.name}, цвет {self.color} отправилась в погоню за {sport_car01.name}')


police_car01 = PoliceCar('Subaro', 'Green', '150 km/h', True)
sport_car01 = SportCar('Mazda', 'Red', '200 km/h', False)

sport_car01.go()
sport_car01.turn()
police_car01.go()



