import random


# HT13_1
# Из полученного списка чисел создайте список с суммами
# этих чисел, отсортированными по возрастанию


# def list_sum_nums(list_nums):
#     ls_sum_nums = []
#     for i in list_nums:
#         sum_i = 0
#         while i != 0:
#             sum_i += i % 10
#             i = i // 10
#         ls_sum_nums.append(sum_i)
#
#     return sorted(ls_sum_nums)
#
#
# print(list_sum_nums([int(i) for i in input().split()]))

# HT13_2
# Напишите функцию f(x), которая возвращает значение следующей функции, определённой на всей числовой прямой


# def f(x):
#     if x <= -2:
#         return 1 - (x + 2)**2
#     elif -2 < x <= 2:
#         return -(x / 2)
#     elif 2 < x:
#         return (x - 2)**2 + 1
#
#
# print(f(float(input())))

# HT_13_3
# Напишите функцию, которая принимает на вход список целых чисел, удаляет из него
# все нечётные значения, а чётные нацело делит на два.


# def even_nums(list_nums):
#     return [i // 2 for i in list_nums if i % 2 == 0]
#
#
# print(even_nums([int(i) for i in input().split()]))

# HT_13_4
# Напишите функцию, которая создает список случайных элементов. На вход функция принимает кол-во элементов,
# минимальное и максимальное значение
# def rand_nums(count, min_num, max_nam):
#     ls_nums = [random.randint(min_num, max_nam) for i in range(count)]
#     return ls_nums
#
#
# a, b, c = map(int, input().split())
# print(rand_nums(a, b, c))

# HT_13_5
# Преобразуйте задачу с покупкой торта из экзамена 2 в функцию.
# cakes = {'наполеон': ['тесто сахар масло', 5, 1000],
#          'медовик': ['тесто мед сгущенка', 4, 950],
#          'киевский': ['тесто орехи безе', 7, 800]}
#
#
# def buy_cake(cake, request, count):
#     if request == 'описание':
#         print(f'Торт {cake} состоит из {cakes[cake][0]}')
#     elif request == 'цена':
#         print(f'Торт {cake} стоит {cakes[cake][1]} рублей')
#     elif request == 'количество':
#         print(f'Торт {cake} осталось {cakes[cake][2]} грамм')
#     print(f'Торта {cake} осталось {cakes[cake][2] - count} грамм')
#     return f'К оплате {cakes[cake][1] * count / 100} рублей'
#
#
# ck = input('Какой торт Вы хотели бы приобрести: ').lower()
# rst = input('Что Вы хотели бы уточнить: ').lower()
# cnt = int(input('Сколько торта Вам положить, гр.: '))
# print(buy_cake(ck, rst, cnt))

# HT_13_6
# Напишите функцию, вычисляющую значение факториала числа N. Используйте рекурсию
def factorial(n):
    if n == 0:
        return 1
    return factorial(n - 1) * n


print(factorial(int(input())))




