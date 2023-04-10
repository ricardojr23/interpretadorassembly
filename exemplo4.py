def parse_assembly(assembly):
    program = []
    labels = {}

    for i, line in enumerate(assembly):
        tokens = line.strip().split(' ')
        mnemonic = tokens[0]

        # Check for label
        if ':' in mnemonic:
            label = mnemonic[:-1]
            labels[label] = i
            tokens.pop(0)
            mnemonic = tokens[0]

        # Parse parameters
        params = []
        for param in tokens[1:]:
            param = param.strip(',')
            try:
                param = int(param)
            except ValueError:
                pass
            params.append(param)

        # Add to program
        program.append((mnemonic, params))

    return program, labels

# Example usage
assembly = [
    "MOVE A,7",
    "MOVE B,14",
    "enquanto: MOVE C,B",
    "CMP B,1",
    "JTRUE fim",
    "MOVE B,C",
    "MULT A,B",
    "SUBT B,1",
    "JUMP enquanto",
    "fim: HALT"
]

program, labels = parse_assembly(assembly)
print("Program:")
for i, (mnemonic, params) in enumerate(program):
    print(f"{i:2d}: {mnemonic} {params}")
print("Labels:")
for label, address in labels.items():
    print(f"{label}: {address}")
