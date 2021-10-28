import dyex.functions.elementary as elem
#import dyex.functions.operator as op
#from dyex.tools.parser import Parser

'''
print("Welcome to dYeX. The easy derivative calculator")
funcStr = input("Please give me a function: \n>")

funcStr = Parser(funcStr)
'''

from dyex.functions.operator import *
from dyex.functions.elementary import *


x = Ex()
f = x**2 + 3*x + Const(5)

derivative = f.get_full_derivative()

g = x*x

y = Const(6)
z = Const(y)

print(f)
print(derivative)

print(g)

print(y)
print(z)