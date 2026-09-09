def validate_student(row):
    """ 
    Проверяем полученную строку данных о студенте
    Если она правильная то возвращаем True, а если нет False
    """
    correct_columns = 4

    # Проверяем количество столбцов если 4 всё правильно если меньше или больше то нет
    if len(row) != correct_columns:
        return False

    try:
        # Так как только имя и группа текстовые проверяем будут ли они пустыми при удалении пробелов
        if not row[0].strip() or not row[2].strip():
            return False

        # Проверям корректность типов у возраста и оценки. Вылезет ValueError если типы сравнялись неправильно
        int(row[1].strip())
        float(row[3].strip())

        # Если всё правильно возвращаем истину
        return True

    # Если какая то ошибка высокчила то валидация провалилась
    except (ValueError, IndexError):
        return False