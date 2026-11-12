import time
from puzzle import N, GIVEN, LESS
from bitblast import build_cnf, var_id
from dpll import custom_dpll
from z3_check import resolver_com_z3

def imprimir_grelha(grelha):
    for linha in grelha:
        print(linha)

def main():
    print("   FUTOSHIKI: Z3 vs DPLL/CNF       ")
    
    inicio_z3 = time.time()
    solucao_z3 = resolver_com_z3(N, GIVEN, LESS)
    tempo_z3 = time.time() - inicio_z3

    inicio_cnf = time.time()
    cnf = build_cnf(N, GIVEN, LESS)
    tempo_cnf = time.time() - inicio_cnf
    
    inicio_dpll = time.time()
    modelo = custom_dpll(cnf.clausulas)
    tempo_dpll = time.time() - inicio_dpll

    solucao_dpll = None
    if modelo:
        solucao_dpll = [[0]*N for _ in range(N)]
        for r in range(N):
            for c in range(N):
                for v in range(1, N + 1):
                    if modelo.get(var_id(r, c, v, N), False):
                        solucao_dpll[r][c] = v

    print("Tabela:")
    print(f"Z3 Solver Total:       {tempo_z3:.4f} seg")
    print(f"Construção CNF:  {tempo_cnf:.4f} seg")
    print(f"DPLL Execução:   {tempo_dpll:.4f} seg")
    print(f"Total:           {tempo_cnf + tempo_dpll:.4f} seg\n")
    
    print("Resultado")
    if solucao_z3 and solucao_dpll and solucao_z3 == solucao_dpll:
        print("DPLL gerou exatamente a mesma solução que o Z3.\n")
        imprimir_grelha(solucao_dpll)
    else:
        print("As soluções não coincidem ou não têm solução.")

if __name__ == "__main__":
    main()
