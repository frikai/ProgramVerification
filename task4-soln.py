import sys
from z3 import *

# Initialise the Z3 solver, set flags for working with quantifiers.
if get_full_version() != "Z3 4.12.6.0":
  print("Incorrect Z3 version. Please install version 4.12.6.0")
  print("pip install z3-solver==4.12.6.0")
  sys.exit(1)
s = Solver()
s.set(auto_config=False, mbqi=False)

# Functions f and g, declared as functions from integers to integers.
f = Function("f", IntSort(), IntSort())
g = Function("g", IntSort(), IntSort())
h = Function("h", IntSort(), IntSort())

# Integer variables, usable in quantifiers and assertions.
a, b, c, d, e, x, y, z = Ints("a b c d e x y z")

# Function for task 4C.
q = Function("q", IntSort(), IntSort())
s.add( ForAll([x], q(x) == 3 * x * x + 2 * x - x * (2 * x + 20) - 100, patterns=[q(x)]) )

# TASK 4A
# --- add your solution here

s.add( ForAll([x, y], Implies(x < y, f(x) < f(y)), patterns=[MultiPattern(f(x), f(y))]) )
s.add( ForAll([x, y], Implies(x < y, g(x) < g(y)), patterns=[MultiPattern(g(x), g(y))]) )

# --- end solution

print(s.check())
s.push()

# TASK 4B
# --- add your solution here

s.add( a < b )
s.add( Not( f(g(a)) < f(g(b)) ) )

# Z3 prints "unsat"
# because the negation of the property that holds is
# unsatisfiable, i.e., there is no variable assignment
# that would violate the given property

# --- end solution

print(s.check())
s.pop()
s.push()

# TASK 4C
# --- add your solution here

m, = Ints("m")
s.add( q(m - 1) > q(m) )
s.add( q(m + 1) > q(m) )

s.check()
md = s.model()
print(f"at: {md.evaluate(m)}, minimum: {md.evaluate(q(m))}")

# --- end solution

print(s.check())
print(s.model())
s.pop()
