# length = float(input("Длина ребра куба= "))
# print("Объем куба= ", length ** 3)
#
# number_1 = float(input("Первое число= "))
# number_2 = float(input("Второе число= "))
# print(number_1 + number_2)
# print(number_1 - number_2)
# print(number_1 * number_2)
# print(number_1 / number_2)
# print(number_1 ** number_2)
# print(number_1 // number_2)
# print(number_1 % number_2)
#
# number_of_apples = int(input("Сколько яблок было у Анны? "))
# eaten_apples = int(input("Сколько яблок съел Пол? "))
# print("Осталось", number_of_apples - eaten_apples)
#
# speed_of_train_1 = 50
# speed_of_train_2 = 50
# speed_of_fly = 75
# distance = 200
# total_speed_of_trains = speed_of_train_1 + speed_of_train_2
# driving_time = distance / total_speed_of_trains
# distance_of_fly = speed_of_fly * driving_time
# print("Расстояние, которое пролетит муха", distance_of_fly, "км")

day = 1
snail_position = 0
while snail_position < 20:
    snail_position = snail_position + 2
    if snail_position == 20:
        print(day, "дней")
    else:
        snail_position = snail_position - 1
        day = day + 1

# Журавлики. Дано общее кол-во. Катя делает в 2 раза больше, чем Петя и Сергей вместе. Мальчики делают одинаковое количество.
# print(counts)
# ob = int(input('общее '))
# p = 0
# s = 0
# k = 0
# for j in range(ob):
#     while k + s + p < ob:
#         p += 1
#         s += 1
#         k = (p + s) * 2
# print(p, k, s)