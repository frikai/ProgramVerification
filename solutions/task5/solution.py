from z3 import *

ROWS = 9
COLS = 9

# ========================================
# ================ TASK 1 ================
# ========================================

# Input:
#   - "puzzle" is a 9-tuple of 9-tuples of digits (0-9). 0 means empty, i.e. a
#     square that is NOT pre-filled. "puzzle[row][col]" refers to the square in
#     row "row", column "col" (counting from the top starting at 0).
#
# Output:
#   - A 9-tuple of 9-tuples of digits (1-9).
def solve(puzzle):
  return solve_base(puzzle)

# ========================================
# ================ TASK 2 ================
# ========================================

# Input:
#   - Same as for Task 1.
#
# Output:
#   - A list of 9-tuples of 9-tuples of digits (1-9).
def solve_all(puzzle):
  return solve_base(puzzle, True)

# ========================================
# ================ TASK 3 ================
# ========================================

# Input:
#   - "puzzle" is the same as for Task 1.
#   - "jigsaws" is a list of jigsaw pieces. Each jigsaw piece is a list of
#     coordinate tuples "(row, col)" representing which coordinates belong
#     to that jigsaw piece.
#
# Output:
#   - A 9-tuple of 9-tuples of digits (1-9).
def solve_jigsaw(puzzle, jigsaws):
  return solve_base(puzzle, False, jigsaws)

def solve_base(puzzle, find_all = False, jigsaws = None):
  s = Solver()

  # matrix of Int variables X[row][col]
  X = [ [ Int("square_%s_%s" % (row, col)) for col in range(COLS) ] for row in range(ROWS) ]

  # constraint: pre-filled squares
  for row in range(ROWS):
    for col in range(COLS):
      if puzzle[row][col] != 0:
        s.add(X[row][col] == puzzle[row][col])

  # constraint: each cell contains a digit between 1 and 9
  for row in range(ROWS):
    for col in range(COLS):
      # X[row][col] is already declared as an Int, so we only add bounds
      s.add(1 <= X[row][col]     )
      s.add(     X[row][col] <= 9)

  # constraint: each row contains every digit at most once
  for row in range(ROWS):
    s.add(Distinct(X[row]))

  # constraint: each column contains every digit at most once
  for col in range(COLS):
    # collect the variables representing this column
    column_vars = [ X[row][col] for row in range(ROWS) ]
    s.add(Distinct(column_vars))

  if jigsaws:
    # constraint: each jigsaw piece contains every digit at most once
    for piece in jigsaws:
      jigsaw_vars = [ X[row][col] for (row, col) in piece ]
      s.add(Distinct(jigsaw_vars))
  else:
    # constraint: each 3 x 3 square contains every digit at most once
    for square_y in range(3):
      for square_x in range(3):
        # collect the variables representing this 3 x 3 square
        square_vars = [ X[square_y * 3 + inner_y][square_x * 3 + inner_x]
                          for inner_y in range(3)
                          for inner_x in range(3) ]
        s.add(Distinct(square_vars))

  if find_all:
    solutions = []
    while s.check() == sat:
      m = s.model()
      solution = [ [ m.evaluate(X[row][col]) for col in range(COLS) ] for row in range(ROWS) ]
      solutions.append(tuple([ tuple(solution[row]) for row in range(ROWS) ]))
      ineqs = []
      for row in range(ROWS):
        for col in range(COLS):
          ineqs.append(X[row][col] != solution[row][col])
      s.add(Or(ineqs))
    return solutions

  # can Z3 find a solution for the given constraints?
  if s.check() == sat:
    # if so, fetch the model
    m = s.model()
    # and check what the variables are set to in that model
    solution = [ [ m.evaluate(X[row][col]) for col in range(COLS) ] for row in range(ROWS) ]
    # then print the solved grid!
    #print_matrix(solution)
    return tuple([ tuple(solution[row]) for row in range(ROWS) ])
  else:
    print("no solution!")
    return None
