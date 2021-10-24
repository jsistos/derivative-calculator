import math

from ..elementary import Elementary

class Exponential(Elementary):
    def __init__(self, input):
        super().__init__("exp", input)

        return self

    def eval(self):
        return math.exp(self.input.__eval__)

    def get_derivative(self):
        return Exponential(self.input)