from fractions import Fraction
import unittest
from matrix import Matrix


class MatrixTest(unittest.TestCase):

    def test_init_creates_deep_copy_of_given_matrix(self):
        original = [
            [1, 2],
            [3, 4]
        ]
        m = Matrix(original)
        original[0] = [0, 0]
        original[1][0] = 0

        self.assertEqual(
            [
                [1, 2],
                [3, 4]
            ], m.matrix
        )

    def test_swap_swaps_rows(self):
        m = Matrix([
            [3, 1, 0],
            [-1, 2, 2],
            [5, 0, -1],
        ])
        m.swap(1, 2)
        self.assertEqual(
            [
                [3, 1, 0],
                [5, 0, -1],
                [-1, 2, 2],
            ], m.matrix
        )

    def test_swap_same_row_does_nothing(self):
        m = Matrix([
            [3, 1, 0],
            [-1, 2, 2],
            [5, 0, -1],
        ])
        m.swap(0, 0)
        self.assertEqual(
            [
                [3, 1, 0],
                [-1, 2, 2],
                [5, 0, -1],
            ], m.matrix
        )

    def test_multiply_by_int_multiplies_each_element_in_row(self):
        m = Matrix([
            [2, Fraction(1, 2), Fraction(3, 7)],
            [1, 2, 3],
        ])

        m.multiply_row(0, 3)

        self.assertEqual(
            [
                [6, Fraction(3, 2), Fraction(9, 7)],
                [1, 2, 3],
            ], m.matrix
        )

    def test_multiply_by_fraction_multiplies_each_element_in_row(self):
        m = Matrix([
            [0, 3, 5],
            [1, 2, 3],
        ])

        m.multiply_row(1, Fraction(1, 2))

        self.assertEqual(
            [
                [0, 3, 5],
                [Fraction(1, 2), 1, Fraction(3, 2)]
            ], m.matrix
        )

    def test_multiply_by_zero_raises_error(self):
        m = Matrix([
            [0, 3, 5],
            [1, 2, 3],
        ])

        self.assertRaises(ValueError, lambda: m.multiply_row(1, 0))

    def test_add_one_row_into_another_without_multiplication(self):
        m = Matrix([
            [1, 2, 3],
            [3, Fraction(1, 2), 6]
        ])

        m.add_row_to_row(0, 1, 1)

        self.assertEqual(
            [
                [1, 2, 3],
                [4, Fraction(5, 2), 9]
            ], m.matrix
        )

    def test_add_one_row_into_another_with_multiplication(self):
        m = Matrix([
            [1, 2, 3],
            [3, Fraction(1, 2), 6]
        ])

        m.add_row_to_row(1, 0, -2)

        self.assertEqual(
            [
                [-5, 1, -9],
                [3, Fraction(1, 2), 6]
            ], m.matrix
        )

    def test_determinant_for_empty_matrix_is_one(self):
        m = Matrix([])
        self.assertEqual(1, m.determinant)

    def test_determinant_throws_exception_for_non_square_matrix(self):
        m = Matrix([
            [1, 2, 3],
            [3, Fraction(1, 2), 6]
        ])

        self.assertRaises(ValueError, lambda: m.determinant)

    def test_determinant_of_1x1_matrix_is_the_number_itself(self):
        m = Matrix([[2]])
        self.assertEqual(2, m.determinant)

    def test_determinant_of_2x2_matrix(self):
        m = Matrix([
            [-2, -6],
            [-7, 5]
        ])
        self.assertEqual(-52, m.determinant)

    def test_determinant_of_3x3_matrix(self):
        m = Matrix([
            [4, 2, 1],
            [-2, -6, 3],
            [-7, 5, 0]
        ])
        self.assertEqual(-154, m.determinant)

    def test_determinant_of_4x4_matrix(self):
        m = Matrix([
            [1, 2, 3, 4],
            [4, 5, 6, 7],
            [8, 9, 10, 11],
            [12, 13, 14, 15]
        ])
        self.assertEqual(0, m.determinant)


if __name__ == "__main__":
    unittest.main()
