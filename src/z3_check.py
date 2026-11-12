from z3 import *

def resolver_com_z3(n, given, less):
    solver = Then('simplify', 'solve-eqs', 'bit-blast', 'sat').solver()
    grid = [[BitVec(f"cell_{r}_{c}", 8) for c in range(n)] for r in range(n)]

    for r in range(n):
        for c in range(n):
            solver.add(And(grid[r][c] >= 1, grid[r][c] <= n))
            
    for i in range(n):
        for j1 in range(n):
            for j2 in range(j1 + 1, n):
                solver.add(grid[i][j1] != grid[i][j2])
                solver.add(grid[j1][i] != grid[j2][i])

    for r, c, val in given:
        solver.add(grid[r][c] == val)

    for r1, c1, r2, c2 in less:
        solver.add(grid[r1][c1] < grid[r2][c2])

    if solver.check() == sat:
        model = solver.model()
        return [[model[grid[r][c]].as_long() for c in range(n)] for r in range(n)]
    return None
