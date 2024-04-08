def file_write(text, file_name):
    """Записує результат у файл"""
    # Відкриваємо файл у режимі запису ('w' - write)
    with open(file_name, "w", encoding="utf-8") as file:
        # Записуємо текст у файл
        file.write(text)


def file_read(file_name):
    """Читає дані записані у файлі"""
    with open(file_name, "r", encoding="utf-8") as file:
        file_content = file.read()
    return file_content


def save_result(text):
    """Зберігає результат шифрування дешифрування у файл"""
    print("\nВи також можете записати результат в текстовий файл\n"
          "Щоб це зробити введіть 1 та натисніть ентер\n"
          "Якщо ви не бажаєте зберігати результат просто натисніть ентер")
    res = input()
    if res == "1":
        print('Введіть під якою назвою потрібно зберегти результат\n'
              'Введіть назву файлу з розширенням, наприклад "file.txt" (без лапок)')
        in_text = input()
        if in_text == '':
            print("Ви не вказали назву файлу, повертаюсь на початок")
        elif in_text[:-5:-1] != "txt.":
            print("Ви не вказали розширення .txt, повертаюсь на початок")
        else:
            file_write(text, in_text)
    else:
        print("Зашифрований текст не буде збережено повертаюсь на початок програми")
