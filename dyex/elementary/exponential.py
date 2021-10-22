import math

from .elementary import Elementary

class Exponential(Elementary):
    def __init__(self, input):
        super().__init__("exp", input)

        return self

    def __eval__(self):
        return math.exp(self.input.__eval__)