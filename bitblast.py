class CNF:
    def __init__(self):
        self.clausulas = []
        
    def add_clause(self, clause):
        self.clausulas.append(clause)

def var_id(r, c, v, n):
    """Mapeia coordenadas para um ID único de variável booleana."""
    return r * (n * n) + c * n + v

def build_cnf(n, given, less):
    cnf = CNF()
    
    for r in range(n):
        for c in range(n):
            cnf.add_clause([var_id(r, c, v, n) for v in range(1, n + 1)])
            for v1 in range(1, n + 1):
                for v2 in range(v1 + 1, n + 1):
                    cnf.add_clause([-var_id(r, c, v1, n), -var_id(r, c, v2, n)])

    for i in range(n):
        for v in range(1, n + 1):
            for j1 in range(n):
                for j2 in range(j1 + 1, n):
                    cnf.add_clause([-var_id(i, j1, v, n), -var_id(i, j2, v, n)]) # Linha
                    cnf.add_clause([-var_id(j1, i, v, n), -var_id(j2, i, v, n)]) # Coluna

    for r, c, val in given:
        cnf.add_clause([var_id(r, c, val, n)])

    for r1, c1, r2, c2 in less:
        for v1 in range(1, n + 1):
            for v2 in range(1, n + 1):
                if v1 >= v2:
                    cnf.add_clause([-var_id(r1, c1, v1, n), -var_id(r2, c2, v2, n)])
                    
    return cnf
