class Function():
    def __init__(self, name):
        self.name = name
        self._args = []
        return None

    def __add__(self, other):
        import dyex.functions.operator as op
        return op.Sum(self, other)

    def __mul__(self, other):
        import dyex.functions.operator as op
        import dyex.functions.elementary as elem

        if isinstance(other, (int, float)):
            return op.Mul(self, elem.Const(other))
        return op.Mul(self, other)

    def __rmul__(self, other):
        import dyex.functions.operator as op
        import dyex.functions.elementary as elem

        if isinstance(other, (int, float)):
            return op.Mul(elem.Const(other), self)
        return op.Mul(other, self)

    def __truediv__(self, other):
        import dyex.functions.operator as op
        return op.Div(self, other)
    
    def __sub__(self, other):
        import dyex.functions.elementary as elem
        return self + elem.Const(-1) * other

    def __pow__(self, degree):
        import dyex.functions.elementary as elem
        if isinstance(degree, (int, float)):
            return elem.Poly(self, degree)
        return elem.Poly(self, degree.value)
    
    #def __init__(self, func_string = ""):
        