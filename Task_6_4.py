class Car:
    def __init__(self, car_speed, car_color, car_name, car_ispolice):
        self.speed = car_speed
        self.color = car_color
        self.name = car_name
        self.ispolice = car_ispolice

    def go(self):
        print('Машина начала движение')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        print('Машина повернула', direction)

    def show_speed(self):
        print('Текущая скорость автомобиля:', self.speed)


class TownCar(Car):
    print('Создана городская машина')

    def show_speed(self):
        print('Скорость:', self.speed)

        if self.speed > 60:
            print('Превышение скорости для класса TownCar.Скорость превышает 60!')


class SportCar(Car):
    print('Создана спортивная машина')


class WorkCar(Car):
    print('Создана рабочая машина')

    def show_speed(self):
        if self.speed > 40:
            print('Превышение скорости для класса WorkCar.Скорость превышает 40!')


class PoliceCar(Car):
    print('Создана полицейская машина')


town_car = TownCar(70, 'вишнеый', 'семерка', False)
work_car = WorkCar(30, 'серый', 'scania', False)
sport_car = SportCar(110, 'красный', 'ламборгини', False)
police_car = PoliceCar(80, 'белый', 'форд', True)
town_car.show_speed()
work_car.turn('налево')
sport_car.stop()
police_car.go()
print(town_car.speed)
print(work_car.name)
print(sport_car.color)
print(police_car.ispolice)