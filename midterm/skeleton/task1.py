from z3 import *

# make sure to use Z3 version 4.12.6.0!
if get_full_version() != "Z3 4.12.6.0":
    print("Incorrect Z3 version. Please install version 4.12.6.0")
    sys.exit(0)

# note: this function is used to check that the given `expr` holds (i.e., that
#   its negation is unsatisfiable); it uses the `push` and `pop` statements to
#   make sure that the different test cases are independent from each other.
def check(expr):
    s.push()
    s.add(Not(expr))
    print(s.check())
    s.pop()

s = Solver()
s.set(auto_config=False, mbqi=False)

# type of maps
MapSort = DeclareSort("Map")

# get function to read the value at the given key
get = Function("get", MapSort, IntSort(), IntSort())

# variables to use in quantifiers
m = Const("m", MapSort)
n = Const("n", MapSort)
x, y, z = Ints("x y z")

# note: do not change anything above this line in your solution
# -------------------------------------------------------------

# Task 1A: Creation

# TODO:
# create = ...
create = Function("create", IntSort(), MapSort)

ax0 = ForAll([x,y], get(create(x), y) == x, patterns=[get(create(x), y)])
s.add(ax0)

# tests (uncomment to check your solution)
# check(get(create(42), 7) == 42)

# Task 1B: Modification

# TODO:
# set = ...
i = Ints("i")
set = Function("set", MapSort, IntSort(), IntSort(), MapSort)
ax1 = ForAll([x, y, z], get(set(create(x), y, z), y) == z, patterns=[get(set(create(x), y, z))]) 
ax2 = ForAll([x, y, z], Not(y==i) ==> get(set(create(x), y, z), i) == x) 
s.add(ax1)
s.add(ax2)

# tests (uncomment to check your solution)
# check(get(set(create(42), 7, 72), 7) == 72)
# check(get(set(create(42), 7, 72), 1) == 42)

# Task 1C: Even-odd merge

# TODO:
# merge = ...

# tests (uncomment to check your solution)
#check(get(merge(create(42), create(72)), 10) == 42)
#check(get(merge(create(42), create(72)), 21) == 72)
