from dyex.function import Function


class Elementary(Function):
    def __init__(self, name, input):
        self.name = name
        self.input = input

        return self
    
    def derivative(self):
        return self._derivative
