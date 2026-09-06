# Визитка с описанием о создателе проекта

name = "Сергей"
group = "ИП-123"
interests = "Программирование, машины, игры"
age = 19

print(f"Привет меня зовут {name}, мне {age} лет, \n"
    f"я учусь в группе {group}, \n"
    f"мои интересы включают в себя: {interests} \n")

# Выполнение 3 задач : преобразование температуры, расчёт стоимости покупки со скидкой, нормализация имени.

print("Можно выполнить следующие операции: \n" \
"1. Преобразование температуры \n" \
"2. Расчёт стоимости покупки со скидкой \n" \
"3. Нормализация имени \n")

number = (int(input("Введите номер операции которой хотите выполнить: ")))

match number:

    # Задача преобразования температуры
    case 1: 
        cels_temperature = "цельсия"
        fahr_temperature = "фаренгейта"
        kelv_temperature = "кельвина"

        print("Выбрана операция преобразования температуры \n")

        temperature = int(input("Введите температуру для перевода: "))

        print("Выберите одну из следующих шкал температуры: \n " \
        "1. Цельсия \n " \
        "2. Кельвина \n " \
        "3. Фаренгейта \n ")

        scale_first = int(input("Введите цифру номера шкалы температуры из которой хотите перевести:  "))
        scale_second = int(input("Введите цифру номера шкалы температуры в которую хотите перевести:  "))

        if (scale_first <= 0 or scale_first >= 4 or scale_second <= 0 or scale_second >= 4 ): 
            print("Выберите правильную шкалу для перевода температуры")
        else:

            # Взаимодействие со шкалой Цельсия
            if (scale_first == 1 and scale_second == 1): print(f"{(temperature)} градусов {cels_temperature} равно {(temperature)} градусам {cels_temperature}")
            elif(scale_first == 1 and scale_second == 2): print(f"{(temperature)} градусов {cels_temperature} равно {temperature + 273,15} градусам {kelv_temperature}")
            elif(scale_first == 1 and scale_second == 3): print(f"{(temperature)} градусов {cels_temperature} равно {(temperature * 9/5) + 32} градусам {fahr_temperature}")

            # Взаимодействие со шкалой Кельвина
            elif (scale_first == 2 and scale_second == 2): print(f"{(temperature)} градусов {kelv_temperature} равно {(temperature)} градусам {kelv_temperature}")
            elif(scale_first == 2 and scale_second == 1): print(f"{(temperature)} градусов {kelv_temperature} равно {temperature - 273,15} градусам {cels_temperature}")
            elif(scale_first == 2 and scale_second == 3): print(f"{(temperature)} градусов {kelv_temperature} равно {(temperature - 273) * 9/5 + 32} градусам {fahr_temperature}")
            # Взаимодействие со шкалой Фаренгейта
            elif (scale_first == 3 and scale_second == 3): print(f"{(temperature)} градусов {fahr_temperature} равно {(temperature)} градусам {fahr_temperature}")
            elif(scale_first == 3 and scale_second == 1): print(f"{(temperature)} градусов {fahr_temperature} равно {(temperature -32) * 5/9} градусам {cels_temperature}")
            elif(scale_first == 3 and scale_second == 2): print(f"{(temperature)} градусов {fahr_temperature} равно {(temperature - 32) * 5/9 + 273,15} градусам {kelv_temperature}")

    # Задача расчёта стоимости покупки со скидкой
    case 2:
        price = int(input("Введите стоимость покупки: "))
        percent = int(input("Введите скидку в процентах: "))
        print(f"Стоимость покупки с учётом скидки {percent}% равна {price - (price * (percent / 100))}")

    # Задача нормализации имени
    case 3:
        name = input("Введите имя: ")
        name_temp = name.lower()
        correct_name = name_temp.capitalize()
        print(f"Нормализованное имя: {correct_name}")