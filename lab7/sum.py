from matrix import get_word


def summa(binary_number1, binary_number2):
    index = len(binary_number1) - 1
    carry = 0
    result_summa = [''] * 5
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
    result_summa.insert(0, str(carry))
    return ''.join(result_summa)


def sum_words(binary_matrix, key):
    words = []
    suitable_words = []
    for word_number in range(16):
        word = get_word(binary_matrix, word_number)
        words.append(word)
    for word in words:
        if word[:3] == key:
            suitable_words.append(word)
    suitable_words_result = []
    for suit_word in suitable_words:
        term1 = suit_word[3:7]
        term2 = suit_word[7:11]
        summed_value = summa(term1, term2)
        new_word = suit_word[:11] + summed_value
        suitable_words_result.append(new_word)
    return suitable_words, suitable_words_result
