import ast

# Initialization
MOT = {
    "MOVEM": 1,
    "MOVER": 2,
    "ADD": 3,
    "SUB": 4,
    "MUL": 5,
    "DIV": 6,
    "BC": 7,
    "COMP": 8,
    "READ": 9,
    "PRINT": 10,
}
POT = {
    "START": 1,
    "END": 2,
    "EQU": 3,
    "ORIGIN": 4,
    "LTORG": 5,
}
DL = {
    "DS": 1,
    "DC": 2,
}
REG = {
    "AREG": 1,
    "BREG": 2,
    "CREG": 3,
    "DREG": 4,
}
ic = []
SYMTAB = []
LITTAB = []
POOLTAB = []

# Initialization complete
# Take input program
with open("intermediateCode.txt", "r") as f:
    temp = f.readlines()
    for line in temp:
        ic.append(ast.literal_eval(line))

with open("tables.txt", "r") as f:
    temp = f.readlines()
    sym = False
    lit = False
    pool = False
    for line in temp:
        line = line.strip().upper()
        print(f"{line}")  # Debugging line
        if line == "SYMBOL TABLE":
            sym = True
            lit = False
            pool = False
            continue
        elif line == "LITERAL TABLE":
            lit = True
            sym = False
            pool = False
            continue
        elif line == "POOL TABLE":
            pool = True
            sym = False
            lit = False
            continue
        elif sym and line:  # Check if line is not empty
            try:
                SYMTAB.append(ast.literal_eval(line))
            except SyntaxError as e:
                print(f"Error evaluating line: {line}")
                print(f"Error: {e}")
        elif lit and line:  # Check if line is not empty
            try:
                LITTAB.append(ast.literal_eval(line))
            except SyntaxError as e:
                print(f"Error evaluating line: {line}")
                print(f"Error: {e}")
        elif pool and line:  # Check if line is not empty
            try:
                POOLTAB.append(ast.literal_eval(line))
            except SyntaxError as e:
                print(f"Error evaluating line: {line}")
                print(f"Error: {e}")

print("Input taken")

# Pass 2
print("Starting Pass 2")
mc = []
for record in ic:
    if record[0] == "":  # Skip the START statement
        continue
    if record[1][0] != "(":  # Skip the EQU & ORIGIN statements
        continue
    statement = (
        record[1].replace("(", "").replace(")", "").split(" ")
    )  # Split statement into statement type and its value
    operand = (
        record[3].replace("(", "").replace(")", "").split(" ")
    )  # Split operand 2 into literal/ symbol type and its value
    if len(operand) > 1:  # if operand is a value, skip
        record.pop(3)
    if operand[0] == "S,":
        index = int(operand[1]) - 1
        if index < len(SYMTAB):  # Check if the index is within the valid range
            record.append(SYMTAB[index][-1])  # Find address location
        else:
            print(f"Error: Index {index} out of range for SYMTAB.")
    elif operand[0] == "L,":
        index = int(operand[1]) - 1
        if index < len(LITTAB):  # Check if the index is within the valid range
            record.append(LITTAB[index][-1])  # Find address location
        else:
            print(f"Error: Index {index} out of range for LITTAB.")

    # Ensure record has at least 4 elements before accessing record[3]
    if len(record) >= 4:
        mc.append(
            [
                f"{record[0]}+",
                statement[1] if statement[0] == "IS," else "",
                record[2],
                record[3],
            ]
        )
    else:
        print(
            f"Error: Record does not have enough elements. Expected at least 4, found {len(record)}."
        )

# Example of parsing an instruction and its operands
for record in ic:
    instruction = record[0]
    operand1 = record[1]
    operand2 = record[2]
    # Process operands and generate machine code
    # This is a simplified example; your actual logic might be more complex
    mc_line = [instruction, operand1, operand2]
    mc.append(mc_line)

# Example of writing machine code to a file
with open("machineCode.txt", "w") as f:
    for line in mc:
        f.write(f"{line}\n")

print("Pass 2 Done")
