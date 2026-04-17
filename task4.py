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

# TODO

# --- end solution

print(s.check())
s.push()

# TASK 4B
# --- add your solution here

# TODO: code

# TODO: comment - what was the output? why?

# --- end solution

print(s.check())
s.pop()
s.push()

# TASK 4C
# --- add your solution here

# TODO: code

# --- end solution

print(s.check())
print(s.model())
s.pop()
