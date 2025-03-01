def decimal_integer_to_direct(decimal_number):
    binary_number = ['0'] * 8
    index = len(binary_number) - 1
    if decimal_number < 0:
        decimal_number = -decimal_number
        binary_number[0] = '1'
    while decimal_number > 0 and index >= (1 if binary_number[0] == '1' else 0):
        binary_number[index] = str(decimal_number % 2)
        decimal_number //= 2
        index -= 1
    return ''.join(binary_number)


def decimal_to_reverse(binary_number):
    if binary_number[0] == '0':
        return binary_number
    else:
        inverted = [binary_number[0], ]
        for bit in binary_number[1:]:
            inverted.append('1' if bit == '0' else '0')
        return ''.join(inverted)


def decimal_to_additional(binary_number):
    if binary_number[0] == '0':
        return binary_number
    else:
        carry = 1
        result = list(binary_number)
        for i in range(len(result) - 1, -1, -1):
            if carry == 0:
                break
            if result[i] == '0':
                result[i] = '1'
                carry = 0
            else:
                result[i] = '0'
                carry = 1
        return ''.join(result)


def summa(binary_number1, binary_number2):
    index = len(binary_number1) - 1
    carry = 0
    result_summa = [''] * len(max(binary_number1, binary_number2))
    while index >= 0:
        total = carry + int(binary_number1[index]) + int(binary_number2[index])
        if total == 0:
            result_summa[index] = '0'
            carry = 0
        elif total == 1:
            result_summa[index] = '1'
            carry = 0
        elif total == 2:
            result_summa[index] = '0'
            carry = 1
        else:
            result_summa[index] = '1'
            carry = 1
        index -= 1

    return ''.join(result_summa)


def additional_to_reverse(binary_number):
    if binary_number[0] == '1':
        result_number = []
        carry = 1
        for bit in reversed(binary_number):
            if bit == '1' and carry == 1:
                result_number.append('0')  # 1 - 1 = 0
                carry = 0
            elif bit == '0' and carry == 1:
                result_number.append('1')
                carry = 1
            else:
                result_number.append(bit)
        return ''.join(reversed(result_number))
    else:
        return binary_number


def from_binary_to_decimal(binary_number, fixed_point_position=None):
    if binary_number[0] == '0':
        number_sign = 1
    else:
        number_sign = -1
    binary_number = binary_number[1:]
    if fixed_point_position is None:
        fixed_point_position = len(binary_number)
    if '.' in binary_number:
        integer_part, fractional_part = binary_number.split('.')
    else:
        integer_part = binary_number
        fractional_part = ''
    integer_part = integer_part.zfill(fixed_point_position)
    result_number = 0
    length = len(integer_part)
    for bit in range(length):
        result_number += int(integer_part[bit]) * (2 ** (length - 1 - bit))
    length = len(fractional_part)
    for bit in range(length):
        result_number += int(fractional_part[bit]) * (2 ** -(bit + 1))
    return result_number * number_sign


def multiplication(binary_number1, binary_number2):
    if binary_number1[0] != binary_number2[0]:
        number_sign = 1
    else:
        number_sign = 0
    binary_number1 = [int(bit) for bit in binary_number1][:-7:-1]
    binary_number2 = [int(bit) for bit in binary_number2][:-7:-1]
    result = [0] * (len(binary_number1) + len(binary_number2))
    for i in range(len(binary_number2)):
        for j in range(len(binary_number1)):
            if binary_number2[i] == 1:
                result[i + j] += binary_number1[j]
    carry = 0
    for i in range(len(result)):
        total = result[i] + carry
        result[i] = total % 2
        carry = total // 2
    if carry:
        result.append(carry)

    result.append(number_sign)
    return ''.join(map(str, result[::-1]))


def binary_division(number1_str, number2_str):
    if number2_str == '0' * len(number2_str):
        raise ValueError("Деление на ноль невозможно.")
    is_negative = (number1_str[0] != number2_str[0])
    num1 = number1_str[1:].zfill(8)
    num2 = number2_str[1:].zfill(8)
    quotient = ''
    remainder = '0' * 8
    for i in range(8):
        remainder = remainder[1:] + num1[i]
        if compare_binary(remainder, num2) >= 0:
            remainder = subtract_binary(remainder, num2)
            quotient += '1'
        else:
            quotient += '0'
    fractional_part = ''
    for _ in range(5):
        remainder = remainder[1:] + '0'

        if compare_binary(remainder, num2) >= 0:
            remainder = subtract_binary(remainder, num2)
            fractional_part += '1'
        else:
            fractional_part += '0'

    quotient = quotient.lstrip('0') or '0'
    quotient = quotient[-7:].zfill(7)
    result = quotient + '.' + fractional_part
    if is_negative:
        result = '1' + result
    else:
        result = '0' + result
    return result


def compare_binary(bin1, bin2):
    if len(bin1) != len(bin2):
        raise ValueError("Числа должны быть одной длины")

    for i in range(len(bin1)):
        if bin1[i] > bin2[i]:
            return 1
        elif bin1[i] < bin2[i]:
            return -1
    return 0


def subtract_binary(bin1, bin2):
    result = ''
    carry = 0
    for i in range(len(bin1) - 1, -1, -1):
        difference = int(bin1[i]) - int(bin2[i]) - carry
        if difference < 0:
            difference += 2
            carry = 1
        else:
            carry = 0
        result = str(difference) + result
    return result


def float_to_binary(float_number):
    if float_number == 0:
        return "0" * 32
    sign = '0' if float_number >= 0 else '1'
    float_number = abs(float_number)
    integer_part = int(float_number)
    fractional_part = float_number - integer_part
    integer_binary = decimal_integer_to_direct(integer_part).lstrip('0')
    schetchik = 24
    fraction_binary = ''
    while schetchik > 0:
        fractional_part *= 2
        bit = int(fractional_part)
        fraction_binary += str(bit)
        fractional_part -= bit
        if fractional_part == 0:
            break
        schetchik -= 1
    return integer_binary, fraction_binary


def getting_mantissa_and_exponenta(integer_binary, fraction_binary):
    if integer_binary:
        exponenta = len(integer_binary) - 1
        mantissa = integer_binary[1:] + fraction_binary
    else:
        first_one_index = fraction_binary.find('1')
        if first_one_index == -1:
            return "0", 0
        exponenta = -(first_one_index + 1)
        mantissa = fraction_binary[first_one_index + 1:]
    return mantissa, exponenta


def floating_point_representation(float_number):
    if float_number == 0:
        return "0" * 32
    integer_binary, binary_fraction = float_to_binary(float_number)
    mantissa, exponenta = getting_mantissa_and_exponenta(integer_binary, binary_fraction)
    sign_bit = '0' if float_number >= 0 else '1'
    exponenta += 127
    exponent_binary = decimal_integer_to_direct(exponenta)
    mantissa = mantissa.ljust(23, '0')[:23]
    floating_point_number = sign_bit + exponent_binary + mantissa
    return floating_point_number


def binary_to_decimal(binary_string):
    decimal_value = 0
    length = len(binary_string)
    for i, bit in enumerate(binary_string):
        decimal_value += int(bit) * (2 ** (length - i - 1))
    return decimal_value


def floating_point_to_decimal(floating_point_number):
    if floating_point_number == "0" * 32:
        return 0.0
    sign_bit = int(floating_point_number[0])
    exponenta_bits = floating_point_number[1:9]
    mantissa_bits = floating_point_number[9:]
    exponenta_decimal = binary_to_decimal(exponenta_bits) - 127
    mantissa = 1
    for i, bit in enumerate(mantissa_bits):
        mantissa += int(bit) * (2 ** -(i + 1))
    result = mantissa * (2 ** exponenta_decimal)
    if sign_bit == 1:
        result = -result
    return result


def add_floating_numbers(floating_number1, floating_number2):
    exponenta_bits1, mantissa_bits1 = floating_number1[1:9], floating_number1[9:]
    exponenta_bits2, mantissa_bits2 = floating_number2[1:9], floating_number2[9:]
    exponenta1 = binary_to_decimal(exponenta_bits1) - 127
    exponenta2 = binary_to_decimal(exponenta_bits2) - 127
    mantissa1 = '1' + mantissa_bits1
    mantissa2 = '1' + mantissa_bits2
    if exponenta1 > exponenta2:
        mantissa2 = '0' * (exponenta1 - exponenta2) + mantissa2
        exponent = exponenta1
    else:
        mantissa1 = '0' * (exponenta2 - exponenta1) + mantissa1
        exponent = exponenta2
    mantissa_sum = binary_summarize(mantissa1[0:24], mantissa2[0:24])
    while len(mantissa_sum) > 23:
        mantissa_sum = mantissa_sum[1:]
        # exponent += 1
    sign = '0'
    exponent_binary = decimal_integer_to_direct(exponent + 127).zfill(8)
    mantissa = mantissa_sum[0:24].ljust(23, '0')
    return sign + exponent_binary + mantissa


def binary_summarize(binary_number1, binary_number2):
    max_len = max(len(binary_number1), len(binary_number2))
    bin_str1 = binary_number1.zfill(max_len)
    bin_str2 = binary_number2.zfill(max_len)
    carry = 0
    result = []
    for bit1, bit2 in zip(reversed(bin_str1), reversed(bin_str2)):
        total = int(bit1) + int(bit2) + carry
        result.append(str(total % 2))
        carry = total // 2
    if carry:
        result.append(str(carry))
    return ''.join(reversed(result))
