from minimising import *


def main():
    while True:
        input_string = input("Введите логическую функцию:")
        if not is_logical_formula(input_string):
            print("Ошибка: введена некорректная логическая формула.")
        else:
            table, field_names, truth_values = truth_table(input_string)
            break

    print(f'Таблица истинности для функции {input_string}:\n'
          f'{table}\n\n')

    print('Расчётный метод:\n')

    sknf = create_sknf(table, field_names)
    sknf_str = format_str(sknf, 0)
    print(f'Совершенная конъюнктивная нормальная форма (СКНФ):\n'
          f'{sknf_str}')
    merged_sknf = merging(sknf)
    merged_sknf_str = format_str(merged_sknf, 0)
    print(f'Минимизация СКНФ:\n'
          f'{merged_sknf_str}\n')

    sdnf = create_sdnf(table, field_names)
    sdnf_str = format_str(sdnf, 1)
    print(f'Совершенная дизъюнктивная нормальная форма (СДНФ):\n'
          f'{sdnf_str}')
    merged_sdnf = merging(sdnf)
    merged_sdnf_str = format_str(merged_sdnf, 1)
    print(f'Минимизация СДНФ:\n'
          f'{merged_sdnf_str}\n')

    print('Таблично-расчётный метод:')

    print('Таблица для СКНФ')
    sknf_table = build_table(sknf, merged_sknf)
    print(format_str(minimized_from_table(sknf_table), 0))
    print('Таблица для СДНФ')
    sdnf_table = build_table(sdnf, merged_sdnf)
    print(format_str(minimized_from_table(sdnf_table), 1))


    variables = extracting_variables(input_string)
    print("\n\nКарта Карно:\n")
    table = carno_cart(variables, truth_values)

    zero_groups = find_groups(variables, truth_values, 'SKNF')
    sknf_expression = minimize(variables, zero_groups, 'SKNF')
    print("\nМинимизированная СКНФ:")
    print(sknf_expression)

    one_groups = find_groups(variables, truth_values, 'SDNF')
    sdnf_expression = minimize(variables, one_groups, 'SDNF')
    print("\nМинимизированная СДНФ:")
    print(sdnf_expression)


if __name__ == '__main__':
    main()
