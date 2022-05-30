# import pyttsx3


# exam_2_1

# a = input().split()
# for i in a:
#     if a.count(i) == 1:
#          print(i)

# exam_2_2
# var_1
# ls = input().split()
# s = set(ls)
#
# print(len(ls) - len(s))

# var_2
# ls = input().split()
# c = 0
#
# for i in range(len(ls)):
#     for j in range(i+1, len(ls)):
#         if ls[i] == ls[j]:
#             c += 1
# print(c)

# exam_2_3

# c_1 = (35, 78, 21, 37, 2, 98, 6, 100, 231)
# c_2 = (45, 21, 124, 76, 5, 23, 91, 234)
#
# if sum(c_1) > sum(c_2):
#     print(f'Сумма больше в кортеже{c_1}')
# elif sum(c_1) < sum(c_2):
#     print(f'Сумма больше в кортеже{c_2}')
#
# print(f'В кортеже с_1 минимальный элемент {c_1.index(min(c_1))}, максимальный элемент {c_1.index(max(c_1))}')
# print(f'В кортеже с_2 минимальный элемент {c_2.index(min(c_2))}, максимальный элемент {c_2.index(max(c_2))}')

# exam_2_4
# a = ' An apple a day keeps the doctor away'
# c = {i: a.count(i) for i in a}
# print(c)

# exam_2_5
# cakes = {'наполеон': ['тесто сахар масло', 5, 1000],
#          'медовик': ['тесто мед сгущенка', 4, 950],
#          'киевский': ['тесто орехи безе', 7, 800]}
# cake = input('Какой торт Вы хотели бы приобрести: ').lower()
# request = input('Что Вы хотели бы уточнить: ').lower()
#
# if request == 'описание':
#     print(f'Торт {cake} состоит из {cakes[cake][0]}')
# elif request == 'цена':
#     print(f'Торт {cake} стоит {cakes[cake][1]} рублей')
# elif request == 'количество':
#     print(f'Торт {cake} осталось {cakes[cake][2]} грамм')
#
#
# c = int(input('Сколько торта Вам положить, гр.: '))
#
# print(f'К оплате {cakes[cake][1] * c / 100} рублей')
# print(f'Торта {cake} осталось {cakes[cake][2] - c} грамм')

# exam_2_6
# a = [int(i) for i in input().split()]
# b = [int(i) for i in input().split()]
# print(len(set(a) & set(b)))

# exam_2_7
# cakes = {'наполеон': ['тесто сахар масло', 5, 1000],
#          'медовик': ['тесто мед сгущенка', 4, 950],
#          'киевский': ['тесто орехи безе', 7, 800]}
# try:
#     cake = input('Какой торт Вы хотели бы приобрести: ').lower()
#     request = input('Что Вы хотели бы уточнить: ').lower()
#
#     if request == 'описание':
#         print(f'Торт {cake} состоит из {cakes[cake][0]}')
#     elif request == 'цена':
#         print(f'Торт {cake} стоит {cakes[cake][1]} рублей')
#     elif request == 'количество':
#         print(f'Торт {cake} осталось {cakes[cake][2]} грамм')
#
#     c = int(input('Сколько торта Вам положить, гр.: '))
#
#     print(f'К оплате {cakes[cake][1] * c / 100} рублей')
#     print(f'Торта {cake} осталось {cakes[cake][2] - c} грамм')
#
# except KeyError:
#     print('Неверное название торта ')
# finally:
#     print('Заходите к нам еще ')

# exam_2_8
# sum_mark = 0
# c = 0
# with open('words.txt', 'r') as list_pupils:
#     for line in list_pupils:
#         line = line.rstrip()
#         mark = int(line[-1])
#         c += 1
#         sum_mark += mark
#         if mark < 3:
#             print(line)
#
# print(f'Средняя оценка за тест = {sum_mark / c}')

