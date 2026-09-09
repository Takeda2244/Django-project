# Функция для составления отчёта 
from student_tools import make_report

# Первый тест: никаких ошибок со строками небыло
def test_report_zero_errors():
    result = make_report(0)
    assert "Пропущено некорректных строк: 0" in result

# Второй тест: ошибок было 5
def test_report_five_errors():
    result = make_report(5)
    assert "Пропущено некорректных строк: 5" in result

# Третий тест: проверяем есть ли заголовок в отчёте
def test_report_header():
    result = make_report(0)
    assert result.startswith("Отчёт о корректности")

# Четвёртый тест: передаем 999 ошибок
def test_report_large_number():
    result = make_report(999)
    assert "999" in result

# Пятый тест: проверяем что отчёт возвращает строка, а не например число
def test_report_string():
    result = make_report(1)
    assert isinstance(result, str)