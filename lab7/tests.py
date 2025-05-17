import unittest
from matrix import *
from functions import *
from sum import sum_words
from search import g_l_search


binary_matrix = [
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]


class TestMatrix(unittest.TestCase):

    def test_create_binary_matrix(self):
        bin_matrix = create_binary_matrix()
        self.assertEqual(len(binary_matrix), 16)  # Проверяем количество строк
        self.assertTrue(all(len(row) == 16 for row in bin_matrix))

    def test_get_word(self):
        word = get_word(binary_matrix, 0)
        self.assertEqual(word, '1010101010101010')

    def test_get_column_address(self):
        address = get_column_address(binary_matrix, 0)
        self.assertEqual(address, '1110111011101110')


class TestFunctions(unittest.TestCase):

    def test_function0(self):
        self.assertEqual(function0(), '0')

    def test_function5(self):
        word = '111011101101110'
        self.assertEqual(function5(word), '111011101101110')

    def test_function10(self):
        word = '111011101101110'
        self.assertEqual(function10(word), ['0', '0', '0', '1', '0', '0', '0', '1', '0', '0', '1', '0', '0', '0', '1'])

    def test_function15(self):
        self.assertEqual(function15(), '1')


class TestSum(unittest.TestCase):

    def test_sum_words(self):
        suitable_words, suitable_words_result = sum_words(binary_matrix, '110')
        self.assertEqual(suitable_words, ['1100110011001100', '1100110011001100', '1100110011001100', '1100110011001100'])
        self.assertEqual(suitable_words_result, ['1100110011001100', '1100110011001100', '1100110011001100', '1100110011001100'])


class TestSearch(unittest.TestCase):

    def test_g_l_search(self):
        arg = '1010101010101010'
        g_values, l_values, counts, words = g_l_search(binary_matrix, arg)
        expected_g_values = [False, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True]
        expected_l_values = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        expected_counts = [16, 8, 16, 8, 16, 8, 16, 8, 16, 8, 16, 8, 16, 8, 16, 8]

        self.assertEqual(g_values, expected_g_values)
        self.assertEqual(l_values, expected_l_values)
        self.assertEqual(counts, expected_counts)


if __name__ == '__main__':
    unittest.main()