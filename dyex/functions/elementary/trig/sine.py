import math

from ...operators.mul import Mul

from ..elementary import Elementary
from .cosine import Cosine


class Sine(Elementary):
    def __init__(self, input):
        super().__init__("sin", input)

        return None

    def __eval__(self):
        return math.sin(self.input.__eval__())

    def get_derivative(self):
        return Mul(Cosine(self.input), self.input.get_derivative)