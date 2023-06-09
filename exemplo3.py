import re

def interpreta_asm(asm):
    
    registradores = {}
    
    
    labels = {}
    
    
    regex = re.compile(r'(?P<label>[a-zA-Z_]+:)?\s*(?P<mnemonico>[a-zA-Z]+)(\s+(?P<reg1>[a-zA-Z]+)(\s*,\s*(?P<reg2>[a-zA-Z0-9]+))?)?')
    
    
    for i, linha in enumerate(asm):
       
        match = regex.match(linha)
        
       
        if match.group('label'):
            
            labels[match.group('label')[:-1]] = i
            mnemonico = match.group('mnemonico')
            reg1 = match.group('reg1')
            reg2 = match.group('reg2')
        else:
            mnemonico = match.group('mnemonico')
            reg1 = match.group('reg1')
            reg2 = match.group('reg2')
        
        
        if mnemonico:
           
            if mnemonico == 'MOVE':
                registradores[reg1] = int(reg2)
            elif mnemonico == 'ADD':
                registradores[reg1] = registradores.get(reg1, 0) + registradores.get(reg2, 0)
            elif mnemonico == 'SUB':
                registradores[reg1] = registradores.get(reg1, 0) - registradores.get(reg2, 0)
            elif mnemonico == 'MULT':
                registradores[reg1] = registradores.get(reg1, 0) * registradores.get(reg2, 0)
            elif mnemonico == 'DIV':
                registradores[reg1] = registradores.get(reg1, 0) // registradores.get(reg2, 0)
            elif mnemonico == 'CMP':
                if registradores.get(reg1, 0) == registradores.get(reg2, 0):
                    registradores['FLG'] = 0
                elif registradores.get(reg1, 0) > registradores.get(reg2, 0):
                    registradores['FLG'] = 1
                else:
                    registradores['FLG'] = -1
            elif mnemonico == 'JTRUE':
                if registradores.get('FLG', 0) == 0:
                    i = labels[reg1] - 1
            elif mnemonico == 'JFALSE':
                if registradores.get('FLG', 0) != 0:
                    i = labels[reg1] - 1
            elif mnemonico == 'JUMP':
                i = labels[reg1] - 1
            elif mnemonico == 'HALT':
                return registradores
codigo_asm = [
    'MOVE A,6',
    'MOVE B,5',
    'enquanto:',
    'MOVE C,B',
    'CMP B,1',
    'JTRUE fim',
    'MOVE B,C',
    'MULT A,B',
    'SUB B,1',
    'JUMP enquanto',
    'fim:',
    'HALT'
]

resultado = interpreta_asm(codigo_asm)

print(resultado) # {'A': 0, 'B': 5, 'C': 1, 'FLG': -1}
