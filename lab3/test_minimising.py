import unittest
from minimising import *
from prettytable import PrettyTable


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
        table, field_names, truth_values = truth_table("a & b")
        self.assertEqual(field_names, ['a', 'b', 'a&b'])
        self.assertEqual(len(table.rows), 4)
        table, field_names, truth_values = truth_table("(!a) & b")
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
        table, field_names, truth_values = truth_table('a&b')
        sknf = create_sknf(table, field_names)
        self.assertEqual(sknf, ['a  b', 'a  !b', '!a  b'])

    def test_create_sdnf(self):
        table, field_names, truth_values = truth_table('a&b')
        sdnf = create_sdnf(table, field_names)
        self.assertEqual(sdnf, ["a b"])

    def test_format_str(self):
        table, field_names, truth_values = truth_table('a&b')
        sdnf = create_sdnf(table, field_names)
        format_sdnf = format_str(sdnf, 1)
        sknf = create_sknf(table, field_names)
        format_sknf = format_str(sknf, 0)
        self.assertEqual(format_sdnf, "(a b)")
        self.assertEqual(format_sknf, "(a  b) ∧ (a  !b) ∧ (!a  b)")

    def test_merging(self):
        self.assertEqual(merging(['a  b  c', '!a  b  c', '!a  !b  c']), ['b c', '!a c'])

    def test_build_table(self):
        constituents = ['a  b  c', '!a  b  c', '!a  !b  c']
        minimized = ['b c', '!a c']

        expected_output = PrettyTable()
        expected_output.field_names = [""] + constituents
        expected_output.add_row(["b c", 'X', 'X', ''])
        expected_output.add_row(["!a c", '', 'X', 'X'])

        result = build_table(constituents, minimized)
        self.assertEqual(result.get_string(), expected_output.get_string())

    def test_minimized_from_table(self):
        table = PrettyTable()
        table.field_names = ["", "a", "b", "c"]
        table.add_row(["x1", "X", "", "X"])
        table.add_row(["x2", "", "X", ""])
        result = minimized_from_table(table)
        self.assertEqual(set(result), {"x1", "x2"})

    def test_generate_gray_code(self):
        self.assertEqual(generate_gray_code(1), ['0', '1'])
        self.assertEqual(generate_gray_code(2), ['00', '01', '11', '10'])
        self.assertEqual(generate_gray_code(3), ['000', '001', '011', '010', '110', '111', '101', '100'])

    def test_find_groups(self):
        variables = ['a', 'b']
        truth_values = {'00': 0, '01': 1, '10': 1, '11': 0}
        groups = find_groups(variables, truth_values, 'SDNF')
        self.assertEqual(groups, [('0', '1'), ('1', '0')])

    def test_merge_groups(self):
        groups = ['000', '100', '110']
        merged = merge_groups(groups)
        expected_merged = ['-00', '1-0']

        for expected in expected_merged:
            self.assertIn(expected, merged)
        self.assertEqual(len(merged), len(set(merged)))

    def test_minimize(self):
        variables = ['a', 'b', 'c']
        groups = [('0', '00'), ('1', '00'), ('1', '10')]
        expression = minimize(variables, groups, 'SKNF')
        self.assertIn('(', expression)


if __name__ == '__main__':
    unittest.main()
