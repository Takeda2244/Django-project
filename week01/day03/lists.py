# Создание списка из 15 студентов: имя, возраст, группа, оценки
def make_students():
    import random

    # Имена студентов
    names = [
        "Наталья", "Иван", "Алекс", "Ольга", "Дмитрий", 
        "Елена", "Артем", "Мария", "Дмитрий", "Анна", 
        "Михаил", "Татьяна", "Егор", "София", "Никита"
    ]

    # Группы студентов
    groups = ["ИП-123", "ИП-124", "ИП-125"]

    # Создание списка из 15 студентов
    students = [
        {
            "name": names[i],
            "age": random.randint(14, 17),
            "group": random.choice(groups),
            "grade": round(random.uniform(3.5, 5.0), 1)
        }
        for i in range(15)
    ]

    # Вывод списка студентов
    print("Список студентов: \n")
    print(f"{'Студент':<12} | {'Возраст':<7} | {'Группа':<8} | {'Оценка'}")
    print("-" * 45)

    for student in students:
        print(f"{student['name']:<12} | {student['age']:<7} | {student['group']:<8} | {student['grade']}")

    return students

# Реализация заданий по списку
def result_students(students_list):
    print("Текстовый отчёт: ")

    # Вывод среднего балла
    average_grade = 0
    for student in students_list:
        average_grade += student["grade"]
    print(f"\nСредний балл равен: {average_grade / len(students_list):.1f}")

    # Вывод топ 5 студентов
    print("\nСписок лучших пяти студентов: ")
    top_students = sorted(students_list, key=lambda x: x["grade"], reverse=True)[:5]

    for student in top_students:
        print(f"{student['name']:<12} | {student['age']:<7} | {student['group']:<8} | {student['grade']}")

    # Фильтрация по группе ИП-123
    print("\nФильтрация по группе ИП-123 ")
    for student in students_list:
        if student["group"] == "ИП-123":
            print(f"{student['name']:<12} | {student['age']:<7} | {student['group']:<8} | {student['grade']}")

    # Сортировка по возрасту 
    print("\nСортировка студентов по возрасту: ")
    age_students = sorted(students_list, key=lambda x: x["age"], reverse=True)
    
    for student in age_students:
        print(f"{student['name']:<12} | {student['age']:<7} | {student['group']:<8} | {student['grade']}")
    
    # Сортировка по среднему баллу (от высшего к низшему)
    print("\nСортировка по среднему баллу: ")
    top_students = sorted(students_list, key=lambda x: x["grade"], reverse=True)
        
    for student in top_students:
        print(f"{student['name']:<12} | {student['age']:<7} | {student['group']:<8} | {student['grade']}")

    # Поиск повторяющихся имен
    print("\nПовторяющиеся имена: ")
    all_names = [student["name"] for student in students_list]

    result_names = set()

    for name in all_names:
        if all_names.count(name) > 1 and name not in result_names:
            print(f"Имя {name} повторяется {all_names.count(name)} раз(а)")
            result_names.add(name)

    # Поиск множества уникальных имен
    print("\nУникальные группы студентов: ")

    groups = {student["group"] for student in students_list}

    print(", ".join(groups))

# Вызов функций
all_students = make_students()
result_students(all_students)

# Сохранение студентов в JSON и CSV

# Сохранение в формате JSON
import json

with open("students.json", "w", encoding="utf-8") as file:
    json.dump(all_students, file, ensure_ascii=False, indent=4)

# Сохранение в формате CSV  

import csv

with open("students.csv", "w", newline="", encoding="utf-8-sig") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "age", "group", "grade"])
    writer.writeheader()
    writer.writerows(all_students)

print("\nДанные успешны сохранены в формате JSON и CSV")