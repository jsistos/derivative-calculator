import math

from ..elementary import Elementary
from .cosine import Cosine


class Sine(Elementary):
    def __init__(self, input):
        super().__init__("sin", input)
        
        self.derivative = Cosine(input)

        return self

    def __eval__(self):
        return math.sin(self.input.__eval__())