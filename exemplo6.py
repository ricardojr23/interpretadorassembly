import re

codigo_assembly = [
    "MOVE A,7",
    "MOVE B,5",
    "MOVE C,B",
    "CMP B,1",
    "JTRUE fim",
    "MOVE B,C",
    "MULT A,B",
    "SUBT B,1",
    "JUMP enquanto",
    "fim: HALT"
]

registradores = {"A": 0, "B": 0, "C": 0} # Inicializa os registradores com zero

# Expressão regular para separar as linhas em tokens
regex = re.compile(r"(\b\w+\b|[,\:])")

# Itera sobre cada linha do código assembly
i = 0
while i < len(codigo_assembly):
    # Aplica a expressão regular na linha
    tokens = regex.findall(codigo_assembly[i])
    
    # Verifica a instrução da linha e executa a ação correspondente
    if tokens[0] == "MOVE":
        if tokens[3] in registradores:
            registradores[tokens[1]] = registradores[tokens[3]]
        else:
            registradores[tokens[1]] = int(tokens[3])
    elif tokens[0] == "CMP":
        if registradores[tokens[1]] == int(tokens[3]):
            comp = 0
        elif registradores[tokens[1]] > int(tokens[3]):
            comp = 1
        else:
            comp = -1
    elif tokens[0] == "JTRUE":
        if comp == 0:
            # Procura pelo rótulo especificado e salta para a linha correspondente
            for j in range(len(codigo_assembly)):
                if codigo_assembly[j].startswith(tokens[1] + ":"):
                    i = j
                    break
    elif tokens[0] == "MULT":
        registradores[tokens[1]] *= registradores[tokens[3]]
    elif tokens[0] == "SUBT":
        registradores[tokens[1]] -= int(tokens[3])
    elif tokens[0] == "JUMP":
        # Procura pelo rótulo especificado e salta para a linha correspondente
        for j in range(len(codigo_assembly)):
            if codigo_assembly[j].startswith(tokens[1] + ":"):
                i = j
                break
    
    i += 1

# Exibe o valor final dos registradores
print(registradores)
