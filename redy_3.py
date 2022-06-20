from abc import ABC, abstractmethod


# exam_1
def family_hide(last_name):
    """Принимает фамилию и показывать только первую заглавную букву.
# Остальные буквы заменяются звездочками"""
    return last_name.upper()[0] + '*' * (len(last_name) - 1)


print(family_hide(input()))
# exam_3


class Temperature(ABC):

    @abstractmethod
    def convert_degrees(self):
        pass


class KelvinScale(Temperature):
    def __init__(self, degree):
        self.degree = degree

    def convert_degrees(self):
        return f'{round(self.degree - 273.15, 2)} degrees Celsius'


class CelsiusScale(Temperature):
    def __init__(self, degree):
        self.degree = degree

    def convert_degrees(self):
        return f'{round(self.degree + 273.15, 2)} degrees Kelvin'


k_degrees = KelvinScale(303)
c_degrees = CelsiusScale(30)
degrees = [k_degrees, c_degrees]
for i in degrees:
    print(i.convert_degrees())
