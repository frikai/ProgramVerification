from z3 import *

x, y = Ints('x y')
z = Const('z', IntSort())

s = Solver()

MySort = DeclareSort("MySort")
a = Const("a", MySort)
b = Const("b", MySort)

f = Function('f', IntSort(), IntSort())
g = Function('g', IntSort(), IntSort())

s.add( x > 0 )
s.add( f(x) == 3*x + 17 )
s.add( y == f(x) + 3 )
s.add( z == f(x+1) )
s.add( g(x) == f(x+2) )
s.add( a == b )

if s.check() == sat:
  print(s.model())