import math

from dyex.elementary.trig.sine import Sine
from dyex.function import Function
from ..elementary import Elementary


class Cosine(Elementary):
    def __init__(self, input):
        super().__init__("cos", input)
        
        self.derivative = Function(-Sine(input))

        return self

    def __eval__(self):
        return math.cos(self._input.__eval__())