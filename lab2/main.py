from truthTable import *


def main():
    while True:
        input_string = input("Введите логическую функцию:")
        if not is_logical_formula(input_string):
            print("Ошибка: введена некорректная логическая формула.")
            continue
    table, field_names = truth_table(input_string)

    print(f'Таблица истинности для функции {input_string}:\n'
          f'{table}\n')
    print(f'Совершенная конъюктивная нормальная форма (СКНФ):\n'
          f'{create_sknf(table, field_names)}\n')
    print(f'Совершенная дизъюнктивная нормальная форма (СДНФ):\n'
          f'{create_sdnf(table, field_names)}\n')
    print(f'Числовая форма СКНФ:\n'
          f'{digital_form_sknf(table)}\n')
    print(f'Числовая форма СДНФ:\n'
          f'{digital_form_sdnf(table)}\n')
    digital_result, index_result = index_form(table)
    print(f'Индексная форма:\n'
          f'{digital_result} - {index_result}\n')


if __name__ == '__main__':
    main()
