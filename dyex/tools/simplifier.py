import dyex.functions.function as func
import dyex.functions.operator as op
import dyex.functions.elementary as elem

class Simplifier():
    def __init__(self, function):
        #Raise Error if not a function
        self.function = function

        return None

    def mul_find_constants(self):
        #Do nothing if not dealing with a multiplication function
        if not isinstance(self.function, op.Mul):
            return self.function

        coeff = 1
        notConst = []
        
        for subfunc in self.function._args:
            if isinstance(subfunc, elem.Const):
                coeff *= subfunc.value
            else:
                notConst.append(subfunc)

        #If all elements in the multiplication were constants then we return the constant
        if len(notConst) == 0:
            return elem.Const(coeff)
        #If the product of the constants equals 1, we return only the other function (Check if we need to do a mul)
        elif coeff == 1:
            if len(notConst) == 1:
                return notConst[0]
            else:
                return op.Mul(*notConst)
        #Otherwise, we return the product of coeff and the rest of the functions
        return op.Mul(elem.Const(coeff), *notConst)

    def mul_distribute_sum(self):
        #Do nothing if not dealing with a multiplication function
        if not isinstance(self.function, op.Mul):
            return self.function

    def sum_similar_coefficients(self):
        return None
        

