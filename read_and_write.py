def file_write(text, file_name):
    # Відкриваємо файл у режимі запису ('w' - write)
    with open(file_name, "w", encoding="utf-8") as file:
        # Записуємо текст у файл
        file.write(text)


def file_read(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        file_content = file.read()
    return file_content


def save_result(text, enc_dec):
    print("\nВи також можете записати результат в текстовий файл\n"
          "Щоб це зробити введіть 1 та натисніть ентер\n"
          "Якщо ви не бажаєте зберігати результат просто натисніть ентер")
    res = input()
    if res == "1":
        if enc_dec == 'enc':
            file_write(text, "clip_text.txt")
        else:
            file_write(text, "plain_text.txt")
    else:
        print("Зашифрований текст не буде збережено повертаюсь на початок програми")
