import time
from functools import wraps

# Декоратор измерения времени выполнения

def vipoln_timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"Функция {func.__name__} выполнилась за {end_time - start_time:.6f} сек.")
        return result
    return wrapper

# Декоратор логирования вызова функции

def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Вывзов {func.__name__} с аргументами: args = {args}, kwargs = {kwargs}")
        try:
            result = func(*args, **kwargs)
            print(f"{func.__name__} успешно завершилась.")
            return result
        except Exception as error:
            print(f"В {func.__name__} произошло исключение: {error}")
            raise
    return wrapper

# Контекстный менеджер timer

class timer:
    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        end = time.perf_counter()
        print(f"Время выполнения блока: {end - self.start:.6f} сек.")

        if exc_type is not None:
            print(f"Завершено с ошибкой: {exc_val}")
            return False
        return True

# Функции проверки декораторов
@logger
@vipoln_timer
# Фильтрация списка
def process_data_list(data_size):
    data = [x for x in range(data_size) if x % 2 == 0]
    time.sleep(0.5)
    return len(data)

@logger
# Проверка неккоректных данных
def calculate_metrics(average_value, total_count):
    return average_value / total_count

# Выполнение

if __name__ == "__main__":
    print("Первый тест: работа декораторов")
    result = process_data_list(100_000)
    print(f"Имя функции в коде: '{process_data_list.__name__}' (Проверка wraps)\n")

    print("Второй тест: контекстный менеджер")
    with timer():
        print("Загружаем сырые данные...")
        time.sleep(0.3)
        print("Данные загружены.")
    print()

    print("Третий тест: контекстный менеджер и декоратор при ошибке")
    try:
        with timer():
            print("Пытаемся рассчитать метрики с нулевым количеством...")
            calculate_metrics(45.5, 0)
    except ZeroDivisionError:
        print("\n[Главный поток] Исключение ZeroDivisionError успешно поймано в основном коде.")