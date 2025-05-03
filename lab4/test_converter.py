import unittest
from converter import decimal_to_binary, create_sdnf_expressions, d8421_table


class TestConvFunctions(unittest.TestCase):

    def test_decimal_to_binary(self):
        binary = decimal_to_binary(0)
        self.assertEqual(binary, '0000')

    def test_create_sdnf_expressions(self):
        table = d8421_table()
        sdnf = create_sdnf_expressions(table, ["x1", "x2", "x3", "x4"])
        self.assertEqual(sdnf, [['!x1  x2  x3  x4', 'x1  !x2  !x3  !x4'], ['!x1  !x2  x3  x4',
                                                                           '!x1  x2  !x3  !x4', '!x1  x2  !x3  x4',
                                                                           '!x1  x2  x3  !x4'], ['!x1  !x2  !x3  x4',
                                                                                                 '!x1  !x2  x3  !x4',
                                                                                                 '!x1  x2  !x3  x4',
                                                                                                 '!x1  x2  x3  !x4'],
                                ['!x1  !x2  !x3  !x4', '!x1  !x2  x3  !x4', '!x1  x2  !x3  !x4', '!x1  x2  x3  !x4',
                                 'x1  !x2  !x3  !x4']])
