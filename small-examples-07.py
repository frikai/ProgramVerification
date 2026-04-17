from z3 import *

x, y = Bools('x y')

s = Solver()

s.add( Implies(x, y) )
s.add( Implies(y, x) )

print( s.check() )  # sat
print( s.model() )

s.add( x )

print( s.check() )  # sat
print( s.model() )

s.add( Not(x) )

print( s.check() )  # unsat
print( s.model() )  # exception