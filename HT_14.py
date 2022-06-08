# Hometask_14_1
# Создать класс Dog.
# Класс имеет четыре атрибута: height, weight, name, age. Класс имеет три метода: jump, run, bark.
# Каждый метод выводит сообщение на экран. Создать объект класса Dog, вызвать все методы
# объекта и вывести на экран все его атрибуты.
# Hometask_14_2
# Добавить в класс Dog метод change_name. Метод принимает на вход новое имя и меняет атрибут имени у
# объекта. Создать один объект класса. Вывести имя.Вызвать метод change_name. Вывести имя

class Dog:

    def __init__(self, height, weight, name, age):
        self.height = height
        self.weight = weight
        self.name = name
        self.age = age

    def jump(self, m):
        return f'Собака {self.name} прыгает на высоту {m} метров'

    def run(self, km_h):
        return f'Собака {self.name} бегает со скоростью {km_h} километров в час'

    def bark(self, db):
        return f'Собака {self.name} лает с громкостью {db} децибел'

    def change_name(self, name):
        self.name = name


labrador = Dog(1, 10, 'Jack', 4)

print(labrador.jump(1.5))
print(labrador.run(25))
print(labrador.bark(90))
labrador.change_name('Rick')
print(labrador.__dict__)
