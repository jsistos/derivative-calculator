import dyex.functions.operator as op
import dyex.functions.elementary as elem

class Simplifier():
    '''Maybe the simplifier methods should be class methods'''
    def simplify_fully(self, func):

        #Try to simplify exponent function
        '''func = self.simplify_nested_exp()'''

        #Try to simplify multiplication function
        func = self.simplify_nested_muls(func)
        '''func = self.simplify_exp_in_mul(func)'''
        func = self.simplify_constants_mul(func)

        #Try to simplify sum function
        func = self.simplify_nested_sums(func)
        func = self.simplify_muls_in_sum(func)
        func = self.simplify_constants_sum(func)

        return func
    '''
        simplify_constants_mul(self, func) - Gets rid of constants by joining them
    '''
    def simplify_constants_mul(self, func):
        #Do nothing if not dealing with a multiplication function
        if not isinstance(func, op.Mul):
            return func

        coeff = 1
        notConst = []
        
        for subfunc in func._args:
            if isinstance(subfunc, elem.Const):
                coeff *= subfunc.value
            else:
                notConst.append(subfunc)

        #If all elements in the multiplication were constants then we return the constant
        if len(notConst) == 0:
            return elem.Const(coeff)
        #If the product of the constants equals 0, we return 0 as well.
        elif coeff == 0:
            return elem.Const(0)
        #If the product of the constants equals 1, we return only the other function.
        elif coeff == 1:
            if len(notConst) == 1:
                return notConst[0]
            else:
                return op.Mul(*notConst)
        #Otherwise, we return the product of coeff and the rest of the functions
        return op.Mul(elem.Const(coeff), *notConst)

    '''
        simplify_constants_sum(self, func) - Gets rid of constants by adding them all
    '''
    def simplify_constants_sum(self, func):
        #Do nothing if not dealing with a sum function
        if not isinstance(func, op.Sum):
            return func
        
        coeff = 0
        notConst = []
        
        for subfunc in func._args:
            if isinstance(subfunc, elem.Const):
                coeff += subfunc.value
            else:
                notConst.append(subfunc)

        #If all elements in the sum were constants then we return the constant
        if len(notConst) == 0:
            return elem.Const(coeff)
        #If the sum of the constants equals 0, we return only the other function (Check if we need to do a sum)
        elif coeff == 0:
            if len(notConst) == 1:
                return notConst[0]
            else:
                return op.Sum(*notConst)
        #Otherwise, we return the product of coeff and the rest of the functions
        return op.Sum(*notConst, elem.Const(coeff))

    '''
        simplify_nested_exp(self, func) - Gets rid of exp issues by joining them all
    '''
    def simplify_nested_exp(self, func):
        if not isinstance(func, (elem.Exp, elem.Poly)):
            return func

    '''
        simplify_nested_muls(self, func) - Gets rid of Mul instances inside Mul instances
    '''
    def simplify_nested_muls(self, func):
        #Do nothing if not dealing with a multiplication function
        if not isinstance(func, op.Mul):
            return func

        mul_parts = []
        for subfunc in func._args:
            if isinstance(subfunc, op.Mul):
                subfunc = Simplifier().simplify_nested_muls(subfunc)
                mul_parts += subfunc._args
            else:
                mul_parts.append(subfunc)
            
        return op.Mul(*mul_parts)

    '''
        simplify_nested_sums(self, func) - Gets rid of Sum instances inside Sum instances
    '''
    def simplify_nested_sums(self, func):
        #Do nothing if not dealing with a sum function
        if not isinstance(func, op.Sum):
            return func

        sum_parts = []
        for subfunc in func._args:
            if isinstance(subfunc, op.Sum):
                subfunc = Simplifier().simplify_nested_sums(subfunc)
                sum_parts += subfunc._args
            else:
                sum_parts.append(subfunc)

        return op.Sum(*sum_parts)

    def mul_distribute_sum(self, func):
        #Do nothing if not dealing with a multiplication function
        if not isinstance(func, op.Mul):
            return func

    def sum_similar_coefficients(self):
        return None

    '''
        simplify_muls_in_sum(self, func) - Accesess all elements of a sum to simplify them
    '''
    def simplify_muls_in_sum(self, func):
        #Do nothing if this is not a sum
        if not isinstance(func, op.Sum):
            return func

        newArgs = []
        for subfunc in func._args:
            #In every argument, convert all that can be converted to a single multiplication.
            #Then, simplify all constants
            '''subfunc = self.simplify_exp_in_mul'''
            subfunc = self.simplify_nested_muls(subfunc)
            subfunc = self.simplify_constants_mul(subfunc)
            newArgs.append(subfunc)
        
        #Rebuild this function
        func = op.Sum(*newArgs)
        return func
