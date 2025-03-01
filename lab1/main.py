from run import (decimal_integer_to_direct, decimal_to_reverse, decimal_to_additional, summa, from_binary_to_decimal,
                 multiplication, binary_division, floating_point_representation,add_floating_numbers,
                 floating_point_to_decimal, additional_to_reverse)


def main():
    data1 = int(input('Введите число: '))
    direct_res1 = decimal_integer_to_direct(data1)
    reverse_res1 = decimal_to_reverse(direct_res1)
    additional_res1 = decimal_to_additional(reverse_res1)
    print(
        f'Введено число: {data1}\n'
        f'Прямой код: {direct_res1}\n'
        f'Обратный код: {reverse_res1}\n'
        f'Дополнительный код: {additional_res1}\n'
    )

    data2 = int(input('Введите число: '))
    direct_res2 = decimal_integer_to_direct(data2)
    reverse_res2 = decimal_to_reverse(direct_res2)
    additional_res2 = decimal_to_additional(reverse_res2)
    print(
        f'Введено число: {data2}\n'
        f'Прямой код: {direct_res2}\n'
        f'Обратный код: {decimal_to_reverse(direct_res2)}\n'
        f'Дополнительный код: {additional_res2}\n'
    )

    res_summa = summa(additional_res1, additional_res2)
    direct_res = decimal_integer_to_direct(-1)
    reverse_from_add = additional_to_reverse(res_summa)
    print(
        f'Результат сложения: {from_binary_to_decimal(decimal_to_reverse(reverse_from_add))}\n'
        f'Прямой код: {decimal_to_reverse(reverse_from_add)}\n'
        f'Обратный код: {reverse_from_add}\n'
        f'Дополнительный код: {res_summa}\n'
    )

    direct_res2 = decimal_integer_to_direct(-data2)
    reverse_res2 = decimal_to_reverse(direct_res2)
    additional_res2 = decimal_to_additional(reverse_res2)
    additional_vichit = summa(additional_res1, additional_res2)
    reverse_vichit = additional_to_reverse(additional_vichit)
    print(
        f'Результат вычитания: {from_binary_to_decimal(decimal_to_reverse(reverse_vichit))}\n'
        f'Прямой код: {decimal_to_reverse(reverse_vichit)}\n'
        f'Обратный код: {reverse_vichit}\n'
        f'Дополнительный код: {additional_vichit}\n'
    )

    direct_res2 = decimal_integer_to_direct(data2)
    multiplication_res = multiplication(direct_res1, direct_res2)
    print(
        f'Результат умножения: {from_binary_to_decimal(multiplication_res)}\n'
        f'Бинарный код: {multiplication_res}\n'
    )
    division_res = binary_division(direct_res1, direct_res2)
    print(
         f'Деление: {from_binary_to_decimal(division_res)}\n'
         f'Бинарный код: {division_res}\n'
          )

    float1 = float(input('Введите первое число с точкой: \n'))
    float2 = float(input('Введите второе число с точкой: \n'))
    float_representation1 = floating_point_representation(float1)
    float_representation2 = floating_point_representation(float2)
    print(f"32-битное представление числа {float1} по IEEE 754: {float_representation1}")
    print(f"32-битное представление числа {float2} по IEEE 754: {float_representation2}")

    sum_float_representation = add_floating_numbers(float_representation1, float_representation2)
    print(f"32-битное представление суммы {float1 + float2} по IEEE 754: {sum_float_representation}")
    print(f"Сумма в десятичном виде: {floating_point_to_decimal(sum_float_representation)}")


if __name__ == '__main__':
    main()
