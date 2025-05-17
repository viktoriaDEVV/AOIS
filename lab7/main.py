from matrix import create_binary_matrix, get_word, get_column_address, print_matrix
from functions import *
from sum import sum_words
from search import g_l_search


def main():
    binary_matrix = create_binary_matrix()
    while True:
        print("""
            Меню:
            1. Показать таблицу
            2. Вывести слово
            3. Вывести адресный столбец
            4. Логические операции
            5. Сложение полей Aj и Bj
            6. Поиск по соответствию
            7. Выход
            """)

        choice = input("Выберите пункт меню: ")

        if choice == "1":

            print_matrix(binary_matrix)
        elif choice == "2":
            word_number = int(input("Номер слова: "))
            print(get_word(binary_matrix, word_number))
        elif choice == "3":
            try:
                column_index = int(input("Введите индекс столбца: "))
                print(get_column_address(binary_matrix, column_index))
            except ValueError:
                print("Пожалуйста, введите корректный номер столбца.")
        elif choice == "4":
            print("""
                        1. f0
                        2. f5
                        3. f10
                        4. f15
                        """)
            function_number = input("Выберите операцию: ")
            if function_number == '1':
                print(function0())
            elif function_number == '2':
                word_number = int(input("Номер слова: "))
                word = get_word(binary_matrix, word_number)
                print(function5(word))
            elif function_number == '3':
                word_number = int(input("Номер слова: "))
                word = get_word(binary_matrix, word_number)
                print(function10(word))
            elif function_number == '4':
                print(function15())
        elif choice == '5':
            key = input("Введите значение ключа (V= 000-111): ")
            before_sum, after_sum = sum_words(binary_matrix, key)
            for before, after in zip(before_sum, after_sum):
                print(f"Before: {before}, After: {after}")
        elif choice == '6':
            argument = input("Введите аргумент для поиска (16 бит): ")
            g_values, l_values, counts, words = g_l_search(binary_matrix, argument)
            print(f'Аргумент для поиска: {argument}')
            for i, word in enumerate(words):
                print(f'For word {word}:')
                print(f"g = {int(g_values[i])}, l = {int(l_values[i])}")
                print(f'Количество совпадений битов: {counts[i]}')
        elif choice == "7":
            print("Выход из программы.")
            break
        else:
            print("Некорректный выбор. Пожалуйста, попробуйте снова.")


if __name__ == "__main__":
    main()
