import unittest
from unittest import TestCase, main
from unittest.mock import patch
import run


class BinaryArifmetics(TestCase):
    def test_decimal_integer_to_direct(self):
        self.assertEqual(run.decimal_integer_to_direct(5), '00000101')
        self.assertEqual(run.decimal_integer_to_direct(-5), '10000101')

    def test_decimal_to_reverse(self):
        self.assertEqual(run.decimal_to_reverse('00000101'), '00000101')
        self.assertEqual(run.decimal_to_reverse('10000101'), '11111010')

    def test_decimal_to_additional(self):
        self.assertEqual(run.decimal_to_additional('00000101'), '00000101')
        self.assertEqual(run.decimal_to_additional('10000101'), '10000110')

    def test_from_binary_to_decimal(self):
        self.assertEqual(run.from_binary_to_decimal('10000101'), -5)

    def test_summa(self):
        self.assertEqual(run.summa(
            '00000101',
            '00000011'
            ),
            '00001000'
        )
        self.assertEqual(run.summa(
            '00111101',
            '00000111'
        ),
            '01000100'
        )

    def test_additional_to_reverse(self):
        self.assertEqual(run.additional_to_reverse(
                '00000101'
            ),
            '00000101'
        )
        self.assertEqual(run.additional_to_reverse(
                '10000101'
            ),
            '10000100'
        )
        self.assertEqual(run.additional_to_reverse('10000110'),'10000101')

    def test_multiplication(self):
        self.assertEqual(run.multiplication(
            '00000101',
            '00000011'
            ),
            '0000000001111'
        )
        self.assertEqual(run.multiplication(
            '10000101',
            '00000011'
        ),
            '1000000001111'
        )

    def test_binary_division(self):
        self.assertEqual(run.binary_division(
            '00000101',
            '00000011'
            ),
            '00000001.10101'
        )

    def test_floating_point_representation(self):
        self.assertEqual(run.floating_point_representation(0), "00000000000000000000000000000000")
        self.assertEqual(run.floating_point_representation(5.75), "01000000101110000000000000000000")

    def test_getting_mantissa_and_exponenta(self):
        mantissa, exponenta = run.getting_mantissa_and_exponenta('110', '101')
        self.assertEqual(mantissa, '10101')  # '101'
        self.assertEqual(exponenta, 2)
        mantissa, exponenta = run.getting_mantissa_and_exponenta('', '00101')
        self.assertEqual(mantissa, '01')  # '0101'
        self.assertEqual(exponenta, -3)

    def test_binary_to_decimal(self):
        self.assertEqual(run.binary_to_decimal('1111'), 15)

    def test_floating_point_to_decimal(self):
        self.assertEqual(run.floating_point_to_decimal("01000000101110000000000000000000"), 5.75)
        self.assertEqual(run.floating_point_to_decimal("00000000000000000000000000000000"), 0.0)

    def test_add_floating_numbers(self):
        self.assertEqual(run.add_floating_numbers("01000000101110000000000000000000",
                                                  "01000000101000000000000000000000"),
                         "01000000110110000000000000000000")


if __name__ == '__main__':
    main()
