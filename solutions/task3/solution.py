from z3 import *

# Make sure to use Z3 version 4.12.6.0!!

s = Solver()
s.set(auto_config=False, mbqi=False)

f = Function('f', IntSort(), IntSort())
fp = Function('fp', IntSort(), IntSort())
g = Function('g', IntSort(), IntSort(), IntSort())
h = Function('h', IntSort(), IntSort())
m = Function('m', IntSort(), IntSort())

x, y = Ints('x y')

s.add(f(1) == 1)
#s.add(fp(3) > 0)
#s.add(f(2) >= 1)
#s.add(h(-1) == 3)
#s.add(g(4, 4) == 0)
#s.add(m(8) > 0)

#s.add(ForAll([x], f(x) == fp(x + 1), patterns=[f(x)]))
#s.add(ForAll([x], ForAll([y], g(x, y) >= x + y, patterns=[g(x, y)]), patterns=[f(x)]))

s.add(ForAll([y], And(fp(y) != f(y)), patterns=[MultiPattern(m(y), f(y))]))
s.add(ForAll([y], fp(y) == f(y), patterns=[f(y)]))
#s.add(ForAll([x], fp(h(x)) == h(x), patterns=[fp(h(x))]))

print(s.check())  # unknown

s.add(g(2, 2) == 0)

print(s.check())  # unsat
