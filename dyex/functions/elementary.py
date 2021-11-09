import math
import dyex.functions.function as func
import dyex.tools.simplifier as s

'''
Elementary class
Used to define all elementary functions (The ones found in a scientific calculator)
'''
class Elementary(func.Function):
    def __init__(self, name, input = None):
        super().__init__(name)
        self.input = input

        return None

    def get_full_derivative(self):
        #Implements the chain rule and allows to define every other derivative as normal
        return self.get_derivative() * self.input.get_full_derivative()

'''
The Poly class is used for elevating general expressions to numeric powers.
'''
class Poly(Elementary):
    def __init__(self, input, exponent = 1):
        super().__init__("Poly", input)
        self.exponent = exponent

        return None

    def __str__(self):
        return f'{self.input.__str__()}^{self.exponent}'

    def eval(self):
        return self.input.eval() ** self.exponent

    def get_derivative(self):
        if self.exponent == 1:
            return Const(1)

        return Const(self.exponent) * Poly(self.input, self.exponent - 1)

'''
Ex class represents the variable on which all other functions are defined (x)
'''
class Ex(Elementary):
    def __init__(self):
        super().__init__("Ex")

    def __str__(self):
        return 'x'

    def get_derivative(self):
        return Const(1)

    def get_full_derivative(self):
        return Const(1)

'''
Constant class used for constants like 5, sin(2pi), 4^3, etc
'''
class Const(Elementary):
    def __init__(self, value, symbol=None):
        super().__init__("Const")
        self.value = value
        self.symbol = symbol

    def __str__(self):
        return f'{self.symbol if self.symbol else self.value}'

    def get_derivative(self):
        return Const(1)

    def get_full_derivative(self):
        return Const(0)

'''
Trig classes
'''
class Sin(Elementary):
    def __init__(self, input):
        super().__init__("Sin", input)

        return None

    def __str__(self):
        return f'sin({self.input})'

    def __eval__(self):
        return math.sin(self.input.__eval__())

    def get_derivative(self):
        return Cos(self.input)

class Cos(Elementary):
    def __init__(self, input):
        super().__init__("Cos", input)

        return None

    def __str__(self):
        return f'cos({self.input})'

    def eval(self):
        return math.cos(self._input.__eval__())
    
    def get_derivative(self):
        return Const(-1) * Sin(self.input)

class Tan(Elementary):
    def __init__(self, input):
        super().__init__("Tan", input)

    def __str__(self):
        return f'tan({self.input})'

    def get_derivative(self):
        return Sec(self.input) ** 2

class Sec(Elementary):
    def __init__(self, input):
        super().__init__("Sec", input=input)
        
    def __str__(self):
        return f'sec({self.input})'
    
    def get_derivative(self):
        return Sec(self.input) * Tan(self.input)

class Csc(Elementary):
    def __init__(self, input):
        super().__init__("Csc", input=input)

    def __str__(self):
        return f'csc({self.input})'

    def get_derivative(self):
        return (Const(-1) * Csc(self.input)) * (Cot(self.input))

class Cot(Elementary):
    def __init__(self, input):
        super().__init__("Cot", input=input)

    def __str__(self):
        return f'cot({self.input})'

    def get_derivative(self):
        return Const(-1) * (Csc(self.input) ** 2)

'''
Log functions classes
'''
class LogN(Elementary):
    def __init__(self, input):
        super().__init__("LogN", input=input)

    def __str__(self):
        return f'ln({self.input})'

    def get_derivative(self):
        return Const(1)/self.input

'''
Exponential functions classes
'''
class Exp(Elementary):
    def __init__(self, base, exponent):
        super().__init__('Exp')

        self.base = base
        self.exponent = exponent

        #Allows for better calculation of the derivative
        combined_exp = s.Simplifier().simplify_nested_muls(LogN(base) * exponent)
        self.input = combined_exp

    def __str__(self):
        return f'({self.base})^({self.exponent})'

    def get_derivative(self):
        return self

class ExpNontraditional(Elementary):
    def __init__(self, name, input=None):
        super().__init__(name, input=input)
'''
Inverse functions classes
'''