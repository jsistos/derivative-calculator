import math
import dyex.functions.function as func
import dyex.functions.operator as op

'''
Elementary class
Used to define all elementary functions (The ones found in a scientific calculator)
'''
class Elementary(func.Function):
    def __init__(self, name, input = None):
        self.name = name
        self.input = input

        return None

    def get_full_derivative(self):
        #Implements the chain rule and allows to define every other derivative as normal
        return self.get_derivative() * self.input.get_full_derivative()

'''
The Poly class is used for elevating general expressions to numeric powers.
'''
class Poly(Elementary):
    def __init__(self, input, degree = 1):
        super().__init__("POLY", input)
        self.degree = degree

        return None

    def __str__(self):
        return f'{self.input.__str__()}^{self.degree}'

    def eval(self):
        return self.input.eval() ** self.degree

    def get_derivative(self):
        if self.degree == 1:
            return Const(1)

        return Const(self.degree) * Poly(self.input, self.degree - 1)

'''
Ex class represents the variable on which all other functions are defined (x)
'''
class Ex(Elementary):
    def __init__(self):
        super().__init__("X")

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
    def __init__(self, value):
        super().__init__("CONST")
        self.value = value

    def __str__(self):
        return f'{self.value}'

    def get_derivative(self):
        return Const(1)

    def get_full_derivative(self):
        return Const(0)

'''
Trig classes
'''
class Sine(Elementary):
    def __init__(self, input):
        super().__init__("SIN", input)

        return None

    def __str__(self):
        return f'sin({self.input})'

    def __eval__(self):
        return math.sin(self.input.__eval__())

    def get_derivative(self):
        return Cosine(self.input)

class Cosine(Elementary):
    def __init__(self, input):
        super().__init__("COS", input)

        return None

    def __str__(self):
        return f'cos({self.input})'

    def eval(self):
        return math.cos(self._input.__eval__())
    
    def get_derivative(self):
        return Const(-1) * Sine(self.input)

class Tangent(Elementary):
    def __init__(self, input):
        super().__init__("TAN", input)

    def __str__(self):
        return f'tan({self.input})'

    def get_derivative(self):
        return Secant(self.input) ** 2

class Secant(Elementary):
    def __init__(self, input):
        super().__init__("SEC", input=input)
        
    def __str__(self):
        return f'sec({self.input})'
    
    def get_derivative(self):
        return Secant(self.input) * Tangent(self.input)

class Cosecant(Elementary):
    def __init__(self, input):
        super().__init__("CSC", input=input)

    def __str__(self):
        return f'csc({self.input})'

    def get_derivative(self):
        return (Const(-1) * Cosecant(self.input)) * (Cotangent(self.input))

class Cotangent(Elementary):
    def __init__(self, input):
        super().__init__("COT", input=input)

    def __str__(self):
        return f'cot({self.input})'

    def get_derivative(self):
        return Const(-1) * (Cosecant(self.input) ** 2)

'''
Log functions classes
'''

'''
Exponential functions classes
'''

'''
Inverse functions classes
'''