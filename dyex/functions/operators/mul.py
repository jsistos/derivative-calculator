from .operator import Operator
from .sum import Sum

class Mul(Operator):
    def __init__(self, func1, func2):
        super().__init__()
        self.func1 = func1
        self.func2 = func2

    def __str__(self):
        return f'({self.func1})({self.func2})'

    def get_full_derivative(self):
        return Sum(Mul(self.func1.get_full_derivative(), self.func2), Mul(self.func1, self.func2.get_full_derivative()))

    def eval(self):
        return self.func1.eval() * self.func1.eval()