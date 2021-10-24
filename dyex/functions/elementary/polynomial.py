from ..elementary.elementary import Elementary
from ..function import Function
from ..operators.mul import Mul


#The Poly class is used for elevating general expressions to numeric powers
class Poly(Elementary):
    def __init__(self, input, degree):
        super().__init__("polynomic", input)
        self.degree = degree

        return None

    def __str__(self):
        return f'({self.input.__str__()})^{self.degree}'

    def eval(self):
        return self.input.eval() ** self.degree

    def get_derivative(self):
        if self.degree == 1:
            return Const(1)
        return Mul(Const(self.degree), Poly(self.input, self.degree - 1))


'''
The following two classes are used to overload the recursion derivative relationship.
'''
class Ex(Elementary):
    def __init__(self):
        super().__init__("ex")

    def __str__(self):
        return 'x'

    def get_derivative(self):
        return Const(1)

    def get_full_derivative(self):
        return Const(1)

class Const(Elementary):
    def __init__(self, value):
        super().__init__("constant")
        self.value = value

    def __str__(self):
        return f'{self.value}'

    def get_derivative(self):
        return Const(1)

    def get_full_derivative(self):
        return Const(0)