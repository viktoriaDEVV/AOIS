import unittest
from summator import truth_table, create_sdnf, format_str, merging


class TestSummFunctions(unittest.TestCase):

    def test_truth_table(self):
        table, field_names = truth_table(['A', 'B', 'Cin'])
        self.assertEqual(field_names, ['A', 'B', 'Cin', 'S', 'C(out)'])
        self.assertEqual(len(table.rows), 8)

    def test_create_sdnf(self):
        table, field_names = truth_table(['A', 'B', 'Cin'])
        sdnf_summ = create_sdnf(table, field_names, 'sum')
        self.assertEqual(sdnf_summ, ['!A !B Cin', '!A B !Cin', 'A !B !Cin', 'A B Cin'])

    def test_format_str(self):
        format_sdnf = format_str(['!A !B Cin', '!A B !Cin', 'A !B !Cin', 'A B Cin'])
        self.assertEqual(format_sdnf, "(!A !B Cin) ∨ (!A B !Cin) ∨ (A !B !Cin) ∨ (A B Cin)")

    def test_merging(self):
        self.assertEqual(merging(['!A !B Cin', '!A B !Cin', 'A !B !Cin', 'A B Cin']),
                         ['!A !B Cin', '!A B !Cin', 'A !B !Cin', 'A B Cin'])
