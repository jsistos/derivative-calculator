from .operator import Operator

class Sum(Operator):
    def __init__(self, *args):
        super().__init__()
        self._args = args

        return self

    def eval(self):
        result = 0
        for func in self._args:
            #What happens with functions that are negative?
            result += func.__eval__()
        
        return result
        

    def get_derivative(self):
        return Sum(func.get_derivative() for func in self._args)
