import pyttsx3


engine = pyttsx3.init()
engine.setProperty('rate', 270)
engine.setProperty('volume', 1)

cakes = {'наполеон': ['тесто сахар масло', 5, 1000],
         'медовик': ['тесто мед сгущёнка', 4, 950],
         'киевский': ['тесто орехи безе', 7, 800]}
nums = [0, 1, 2, 3, 4]
engine.say('Какой торт Вас интересует: ')
engine.runAndWait()
cake = input(f'Торт: ').lower()


try:
    while True:
        if cake in cakes:
            engine.say('Если интересует состав, введите 1, '
                       'если цена - введите 2, '
                       'если остаток - введите 3, '
                       'если оформить заказ - введите 4, '
                       'если выйти - введите 0')
            engine.runAndWait()
            while True:
                request = int(input('Введите запрос:\nСостав - 1, Цена - 2, Количество в наличии - 3, '
                                    'Оформить заказ - 4, Если хотите выйти - введите 0\n'))

                if request in nums:
                    if request == 0:
                        break
                    if request == 1:
                        engine.say(f'Торт {cake} состоит из {cakes[cake][0]}')
                        engine.runAndWait()
                        print(f'Торт {cake} состоит из {cakes[cake][0]}.')
                    elif request == 2:
                        engine.say(f'Торт {cake} стоит {cakes[cake][1]} рублей')
                        engine.runAndWait()
                        print(f'Торт {cake} стоит {cakes[cake][1]} рублей.')
                    elif request == 3:
                        engine.say(f'Торт {cake} осталось {cakes[cake][2]} грамм')
                        engine.runAndWait()
                        print(f'Торт {cake} осталось {cakes[cake][2]} грамм')
                    elif request == 4:
                        engine.say('Сколько торта Вам положить ')
                        engine.runAndWait()
                        c = input('Сколько торта Вам положить, гр: ')

                        while True:
                            if c.isdigit():
                                if int(c) > cakes[cake][2]:
                                    engine.say(f'Торта {cake} меньше, чем Вам нужно. Осталось {cakes[cake][2]} граммов')
                                    engine.runAndWait()
                                    print(f'Торта {cake} меньше, чем Вам нужно. Осталось {cakes[cake][2]} граммов')
                                    c = input('Сколько торта Вам положить, гр: ')
                                else:
                                    engine.say(f'У вас есть карта постоянного покупателя?')
                                    engine.runAndWait()

                                    while True:
                                        discount = int(input('У вас есть карта постоянного покупателя?\n'
                                                             'Если да, введите 1; если нет, введите 0\n'))
                                        if discount == 1 or discount == 0:
                                            if discount == 0:
                                                engine.say(f'К оплате {cakes[cake][1] * int(c) / 100} рублей')
                                                engine.runAndWait()
                                                print(f'К оплате {cakes[cake][1] * int(c) / 100} рублей')
                                                break
                                            elif discount == 1:
                                                engine.say(f'К оплате с учетом скидки 10% '
                                                           f'{cakes[cake][1] * int(c) / 100 * 0.9} рублей')
                                                engine.runAndWait()
                                                print(f'К оплате {cakes[cake][1] * int(c) / 100 * 0.9} рублей')
                                                break
                                        else:
                                            engine.say('Вы ввели неверный запрос, попробуйте снова')
                                            engine.runAndWait()
                                            print('Вы ввели неверный запрос, попробуйте снова ')
                                            discount = input('У вас есть карта постоянного покупателя?\n'
                                                             'Если да, введите 1; если нет, введите 0\n')
                                    break
                            print('Неверное значение')
                            c = input('Сколько торта Вам положить, гр: ')
                        break
                else:
                    engine.say('Вы ввели неверный запрос, попробуйте снова')
                    engine.runAndWait()
                    print('Вы ввели неверный запрос, попробуйте снова ')
            break
        else:
            engine.say('Неверное название торта ')
            engine.runAndWait()
            print('Неверное название торта. Есть Наполеон, Медовик и Киевский.')
            cake = input('Торт: ').lower()

except ValueError:
    engine.say('Ошибка. Попробуйте оформить заказ снова')
    engine.runAndWait()
    print('Ошибка. Попробуйте оформить заказ снова')
finally:
    engine.say('Заходите к нам еще')
    engine.runAndWait()
    print('Заходите к нам еще ')
