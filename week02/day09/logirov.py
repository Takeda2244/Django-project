# Сделано иишкой так как я ничего не понял но разбирался
import os
import logging
from dotenv import load_dotenv

# --- 1. НАСТРОЙКА ЛОГИРОВАНИЯ ---
# Автоматически создаем папку logs, если её ещё нет на диске
os.makedirs("logs", exist_ok=True)

# Настраиваем конфигурацию: куда писать, какой формат, какой уровень
logging.basicConfig(
    level=logging.INFO,  # Пропускать логи уровня INFO и выше (WARNING, ERROR)
    format="%(asctime)s - [%(levelname)s] - %(message)s",
    handlers=[
        logging.FileHandler("logs/app.log", encoding="utf-8"), # Пишем в файл
        logging.StreamHandler()  # Дублируем вывод в консоль VS Code
    ]
)

# Выполняем пункт 2: INFO (запуск приложения)
logging.info("Приложение API успешно запущено.")


# --- 2. ЗАГРУЗКА КОНФИГУРАЦИИ ---
# Инструмент load_dotenv читает файл .env и подгружает переменные в систему
load_dotenv()

# Читаем конфигурационный параметр API_URL через переменную окружения
API_URL = os.getenv("API_URL")


# --- 3. ПРОВЕРКА И ЛОГИРОВАНИЕ ОПЕРАЦИЙ ---
if not API_URL:
    # Выполняем пункт 2: WARNING (пропуск важных данных)
    logging.warning("Пропуск данных: конфигурационный параметр API_URL не найден в .env!")
else:
    # Выполняем пункт 2: INFO (успешная операция)
    logging.info(f"Конфигурация успешно применена. API_URL равен: {API_URL}")


# --- 4. ПРИМЕР ДЛЯ ИМИТАЦИИ ОШИБКИ (ERROR) ---
# Покажем, как логгер фиксирует критические сбои (Выполняем пункт 2: ERROR)
try:
    logging.info("Попытка сымитировать запрос к API...")
    # Намеренно создаем ошибку (деление на ноль), как будто сломалась сеть или база данных
    broken_request = 10 / 0
except Exception as error:
    # Записываем ошибку в лог-файл
    logging.error(f"Ошибка при работе с API: {error}")