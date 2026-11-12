# Futoshiki SAT Solver: DPLL & Bit-Blasting

Este repositório contém a modelação e resolução formal do puzzle lógico Futoshiki ($5 \times 5$) através da sua redução a um Problema de Satisfação Booleana (SAT). O projeto contrasta uma implementação construída de raiz (gerador CNF + Algoritmo DPLL) com o *pipeline* industrial do Z3 Theorem Prover.

Projeto desenvolvido no âmbito da unidade curricular de **Fiabilidade e Verificação Formal** do Mestrado em Engenharia Informática.

## Sobre o Projeto

O Futoshiki é um puzzle japonês onde uma grelha $N \times N$ deve ser preenchida com números de $1$ a $N$, garantindo que não há repetições nas linhas e colunas, e respeitando um conjunto de pistas numéricas e desigualdades ($<$ ou $>$) pré-definidas.

Em vez de utilizar abordagens aritméticas tradicionais, este projeto foca-se na **proposicionalização (*Bit-Blasting*)**:
1. O tabuleiro e as suas regras matemáticas são convertidos num vasto conjunto de cláusulas lógicas (CNF).
2. O algoritmo DPLL (*Davis-Putnam-Logemann-Loveland*) processa a propagação unitária e o *backtracking* para encontrar a única solução satisfazível.
3. O resultado é validado lado a lado com o Z3 utilizando explicitamente a tática de abstração em bits (`Then('simplify', 'solve-eqs', 'bit-blast', 'sat')`).

## Arquitetura e Ficheiros

A base de código foi desenhada de forma estritamente modular, separando a definição das regras, a conversão lógica e o motor computacional:

* **`puzzle.py`**: Define o estado inicial da instância do Futoshiki ($5 \times 5$), incluindo as restrições fixas (`GIVEN`) e as relações de desigualdade (`LESS`).
* **`bitblast.py`**: Motor de conversão. Traduz as regras do jogo e do domínio finito para variáveis booleanas tridimensionais (linha, coluna, valor) e gera a Forma Normal Conjuntiva (CNF).
* **`dpll.py`**: Implementação recursiva do algoritmo DPLL, encarregue de processar as cláusulas CNF através de propagação unitária e decisões lógicas.
* **`z3_check.py`**: Script de validação que invoca o motor SAT/SMT do Z3, modelando as células como `BitVec(8)` para forçar o *bit-blasting* interno.
* **`main.py`**: Orquestrador que executa ambas as abordagens (Custom DPLL vs Z3), cronometra a performance de cada uma e valida a correspondência dos resultados.

## Instalação e Execução

### Pré-requisitos
O motor customizado (DPLL/CNF) utiliza apenas Python *vanilla*. A única dependência externa exigida é o motor de validação:

```bash
pip install z3-solver