import unittest
from digital_machine import (subtraction, bits_to_string, string_to_bits, next_state, generate_transition_table,
                             create_sdnf_from_transitions, merging, format_str)


class TestDigitalMachine(unittest.TestCase):

    def test_substraction(self):
        result1 = subtraction('111')
        self.assertEqual(result1, '110')
        result2 = subtraction('100')
        self.assertEqual(result2, '011')

    def test_bits_to_string(self):
        string = bits_to_string(1, 0, 0)
        self.assertEqual(string, '100')

    def test_string_to_bits(self):
        bits = string_to_bits('101')
        self.assertEqual(bits, (1, 0, 1))

    def test_next_state(self):
        next1 = next_state(1, 1, 1)
        self.assertEqual(next1, (1, 1, 0))
        next2 = next_state(0, 0, 0)
        self.assertEqual(next2, (1, 1, 1))

    def test_generate_transition_table(self):
        table, field_names = generate_transition_table()
        self.assertEqual(field_names, ['Q2', 'Q1', 'Q0', ' ', 'Q2_next', 'Q1_next', 'Q0_next', '  ',
                                       'T2', 'T1', 'T0'])
        self.assertEqual(len(table.rows), 8)

    def test_create_sdnf_from_transitions(self):
        table, field_names = generate_transition_table()
        sdnf = create_sdnf_from_transitions(table, field_names, 'T2')
        self.assertEqual(sdnf, ['Q2 !Q1 !Q0', '!Q2 !Q1 !Q0'])

    def test_format_str(self):
        format_sdnf = format_str(['!Q1 !Q0'])
        self.assertEqual(format_sdnf, "(!Q1 !Q0)")

    def test_merging(self):
        self.assertEqual(merging(['Q2 !Q1 !Q0', '!Q2 !Q1 !Q0']),
                             ['!Q1 !Q0'])
