import random as rd


def create_binary_matrix():
    binary_matrix = [[rd.randint(0, 1) for _ in range(16)] for _ in range(16)]
    return binary_matrix


def get_word(binary_matrix, word_number):
    word = []
    for i in range(word_number, len(binary_matrix)):
        word.append(binary_matrix[i][word_number])
    for i in range(word_number):
        word.append(binary_matrix[i][word_number])
    return ''.join(map(str, word))


def get_column_address(binary_matrix, column_number):
    address = []
    i = 0

    for j in range(len(binary_matrix) - column_number):
        address.append(binary_matrix[column_number + j][j])
    for j in range(len(binary_matrix) - column_number, len(binary_matrix)):
        address.append(binary_matrix[i][j])
        i += 1
    return ''.join(map(str, address))


def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))
