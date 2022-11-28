from fractions import Fraction


class Matrix:
    def __init__(self, matrix: list[list[int | Fraction]]) -> None:
        self.matrix = [[y for y in x] for x in matrix]

    def swap(self, row_a: int, row_b: int):
        self.matrix[row_a], self.matrix[row_b] = self.matrix[row_b], self.matrix[row_a]

    def multiply_row(self, row: int, coefficient: int | Fraction):
        self.matrix[row] = [el * coefficient for el in self.matrix[row]]

    def add_row_to_row(self, source_row: int, target_row: int, source_coefficient: int | Fraction):
        m = self.matrix
        m[target_row] = [m[target_row][i] + m[source_row][i] *
                         source_coefficient for i in range(len(m[target_row]))]
