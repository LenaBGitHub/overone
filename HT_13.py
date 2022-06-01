# HT13_1
# Из полученного списка чисел создайте список с суммами
# этих чисел, отсортированными по возрастанию


def list_sum_nums(list_nums):
    ls_sum_nums = []
    for i in list_nums:
        sum_i = 0
        while i != 0:
            sum_i += i % 10
            i = i // 10
        ls_sum_nums.append(sum_i)

    return sorted(ls_sum_nums)


print(list_sum_nums([int(i) for i in input().split()]))

# HT13_2
# Напишите функцию f(x), которая возвращает значение следующей функции, определённой на всей числовой прямой


def f(x):
    if x <= -2:
        return 1 - (x + 2)**2
    elif -2 < x <= 2:
        return -(x / 2)
    elif 2 < x:
        return (x - 2)**2 + 1


print(f(float(input())))

# HT_13_3
# Напишите функцию, которая принимает на вход список целых чисел, удаляет из него
# все нечётные значения, а чётные нацело делит на два.


def even_nums(list_nums):
    return [i // 2 for i in list_nums if i % 2 == 0]


print(even_nums([int(i) for i in input().split()]))
