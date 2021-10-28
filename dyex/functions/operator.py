import dyex.functions.function as func
import dyex.functions.elementary as elem


class Operator(func.Function):
    def __init__(self, name):
        self.name = name
        return None

class Sum(Operator):
    def __init__(self, func1, func2, *args):
        super().__init__('SUM')
        self._args = [func1, func2, *args]

        return None

    def __str__(self):
        retStr = f'{self._args[0]}'
        for func in self._args[1::]:
            retStr+= f' + {func}'
        return retStr

    def get_full_derivative(self):
        #You can use the * operator before an iterable to expand it within the function call.
        #Use to so a general sum operator
        return Sum(*[func.get_full_derivative() for func in self._args])

    def eval(self):
        result = 0
        for func in self._args:
            #What happens with functions that are negative?
            result += func.eval()
        
        return result

class Mul(Operator):
    def __init__(self, func1, func2, *args):
        super().__init__("mulOP")
        self._args = [func1, func2, *args]

    def __str__(self):
        retStr = ''

        for subFunc in self._args:
            retStr += f'({subFunc})'

        return retStr

    def get_full_derivative(self):
        copy_args = self._args[::]
        rSide = copy_args[-1]
        lSide = copy_args[:-1:]

        if(len(lSide) != 1):
            lSide = Mul(*lSide)
        else:
            lSide = lSide[0]

        return lSide * rSide.get_full_derivative() + lSide.get_full_derivative() * rSide

class Div(Operator):
    def __init__(self, numerator, denominator):
        super().__init__('DIV')
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        #Look into circular dependency issue
        if isinstance(self.numerator, Sum) and isinstance(self.denominator, Sum):
            return f'({self.numerator})/({self.denominator})'
        elif isinstance(self.numerator, Sum):
            return f'({self.numerator})/{self.denominator}'
        elif isinstance(self.denominator, Sum):
            return f'{self.numerator}/({self.denominator})'
        else:
            return f'{self.numerator}/{self.denominator}'

    def get_full_derivative(self):
        return (self.numerator.get_full_derivative() * self.denominator 
        - self.numerator * self.denominator.get_full_derivative())/(self.denominator ** 2)