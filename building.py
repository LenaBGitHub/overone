class Building:
    def __init__(self, floor, windows, doors):
        self.floor = floor
        self.windows = windows
        self.doors = doors

    def build(self):
        return f'The house was built'

    def populate(self):
        return f'The house was populated'

    def demolish(self):
        return f'The house was demolished'


class PrivateHouse(Building):
    def __init__(self, floor, windows, doors, rooms):
        super().__init__(floor, windows, doors)
        self.rooms = rooms


class BusinessCenter(Building):
    def __init__(self, floor, windows, doors):
        super().__init__(floor, windows, doors)
        self.floor = [None] * floor

    def build(self):
        print(f'The Business Center was built')

    def __setitem__(self, floor_number, company_name):
        self.floor[floor_number] = company_name

    def __getitem__(self, floor_number):
        return self.floor[floor_number]


class MultistoryHouse(Building):

    def __init__(self, floor, windows, doors, count_of_flat):
        super().__init__(floor, windows, doors)
        self.count_of_flat = count_of_flat
        self.occupied = 0

    def populate(self, flats_to_occupied=0):
        if self.occupied + flats_to_occupied <= self.count_of_flat:
            self.occupied += flats_to_occupied
        else:
            raise ValueError("Столько свободных квартир нет")

    def empty_flats(self):
        return f'Осталось {self.count_of_flat - self.occupied} свободных квартир'


class BeautySalonMixin:
    """Маникюр стоит на 20% больше мин цены
Стрижка зависит от длины волос: меньше 30см - +20%, От 30 до 50 см - +50% Свыше 50 см - +80%"""
    min_price = 35

    def __init__(self):
        self.close_time = None
        self.open_time = None

    def salon_opening_hours(self, time):
        if self.close_time > time > self.open_time:
            return f'The salon is opened at {time}'
        else:
            return f'The salon is closed at {time}'

    def manicure(self):
        return f'Manicure costs {self.min_price * 1.2}'

    def haircut(self, length):
        if length <= 30:
            return f'Haircut costs {self.min_price * 1.2}'
        elif 30 < length <= 50:
            return f'Haircut costs {self.min_price * 1.5}'
        if length < 50:
            return f'Haircut costs {self.min_price * 1.8}'


class HouseWithBeautySalon(Building, BeautySalonMixin):
    def __init__(self, floor, windows, doors):
        super(HouseWithBeautySalon, self).__init__(floor, windows, doors)

    def set_timework(self, salon_opening_hours, salon_closing_hours):
        self.open_time = salon_opening_hours
        self.close_time = salon_closing_hours


if __name__ == "__main__":
    ph = PrivateHouse(2, 12, 7, 6)
    print(ph.build())
    print(ph.populate())
if __name__ == "__main__":
    mh = MultistoryHouse(10, 50, 20, 10)
    mh.populate(5)
    print(mh.empty_flats())
if __name__ == "__main__":
    hbs = HouseWithBeautySalon(5, 10, 5)
    hbs.set_timework(10, 22)
    print(hbs.salon_opening_hours(13))
    print(hbs.salon_opening_hours(23))
    print(hbs.open_time)
    print(hbs.haircut(25))
    print(hbs.manicure())
if __name__ == '__main__':
    building1 = BusinessCenter(4, 20, 20)
    building1.build()
    building1[0] = 'Arabian Coffee'
    building1[1] = 'Overone'
    print(building1[1])
