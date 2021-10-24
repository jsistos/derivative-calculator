import math

from dyex.elementary.trig.sine import Sine
from dyex.function import Function
from ..elementary import Elementary


class Cosine(Elementary):
    def __init__(self, input):
        super().__init__("cos", input)

        return None

    def eval(self):
        return math.cos(self._input.__eval__())
    
    def get_derivative(self):
        return Function(-Sine(self.input))