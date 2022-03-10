## From a directory  tree
# with general import
import Functions.Scope.lib.calculator
# With alias
import Functions.Scope.lib.calculator as calc

# Import only a function
from Functions.Scope.lib.calculator import add

# Import every function from module
from Functions.Scope.lib.calculator import *

a = 1
b = 2

x1 = Functions.Scope.lib.calculator.add(a, b)
x2 = calc.add(a,b)
x3 = add(a,b)
x4 = sub(a , b)
print(x1, x2, x3, x4)