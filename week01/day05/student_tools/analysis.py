def make_report(incorrect_rows_count):
    """ Составляет отчёт на основе полученных данных """
    report_text = "Отчёт о корректности полученных данных:\n"
    report_text += f"Пропущено некорректных строк: {incorrect_rows_count}"
    return report_text