import os
import logging

os.makedirs("logs", exist_ok=True)

## Сделано с помощью нейросети так как не очень понятно задание

# Настройка конфигурации логирования
logging.basicConfig(
    level=logging.INFO,  # Минимальный уровень логирования
    format="%(asctime)s - [%(levelname)s] - %(message)s",
    handlers=[
        logging.FileHandler("logs/app.log", encoding="utf-8"),
        logging.StreamHandler()  # Чтобы логи дублировались в консоль
    ]
)

# Пример использования логгера в коде:
# logging.info("Приложение API успешно запущено.")
# logging.warning("Пропуск данных: в запросе отсутствует поле 'email'.")
# logging.error("Ошибка при подключении к базе данных: ...")

# Нужно установить библиотеку pip install python-dotenv

from dotenv import load_dotenv
import os

# Загружаем переменные из .env файла
load_dotenv()

# Получаем параметр API_URL
API_URL = os.getenv("API_URL")

if not API_URL:
    logging.warning("Переменная окружения API_URL не задана!")
else:
    logging.info(f"API успешно сконфигурировано. URL: {API_URL}")
