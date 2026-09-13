import csv
from pathlib import Path
from classes import Student, Group

# Импорт студентов

group = Group("ИП-154")

# Проверка пяти сценариев

# Первый сценарий: чтение студентов из файла

path_csv = Path(__file__).parent.parent.parent / "students1.csv"

try:
    with path_csv.open("r", encoding="utf-8") as file_csv:
        reader = csv.reader(file_csv)
        next(reader) 
        for row in reader:
            if row:
                name = row[0]
                age = row[1]
                grades = row[3]
                
                new_student = Student(name, age, grades)
                group.add(new_student)

except FileNotFoundError as file_error:
    print(f"Не удалось найти файл {file_error}")

# Второй сценарий: добавление оценки
if group.students:
    test_student = group.students[0]
    print(f"Студент: {test_student.name}. Оценки до: {test_student.grades}")
    test_student.add_grade(5)
    print(f"Оценки после добавления: {test_student.grades} (Новый средний балл: {test_student.average()})")

# Третий сценарий: поиск студента
    name = "Михаил" 
    founded = group.find(name)
    if founded:
        print(f"Студент {name} найден! Информация: {founded.to_dict()}")
    else:
        print(f"Студент с именем {name} не найден в группе.")

# Четвёртый сценарий: 5 лучших студентов
    students = group.top_students()
    for index, student in enumerate(students, 1):
        print(f"{index}. {student.name} — Средний балл: {student.average()}")

# Пятый сценарий: удаление студента
    if group.students:
        name= group.students[-1].name
        print(f"Количество студентов до удаления: {len(group.students)}")
        
        is_deleted = group.delete(name)
        print(f"Удаление студента '{name}': {is_deleted}")
        print(f"Количество студентов после удаления: {len(group.students)}")