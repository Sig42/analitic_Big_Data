# Task 1
# import time
#
#
# class TrafficLight:
#     __color = ['red', 'yellow', 'green']
#
#     def running(self):
#         while True:
#             print(TrafficLight.__color[0])
#             time.sleep(7)
#             print(TrafficLight.__color[1])
#             time.sleep(2)
#             print(TrafficLight.__color[2])
#             time.sleep(8)
#
#
# a = TrafficLight()
# a.running()

# Task 2
# class Road:
#     _length = 0
#     _width = 0
#
#     def __init__(self, length, width, mass, thickness):
#         self.thickness = thickness
#         self.mass = mass
#         self._length = length
#         self._width = width
#         print(length * width * mass * thickness)
#
#
# a = Road(200, 5, 20, 4)

# Task 3
# class Worker:
#
#     def __init__(self, name, surname, position, wage, bonus):
#         self.name = name
#         self.surname = surname
#         self.position = position
#         self._income = {'wage': wage, 'bonus': bonus}
#
#
# class Position(Worker):
#
#     def get_full_name(self):
#         return self.name+' '+self.surname
#
#     def get_total_income(self):
#         return self._income.get('wage')+self._income.get('bonus')
#
#
# a = Position('Joe', 'Smith', 'smith', 100, 200)
# print(a.get_full_name())
# print(a.get_total_income())

# Task 4
# class Car:
#
#     def __init__(self, name, color, speed, is_police=False):
#         self.speed = speed
#         self.color = color
#         self.name = name
#         self.is_police = is_police
#
#     def go_go_go(self):
#         print('Поехали!')
#
#     def stop(self):
#         print('Остановка!')
#
#     def turn_left(self):
#         print('Повернули налево!')
#
#     def turn_right(self):
#         print('Повернули налево!')
#
#     def show_speed(self):
#         print(self.speed)
#
#
# class TownCar(Car):
#
#     def show_speed(self):
#         if self.speed > 60:
#             print('Превышение скорости!')
#         else:
#             print(self.speed)
#
#
# class WorkCar(Car):
#
#     def show_speed(self):
#         if self.speed > 40:
#             print('Превышение скорости!')
#         else:
#             print(self.speed)
#
#
# class SportCar(Car):
#     pass
#
#
# class PoliceCar(Car):
#
#     def __init__(self, name, color, speed, is_police=True):
#         super().__init__(speed, color, name, is_police)
#
#
# a = PoliceCar('gbr', 'black', 150)
# print(a.is_police)
# a.turn_left()
# a.show_speed()
# b = WorkCar('ww', 'red', 100)
# b.show_speed()
# print(b.is_police)

# Task 5
# class Stationery:
#
#     def __init__(self, title):
#         self.title = title
#
#     def draw(self):
#         print('Запуск отрисовки')
#
#
# class Pen(Stationery):
#
#     def draw(self):
#         print('Рисуем ручкой!')
#
#
# class Pencil(Stationery):
#
#     def draw(self):
#         print('Рисуем карандашом!')
#
#
# class Handle(Stationery):
#
#     def draw(self):
#         print('Рисуем маркером!')
#
#
# a = Pen('p')
# a.draw()
# b = Handle('h')
# b.draw()
# c = Pencil('r')
# c.draw()
