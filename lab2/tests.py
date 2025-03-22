import unittest
from truthTable import *


class TestLogicFunctions(unittest.TestCase):

    def test_is_logical_formula(self):
        self.assertTrue(is_logical_formula("a & b"))
        self.assertTrue(is_logical_formula("!a | b"))
        self.assertEqual(is_logical_formula("a8% b"), False)

    def test_extracting_variables(self):
        self.assertEqual(extracting_variables("a & b"), ['a', 'b'])
        self.assertEqual(extracting_variables("!a | b & c"), ['a', 'b', 'c'])
        self.assertEqual(extracting_variables("d -> e"), ['d', 'e'])

    def test_truth_table(self):
        table, field_names = truth_table("a & b")
        self.assertEqual(field_names, ['a', 'b', 'a&b'])
        self.assertEqual(len(table.rows), 4)
        table, field_names = truth_table("(!a) & b")
        self.assertEqual(field_names, ['a', 'b', '!a', '(!a)&b'])
        self.assertEqual(len(table.rows), 4)

    def test_evaluate(self):
        self.assertEqual(evaluate('True', {}), 1)
        self.assertEqual(evaluate('!False', {}), 1)
        self.assertEqual(evaluate('x & y', {'x': 1, 'y': 0}), 0)
        self.assertEqual(evaluate('x | y', {'x': 1, 'y': 0}), 1)
        self.assertEqual(evaluate('x -> y', {'x': 1, 'y': 0}), 0)
        self.assertEqual(evaluate('(x ~ y)', {'x': 1, 'y': 1}), 1)

    def test_remove_outer_parentheses(self):
        self.assertEqual(remove_outer_parentheses('(a&b)'), 'a&b')
        self.assertEqual(remove_outer_parentheses('(a|b)'), 'a|b')

    def test_extracting_sub_formulas(self):
        self.assertEqual(extracting_sub_formulas("(!a)&b"), ['a', 'b', '!a', '(!a)&b'])

    def test_find_last_operator(self):
        self.assertEqual(find_last_operator('a & b | c', ['&', '|']), 6)

    def test_create_sknf(self):
        table, field_names = truth_table('a&b')
        sknf = create_sknf(table, field_names)
        self.assertEqual(sknf, "(a ∨ b) ∧ (a ∨ !b) ∧ (!a ∨ b)")

    def test_create_sdnf(self):
        table, field_names = truth_table('a&b')
        sdnf = create_sdnf(table, field_names)
        self.assertEqual(sdnf, "(a ∧ b)")

    def test_digital_form_sknf(self):
        table, field_names = truth_table('a&b')
        digital_sknf = digital_form_sknf(table)
        self.assertEqual(digital_sknf, "(0, 1, 2) ∧")

    def test_digital_form_sdnf(self):
        table, field_names = truth_table('a&b')
        digital_sdnf = digital_form_sdnf(table)
        self.assertEqual(digital_sdnf, "(3) ∨")

    def test_index_form(self):
        table, field_names = truth_table('a&b')
        index, binary_result = index_form(table)
        self.assertEqual(index, 1)
        self.assertEqual(binary_result, '0001')


if __name__ == '__main__':
    unittest.main()
