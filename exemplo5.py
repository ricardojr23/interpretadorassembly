import re

def interpretar(codigo):
    registradores = {'A': 0, 'B': 0, 'C': 0}
    indice = 0

    while indice < len(codigo):
        linha = codigo[indice]
        instrucao = re.findall(r'(\w+)\s+([A-C]),(\d+|[A-C])', linha)
        if not instrucao:
            print('Comando inválido: ' + linha)
            break
        operando1 = instrucao[0][1]
        
        if instrucao[0][0] == 'MOVE':
            operando2 = instrucao[0][2]
            registradores[operando1] = int(operando2) if operando2.isdigit() else registradores[operando2]
            
            
        elif instrucao[0][0] == 'CMP':
            operando2 = instrucao[0][2]
            if registradores[operando1] == int(operando2):
                indice += 1
            else:
                indice += 2
                
                
        elif instrucao[0][0] == 'JTRUE':
            operando2 = instrucao[0][2]
            operando2_valor = int(operando2) if operando2.isdigit() else registradores[operando2]
            if registradores['B'] == operando2_valor:
                indice += 1
            else:
                indice += 2
        elif instrucao[0][0] == 'MULT':
            operando2 = instrucao[0][2]
            registradores[operando1] *= registradores[operando2]
        elif instrucao[0][0] == 'SUBT':
            operando2 = instrucao[0][2]
            registradores[operando1] -= int(operando2) if operando2.isdigit() else registradores[operando2]
        elif instrucao[0][0] == 'JUMP':
            operando2 = instrucao[0][2]
            try:
                indice = codigo.index("MOVE C,"+operando2)
            except ValueError:
                print('Erro: label ' + operando2 + ' não encontrada')
                break
        elif instrucao[0][0] == 'HALT':
            break
        else:
            print('Instrução inválida: ' + linha)
            break
        indice += 1

    print(registradores)


codigo = ['MOVE A,11',
          'MOVE B,5', 
          'MOVE C,B', 
          'CMP B,1',
          'JTRUE fim', 
          'MOVE B,C',
          'MULT A,B', 
          'SUBT B,1',
          'JUMP enquanto', 
          'fim: HALT']

interpretar(codigo)
