def interpreta_asm(asm):
    
    registradores = {}
    
    labels = {}
    
    # percorre todas as linhas do código
    for i, linha in enumerate(asm):
        # divide a linha em tokens separados por espaços em branco
        tokens = linha.split()
        
        if tokens[0][-1] == ':':
            # se sim, adiciona o endereço da label no dicionário de labels
            labels[tokens[0][:-1]] = i
            tokens = tokens[1:]
        
        if len(tokens) > 0:
            
            # verifica qual é a instrução e executa a operação correspondente
            if mnemonico == 'MOVE':
                registradores[tokens[1]] = int(tokens[2])
            elif mnemonico == 'ADD':
                registradores[tokens[1]] = registradores.get(tokens[1], 0) + registradores.get(tokens[2], 0)
            elif mnemonico == 'SUB':
                registradores[tokens[1]] = registradores.get(tokens[1], 0) - registradores.get(tokens[2], 0)
            elif mnemonico == 'MULT':
                registradores[tokens[1]] = registradores.get(tokens[1], 0) * registradores.get(tokens[2], 0)
            elif mnemonico == 'DIV':
                registradores[tokens[1]] = registradores.get(tokens[1], 0) // registradores.get(tokens[2], 0)
            elif mnemonico == 'CMP':
                if registradores.get(tokens[1], 0) == registradores.get(tokens[2], 0):
                    registradores['FLG'] = 0
                elif registradores.get(tokens[1], 0) > registradores.get(tokens[2], 0):
                    registradores['FLG'] = 1
                else:
                    registradores['FLG'] = -1
            elif mnemonico == 'JTRUE':
                if registradores.get('FLG', 0) == 0:
                    i = labels[tokens[1]] - 1
            elif mnemonico == 'JFALSE':
                if registradores.get('FLG', 0) != 0:
                    i = labels[tokens[1]] - 1
            elif mnemonico == 'JUMP':
                i = labels[tokens[1]] - 1
            elif mnemonico == 'HALT':
                return registradores

codigo_asm = [
    'MOVE A,6',
    'MOVE B,5',
    'enquanto:MOVE C,B',
    'CMP B,1',
    'JTRUE fim',
    'MOVE B,C',
    'MULT A,B',
    'SUB B,1',
    'JUMP enquanto',
    'fim:HALT'
]

registradores = interpreta_asm(codigo_asm)
print(registradores)
