# Функция для проверки правильности полученной строки
from student_tools import validate_student

# Первый тест: если строка полность корректна
def test_correct_row():
    row = ["Иван", "20", "ИП-132", "4.5"]
    assert validate_student(row) is True

# Второй тест: ошибка заключается в написании возраста буквами, а не цифрой
def test_letters_in_age():
    row = ["Иван", "двадцать", "ИП-132", "4.5"]
    assert validate_student(row) is False

# Третий тест: неправильная запись оценки вместо точки стоит запятая
def test_incorrect_grade_format():
    row = ["Иван", "20", "ИП-132", "4,5"]
    assert validate_student(row) is False

# Четвёртый тест: появилась лишняя пятая колонка когда правильно должно быть 4
def test_too_many_columns():
    row = ["Иван", "20", "ИП-132", "4.5", "Лишняя колонка"]
    assert validate_student(row) is False

# Пятый тест: колонок слишком мало
def test_empty_row():
    row = ["Иван"]
    assert validate_student(row) is False