from ..function import Function
from ..operators.mul import Mul


class Elementary(Function):
    def __init__(self, name, input = None):
        self.name = name
        self.input = input

        return None

    def get_full_derivative(self):
        #Implements the chain rule and allows to define every other derivative as normal
        return Mul(self.get_derivative(), self.input.get_full_derivative())
