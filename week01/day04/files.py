# Читаем оба формата и сравниваем количество записей

# Прочтение файла JSON и CSV и их сравнение

import csv
from pathlib import Path

# Путь для файла json и его чтение
try:
    print("Информация из json-файла:\n")
    path_json = Path("students.json")

    with path_json.open("r", encoding="utf-8") as file_json:
        info_json = file_json.read()
        print(info_json)
        
    # Путь для файла csv и его чтение
    
    print("\nИнформация из csv-файла:\n")
    path_csv = Path("students.csv")

    with path_csv.open("r", encoding="utf-8") as file_csv:
        info_csv = file_csv.read()
        print(info_csv)

except FileNotFoundError as file_error:
    print(f"Не удалось найти файл {file_error}")

# Реализация импорта студентов из csv с пропуском некорректных строк

path_csv_incorrect = Path("students.csv")

correct_students = []

incorrect_rows_count = 0

correct_columns = 4

print("Импортируем файл из CSV формата")

try:
    with path_csv_incorrect.open("r", encoding="utf-8", newline="") as file_csv:
        reader = csv.reader(file_csv)

        for line, row in enumerate(reader, start=1):
            try:
                if len(row) != correct_columns:
                    raise ValueError("Неверное количество колонок")

                name = row[0].strip()
                age = int(row[1].strip())
                group = row[2].strip()
                grade = float(row[3].strip())

                correct_students.append({
                    "name": name,
                    "age": age,
                    "group": group,
                    "grade": grade
                })

            except (ValueError, IndexError) as error:
                print(f"Строка {line} пропущена. Причина: {error}. Данные строки: {row}")
                incorrect_rows_count += 1

    print("\n--- Итоги импорта ---")
    print(f"Успешно импортировано студентов: {len(correct_students)}")
    print(f"Пропущено некорректных строк: {incorrect_rows_count}")

    print("Импортированные данные:")
    for student in correct_students:
        print(student)

except FileNotFoundError:
    print(f"Файл {path_csv_incorrect} не был найден")

# Создание и чтение файла отчёта со статистикой report.txt

print("\n")
with open("report.txt", "w", encoding="utf-8") as file_report:
    file_report.write("Отчёт о корректности выполнения операций:\n")
    file_report.write(f"Пропущено некорректных строк: {incorrect_rows_count}")

with open("report.txt", "r", encoding="utf-8") as file_report:
    info = file_report.read()
    print(info)