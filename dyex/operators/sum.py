from .operator import Operator

class Sum(Operator):
    def __init__(self, *args):
        super().__init__()
        self._args = args

        return self

    def derivative(self, func1, func2):
        return Sum(func.derivative() for func in self._args)
