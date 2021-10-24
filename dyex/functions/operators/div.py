from ..operators.mul import Mul
from ..elementary.polynomial import Poly
from .operator import Operator
from .sum import Sum

class Div(Operator):
    def __init__(self, numeratorFunc, denominatorFunc):
        super().__init__()
        self.numerator = numeratorFunc
        self.denominator = denominatorFunc

    def get_full_derivative(self):
        return Div(Sum(
            Mul(self.numerator.get_full_derivative(), self.denominator),
            Mul(self.numerator, self.denominator.get_full_derivative())
            ),
            Poly(self.denominatorFunc, 2))