from sp_network import sp_encode, sp_decode
from config import s_tables, p_tables
from plain_and_clip import plain_text, clip_text, text_to_hex
from read_and_write import file_read, save_result


def main():
    print("Привіт я програма, виберіть необхідний параметер\n"
          "Якщо вам потрібно зашифрувати текст введіть 1 та ентер\n"
          "Якщо потрібно розшифрувати текст введіть 2 та ентер")
    while True:
        print("Ви знаходитесь в початку програми")
        parameter = input()
        if parameter == "1":
            print("Програма може працювати і з текстовим файлом і з введеним текстом в консоль\n"
                  "Якщо ви хочете імпортувати текст введіть 1\n"
                  "Якщо хочете ввести текст вручну введіть 2")
            parameter1 = input()
            if parameter1 == "1":
                print(f'Щоб імпортувати текст файл повинен мати розширення .txt\n'
                      f'Введіть назву файлу з розширенням, наприклад "file.txt" (без лапок)')
                file_name = input()
                try:
                    text = file_read(file_name)
                    print("Відкритий текст")
                    print(text)
                    print("Відкритий текст в шістнадцятковому вигляді")
                    print(text_to_hex(text))
                    clip = clip_text(text)
                    print("Закритий текст")
                    print(clip)
                    save_result(clip, 'enc')

                except FileNotFoundError:
                    print("Файл з такою назвою не знайдено\n"
                          "Перевірте правильність набору\n"
                          "Перевірте чи ви вказали розширення файлу\n"
                          "Перевірте чи1 знаходиться файл в тій же папці що і програма\n"
                          "Можливо ви вказали назву в лапках")
            elif parameter1 == "2":
                print("Можете починати вводити текст який хочети зашифрувати")
                text = input()
                print("Відкритий текст")
                print(text)
                print("Відкритий текст в шістнадцятковому вигляді")
                print(text_to_hex(text))
                clip = clip_text(text)
                print("Закритий текст")
                print(clip)
                save_result(clip, 'enc')

            else:
                print("Ви не вірно ввели параметр повертаюсь на початок")

        elif parameter == "2":
            print("Програма може працювати і з зашифрованим файлом і з введеним зашифрованим текстом в консоль\n"
                  "Якщо ви хочете імпортувати зашифрований текст введіть 1\n"
                  "Якщо хочете ввести зашифрований текст вручну введіть 2")
            parameter2 = input()

            if parameter2 == "1":
                print(f'Щоб імпортувати текст файл повинен мати розширення .txt\n'
                      f'Введіть назву файлу з розширенням, наприклад "file.txt" (без лапок)')
                file_name = input()
                try:
                    text = file_read(file_name)
                    print("Закритий текст")
                    print(text)
                    plain = plain_text(text)
                    print("Відкритий текст")
                    print(plain)
                    print("Відкритий текст в шістнадцятковому представленні")
                    print(text_to_hex(plain))
                    save_result(plain, 'dec')

                except FileNotFoundError:
                    print("Файл з такою назвою не знайдено\n"
                          "Перевірте правильність набору\n"
                          "Перевірте чи ви вказали розширення файлу\n"
                          "Перевірте чи знаходиться файл в тій же папці що і програма\n"
                          "Можливо ви вказали назву в лапках")
                except UnicodeDecodeError:
                    print("Можливо зашифрований текст було пошкодженно, або формат введення невірний")
            elif parameter2 == "2":
                print("Можете починати вводити зашифровану послідовність шістнадцяткових чисел які хочете розшифрувати")
                clip = input()
                print("Закритий текст")
                print(clip)
                try:
                    plain = plain_text(clip)
                    print("Відкритий текст")
                    print(plain)
                    print("Відкритий текст в шістнадцятковому представленні")
                    print(text_to_hex(plain))
                    save_result(plain, 'dec')
                except ValueError:
                    print("Підчас декодування сталася помилка, можливо введена вами послідовність неправильна")
            else:
                print("Ви не вірно ввели параметр повертаюсь на початок")

        else:
            print("Я не розумію команди, введіть цифру 1 або 2")


def test():
    # test sp_network and test config
    bit = "1111011101010010"
    enc_bit = sp_encode(bit, s_tables, p_tables)
    print("encode ", sp_encode(bit, s_tables, p_tables))
    print("decode ", sp_decode(enc_bit, s_tables, p_tables))

    # test plain_and_clip
    text = "Privett world!"
    print(clip_text(text))
    print(plain_text(clip_text(text)))


if __name__ == '__main__':
    main()
    # test()
