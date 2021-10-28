import dyex.functions.operator as op
import dyex.functions.elementary as elem

from dyex.tools.simplifier import Simplifier

'''
cube = elem.Poly(elem.Ex(), 3)
dydx2 = cube.get_full_derivative()

sqrt = elem.Poly(elem.Ex(), 1./2)
dydx3 = sqrt.get_full_derivative()

inv = elem.Poly(elem.Ex(), -1)
dydx4 = inv.get_full_derivative()

pol1 = cube + sqrt
pol2 = cube * sqrt
print(pol1)
print(pol2)

print(f'{cube} has a derivative of {dydx2}')
print(f'{sqrt} has a derivative of {dydx3}')
print(f'{inv} has a derivative of {dydx4}')


exp1 = op.Sum(elem.Poly(elem.Ex(), 2), op.Mul(elem.Const(2), elem.Ex()), elem.Const(5))
print(f'Expression: {exp1}')

der = exp1.get_full_derivative()
print(f'Derivative: {der}')

exp2 = op.Div(elem.Const(1), elem.Ex())
print(exp2)
print(exp2.get_full_derivative())

expA = elem.Sine(elem.Sine(exp1))
print(expA)
print(expA.get_full_derivative())

mult = op.Mul(elem.Const(2), elem.Const(3))
print(mult)

mult = Simplifier(mult).simplify_const_mul()
print(mult)
'''

f = op.Mul(elem.Poly(elem.Ex(), 2), elem.Poly(elem.Ex(), 2), elem.Poly(elem.Ex()))
print(f)
print(f.get_full_derivative())

f1 = op.Mul(elem.Const(2), elem.Const(2), elem.Poly(elem.Ex()), elem.Const(3))
f1 = Simplifier(f1).mul_find_constants()
print(f1)

print(elem.Ex() + elem.Ex() - elem.Ex())