from functions.elementary.polynomial import Const, Poly, Ex

squa = Poly(Ex(), 2)
dydx1 = squa.get_full_derivative()

cube = Poly(Ex(), 3)
dydx2 = cube.get_full_derivative()

sqrt = Poly(Ex(), 1./2)
dydx3 = sqrt.get_full_derivative()

inv = Poly(Ex(), -1)
dydx4 = inv.get_full_derivative()

print(f'{squa} has a derivative of {dydx1}')
print(f'{cube} has a derivative of {dydx2}')
print(f'{sqrt} has a derivative of {dydx3}')
print(f'{inv} has a derivative of {dydx4}')