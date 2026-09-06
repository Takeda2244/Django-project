# CLI-калькулятор
def calculate():
    print("Это CLI-калькулятор \nДля того чтобы выйти из калькулятора введите 'exit'")
    while True:
        num1 = input("Введите первое число: ").strip()

        if num1 == "exit":
            print("Программа завершена")
            break

        operator = input("Введите оператор вычисления (+, -, *, /): ").strip()
        num2 = input("Введите второе число: ").strip()

        # Числа приводятся к типу данных с плавающей точкой
        try:
            num1 = float(num1)
            num2 = float(num2)

        # Выбор операции
            if operator == "+":
                result = num1 + num2
            elif operator == "-":
                result = num1 + num2
            elif operator == "*":
                result = num1 * num2
            elif operator == "/":
                result = num1 / num2
            else: 
                print("Неверный знак выполняемой операции")
                continue

        # Вывод результата

            print(f"{num1} {operator} {num2} = {result}")

        # Исключения
        except ValueError:
            print("Неправильный формат вводимых данных")
        except ZeroDivisionError:
            print("На ноль делить нельзя")

# Функция вывода простых чисел от 1 до 200
def is_prime(n):
    if n < 2:
        # Числа меньше двух не являются простыми
        return False

    # Проверка простое ли число
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            # Если делителей больше чем два то число не является простым
            return False

    # Если делителей два то число просто и мы его выводим
    return True

def validate_age(value):
    if (value < 0): print("Возраст не может быть меньше 0")
    elif(value > 120): print("Возраст не может быть больше 120")

print("Можно выполнить следующие операции: \n" \
"1. Вызов CLI-калькулятора \n" \
"2. Вывод простых чисел от 1 до 200 \n" \
"3. Функция валидации возраста \n")

try:

    number = (int(input("Введите номер операции которой хотите выполнить: ")))

    match number:
            case 1:
                # Функция вызов CLI-калькулятора
                calculate()
            case 2:
                # Функция вызова простых чисел от 1 до 200
                n = int(input("\nВведите любое число: "))
                for num in range(1, 201):
                    if is_prime(num):
                        print(num)
            case 3:
                # Функция валидации возраста
                value = int(input("Введите возраст: "))
                validate_age(value)
            case _:
                print("Операции с данным номером не существует")

except ValueError:
    print("Неправильный формат вводимых данных")