# Создание бд

import sqlite3

name = "students.db"

def make_db():
    return sqlite3.connect(name)

# Создание таблицы students

def make_table():
    with make_db() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER NOT NULL,
                group_name TEXT NOT NULL
            )
        """)
        conn.commit()

# Создание CRUD-функций 

# Create функция

# Создание студента
def create_student(name: str, age: int, group_name: str) -> int:
    with make_db() as conn:
        cursor = conn.cursor()
        # Как я понял параметризация защищает от SQL-инъекций тоесть знак ?
        cursor.execute(
            "INSERT INTO students (name, age, group_name) VALUES (?, ?, ?)", 
             (name, age, group_name)
        )
        conn.commit()
        # Вернули айди добавленного студента
        return cursor.lastrowid

# Read функция

# Чтение всех студентов
def read_students() -> list:
    with make_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students")
        return cursor.fetchall()

# Чтение одного студента по id
def read_one_student(student_id: int) -> tuple:
    with make_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,))
        return cursor.fetchone()

# Update функция

# Обновление у студента возраста
def update_student_age(student_id: int, age: int) -> bool:
    with make_db() as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE students SET age = ? WHERE id = ?", (age, student_id))
        conn.commit()
        # Проверка выполнено ли обновление данных успешно
        return cursor.rowcount > 0

# Delete функция

# Удалим студента по id

def delete_student(student_id: int) -> bool:
    with make_db() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM students WHERE id = ?", (student_id, ))
        conn.commit()
        # Проверка выполнено ли удаление данных успешно
        return cursor.rowcount > 0

# Поиск по имени 

def found_student(name: str) -> bool:
    with make_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students WHERE name = ?", (name,))
        # Проверка был ли найден студент с таким именем
        result = cursor.fetchone()
        return result is not None

# Фильтр по группе

def found_students_group(group_name: str) -> list:
    with make_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students WHERE group_name = ?", (group_name,))
        # Проверка найдена ли такая группа
        return cursor.fetchall()

# Реализация 6 тестов

if __name__ == "__main__":
    make_table()

# Первый тест на создание студентов

print("\nТест 1: Добавление студентов")
id_ivan = create_student("Иван", 20, "ИП-201")
id_anna = create_student("Анна", 19, "ИП-201")
id_petr = create_student("Петр", 21, "ИП-302")
print(f"Добавлены студенты. ID Ивана: {id_ivan}, ID Анны: {id_anna}, ID Петра: {id_petr}")

# Второй тест чтение таблицы 

print("\nТест 2: Чтение всех студентов")
all_students = read_students()
print(f"Всего студентов в базе: {len(all_students)}")
for student in all_students:
    print(f" Студент: ID={student[0]}, Имя={student[1]}, Возраст={student[2]}, Группа={student[3]}")

# Третий тест чтение одного студента

print("\nТест 3: Чтение одного студента по ID")
student_info = read_one_student(id_anna)
print(f"Данные Анны из базы: {student_info}")

# Четвертый тест изменение возраста

print("\nТест 4: Обновление возраста")
print(f"Возраст Ивана до обновления: {read_one_student(id_ivan)[2]}")
was_updated = update_student_age(id_ivan, 22)
if was_updated:
    print(f"Возраст Ивана обновлен. Теперь ему: {read_one_student(id_ivan)[2]}")
else:
    print("Не удалось обновить данные")

# Пятый тест выполнение функций поиска и фильтрации

print("\nТест 5: Поиск и фильтрация данных")

print(f"Есть ли в базе Иван? -> {found_student('Иван')}")
print(f"Есть ли в базе Олег? -> {found_student('Олег')}")

group = found_students_group("ИП-201")
print(f"Студенты группы ИП-201: {group}")

# Шестой тест удаление студента по ID

print("\nТест 6: Удаление студента по ID")
print(f"Количество студентов до удаления: {len(read_students())}")
was_deleted = delete_student(id_petr)
if was_deleted:
    print(f"Студент Петр (ID {id_petr}) удален.")
    print(f"Количество студентов после удаления: {len(read_students())}")
else:
    print("Не удалось удалить студента")