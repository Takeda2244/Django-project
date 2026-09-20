import sys

# Функция создания генератора чтения файла построчно

def read_file_str(file_name):
    with open(file_name, "r", encoding="utf-8") as file :
        for line in file:
            yield line.strip()

# Вызов функций

def valid_zapic(iterator):
        for line in iterator:
            if line and line.isalpha():
                yield line

file_name = "C:\\ProjectDjango\\Project\\week03\\day11\\text.txt"

# Создаем генератор и затем проверяем записи на валидность

generator_1 = read_file_str(file_name)

valid_generator_1 = valid_zapic(generator_1)

for index, row in enumerate(valid_generator_1):
    if index < 2:
        print(f"Валидная строка {index + 1}: {row}")
    else:
        break 

# Повторяем операцию

generator_2= read_file_str(file_name)
valid_generator_2 = valid_zapic(generator_2)

for index, row in enumerate(valid_generator_2):
    if index < 2:
        print(f"Валидная строка {index + 1}: {row}")
    else:
        break

# Тесты
print("\n")

# Сравнение сколько потребляет памяти

list_data = []
with open(file_name, "r", encoding="utf-8") as file:
    for line in file:
        clean = line.strip()
        if clean and clean.isalpha():
            list_data.append(clean)

total_list_memory = sys.getsizeof(list_data) + sum(sys.getsizeof(s) for s in list_data)
print(f"Обычный список (list) занимает: {total_list_memory} байт")

gen_raw = read_file_str(file_name)
gen_valid = valid_zapic(gen_raw)

total_gen_memory = sys.getsizeof(gen_valid)
print(f"Генератор (generator) занимает: {total_gen_memory} байт")

print(f"\nВывод: Генератор использует в {round(total_list_memory / total_gen_memory, 1)} раз(а) меньше памяти!")