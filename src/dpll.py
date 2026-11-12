def custom_dpll(clausulas, atribuicao=None):
    if atribuicao is None:
        atribuicao = {}
        
    mudou = True
    while mudou:
        mudou = False
        novas_clausulas = []
        for c in clausulas:
            if any(atribuicao.get(abs(lit)) == (lit > 0) for lit in c):
                continue
            
            
            c_reduzida = [lit for lit in c if abs(lit) not in atribuicao]
            if len(c_reduzida) == 0:
                return None 
          
            if len(c_reduzida) == 1:
                lit = c_reduzida[0]
                atribuicao = atribuicao.copy()
                atribuicao[abs(lit)] = (lit > 0)
                mudou = True
            else:
                novas_clausulas.append(c_reduzida)
        clausulas = novas_clausulas

    if not clausulas:
        return atribuicao
      
    var = abs(min(clausulas, key=len)[0])
    for valor in [True, False]:
        nova_atrib = atribuicao.copy()
        nova_atrib[var] = valor
        resultado = custom_dpll(clausulas, nova_atrib)
        if resultado is not None:
            return resultado
            
    return None
