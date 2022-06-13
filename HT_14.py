# Hometask_14_1
# Создать класс Dog.
# Класс имеет четыре атрибута: height, weight, name, age. Класс имеет три метода: jump, run, bark.
# Каждый метод выводит сообщение на экран. Создать объект класса Dog, вызвать все методы
# объекта и вывести на экран все его атрибуты.
# Hometask_14_2
# Добавить в класс Dog метод change_name. Метод принимает на вход новое имя и меняет атрибут имени у
# объекта. Создать один объект класса. Вывести имя. Вызвать метод change_name. Вывести имя
# Hometask_14_6
# Создать родительский класс Pet, содержащий все общие методы классов Dog, Cat, Parrot. Унаследовать Dog,
# Cat, Parrot от класса Pet. Удалить в дочерних классах те методы, которые имеются у родительского класса.
# Создать объект каждого класса и вызвать все его методы

class Pet:

    def __init__(self, master, name, age):
        self.master = master
        self.name = name
        self.age = age

    def run(self, km_h):
        return f'Питомец {self.name} бегает со скоростью {km_h} километров в час'

    def jump(self, m):
        return f'Питомец {self.name} прыгает на высоту {m} метров'

    def birthday(self):
        return f'Питомцу {self.name} сегодня {self.age + 1} лет'

    def sleep(self, h):
        return f'Питомец {self.name} спит {h} часов в день'


class Dog(Pet):
    def __init__(self, master, name, age):
        super().__init__(master, name, age)

    def bark(self, db):
        return f'Собака {self.name} лает с громкостью {db} децибел'

    def change_name(self, name):
        self.name = name


class Cat(Pet):
    def __init__(self, master, name, age):
        super().__init__(master, name, age)

    def meow(self, db):
        return f'Кот {self.name} мяукает с громкостью {db} децибел'


class Parrot(Pet):
    def __init__(self, master, name, age):
        super().__init__(master, name, age)

    def fly(self, km_h):
        return f'Попугай {self.name} летает со скоростью {km_h} километров в час'


if __name__ == "__main__":
    labrador = Dog("Mike", 'Jack', 4)
    print(labrador.jump(1.5))
    print(labrador.run(25))
    print(labrador.bark(90))
    print(labrador.sleep(6))
    print(labrador.birthday())
    labrador.change_name('Rick')

    pers = Cat("July", 'Simba', 2)
    print(pers.jump(0.5))
    print(pers.run(15))
    print(pers.meow(50))
    print(pers.sleep(16))
    print(pers.birthday())

    ara = Parrot("Katy", "Kesha", 1)
    print(ara.jump(0.2))
    print(ara.run(5))
    print(ara.fly(20))
    print(ara.sleep(8))
    print(ara.birthday())
