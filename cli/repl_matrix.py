from fractions import Fraction
from typing import Callable
from logic.matrix import Matrix


class ReplMatrix(Matrix):

    @staticmethod
    def print_after_operation(f: Callable):
        def wrapper(self: 'ReplMatrix', *args, **kwargs):
            result = f(self, *args, **kwargs)

            for row in self.matrix:
                print([str(x) for x in row])

            return result
        return wrapper

    @print_after_operation
    def swap(self, row_a: int, row_b: int):
        return super().swap(row_a, row_b)

    @print_after_operation
    def multiply_row(self, row: int, coefficient: int | Fraction):
        return super().multiply_row(row, coefficient)

    @print_after_operation
    def add_row_to_row(self, source_row: int, target_row: int, source_coefficient: int | Fraction):
        return super().add_row_to_row(source_row, target_row, source_coefficient)
