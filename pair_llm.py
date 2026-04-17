from z3 import *

# Declare sort
Pair = DeclareSort("Pair")

# Declare all functions
pair = Function("pair", IntSort(), IntSort(), Pair)
fst = Function("fst", Pair, IntSort())
snd = Function("snd", Pair, IntSort())

# Variables to be used in quantifiers and in constraints
x, y, z, a = Ints("x y z a")
p = Const("p", Pair)
p2 = Const("p2", Pair)

s = Solver()
s.set(auto_config=False, mbqi=False)

# Basic axioms: definitions of fst and snd.
# Trigger: pair(x, y)
ax_fst = ForAll([x, y], fst(pair(x, y)) == x, patterns=[pair(x, y)])
ax_snd = ForAll([x, y], snd(pair(x, y)) == y, patterns=[pair(x, y)])

# Extensionality axiom: A pair is strictly composed of its projections.
# Trigger: Requires both fst(p) and snd(p) to be present for instantiation.
ax_ext = ForAll([p], pair(fst(p), snd(p)) == p, patterns=[MultiPattern(fst(p), snd(p))])

s.add(ax_fst, ax_snd, ax_ext)

# --- Proofs ---

# 1. Base projection proof
F1 = fst(pair(1, 2)) == 1
s.push()
s.add(Not(F1))
print("Proof fst(pair(1, 2)) == 1:", s.check())  # Output: unsat (proved)
s.pop()

# 2. Injectivity test
F2 = Not(pair(1, 2) == pair(2, 3))
s.push()
s.add(Not(F2))
print("Proof pair(1, 2) != pair(2, 3):", s.check())  # Output: unsat (proved)
s.pop()

# 3. Extensionality implication test
F3 = Implies(And(fst(p) == fst(p2), snd(p) == snd(p2)), p == p2)
s.push()
s.add(Not(F3))
print("Proof Extensionality (p == p2):", s.check())  # Output: unsat (proved)
s.pop()
