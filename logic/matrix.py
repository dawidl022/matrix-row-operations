from fractions import Fraction


class Matrix:
    def __init__(self, matrix: list[list[int | Fraction]]) -> None:
        self.matrix = [[y for y in x] for x in matrix]

    def swap(self, row_a: int, row_b: int):
        self.matrix[row_a], self.matrix[row_b] = self.matrix[row_b], self.matrix[row_a]

    def multiply_row(self, row: int, coefficient: int | Fraction):
        if coefficient == 0:
            raise ValueError(
                "multiplying a row by 0 would break the matrix row equivalence property")
        self.matrix[row] = [el * coefficient for el in self.matrix[row]]

    def add_row_to_row(self, source_row: int, target_row: int, source_coefficient: int | Fraction):
        m = self.matrix
        m[target_row] = [m[target_row][i] + m[source_row][i] *
                         source_coefficient for i in range(len(m[target_row]))]

    @property
    def determinant(self):
        if len(self.matrix) == 0:
            return 1
        if len(self.matrix) != len(self.matrix[0]):
            raise ValueError
        if len(self.matrix) == 1:
            return self.matrix[0][0]

        total = 0
        for j in range(len(self.matrix)):
            total += (-1) ** j * \
                self.matrix[0][j] * self._minor_matrix(j).determinant

        return total

    def _minor_matrix(self, j: int) -> 'Matrix':
        sub_m = [[0 for _ in range(len(self.matrix) - 1)]
                 for _ in range(len(self.matrix) - 1)]
        sub_i = 0
        for k in range(1, len(self.matrix)):
            sub_j = 0
            for l in range(len(self.matrix[0])):
                if l != j:
                    sub_m[sub_i][sub_j] = self.matrix[k][l]
                    sub_j += 1
            sub_i += 1
        return Matrix(sub_m)
