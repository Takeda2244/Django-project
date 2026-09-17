import os
import json
import requests

# Получение данных из ссылка и обработка ошибок 
def get_data(url = "https://jsonplaceholder.typicode.com/posts", id = 1, timeout=5):
    query_params = {"userId": id}
    try:
        data = requests.get(url, params=query_params, timeout=timeout)

        data.raise_for_status()

        return data.json()
    except requests.exceptions.RequestException as error:
        print(f"Ошибка в сети: {error}")
        return None

# Сохранение данных в data\
def save_data(data, folder="data", filename="data_info.json"):
    if not os.path.exists(folder):
        os.makedirs(folder)

    path = os.path.join(folder, filename)
    
    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    print(f"Данные сохранены в файл: {path}")

# Формирование статистики
def make_stat(info):
    if not info:
        print("Нет данных")
        return

    data_info = len(info)
    
    # Считаем среднюю длину заголовков (title) в символах
    title_length = sum(len(post.get("title", "")) for post in info)
    if ((title_length / data_info) > 0):
        avg_title_length = title_length / data_info
    else:
        avg_title_length = 0

    print("\n Статистика по полученным данным: ")
    print(f"Всего постов загружено: {data_info}")
    print(f"Средняя длина заголовка поста: {avg_title_length:.1f} символов.")

# Запрос выполняется не при импорте модуля
if __name__ == "__main__":
    data = get_data()

    if (data) is not None:
        save_data(data)
        
        make_stat(data)