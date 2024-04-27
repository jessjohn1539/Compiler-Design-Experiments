import re

# Initialize MNT and MDT
MNT = [] # Macro Name Table
MDT = [] # Macro Definition Table

# Open input file and read contents
with open('macro.txt', 'r') as file:
    input_text = file.readlines()

# Process each line in input text
for i, line in enumerate(input_text):
    line = line.strip()
    # Check if line is a macro definition
    if line.startswith('MACRO'):
        macro_name = input_text[i+1].split()[0]
        MNT.append([macro_name, len(MDT)+1])
        MDT.append(input_text[i+1])
        for j in range(i+1, len(input_text)):
            if input_text[j].strip() == 'MEND':
                MDT.append(input_text[j])
                break
            MDT.append(input_text[j+1].replace('&ARG', '#'))
    # Check if line is a macro call
    elif ' ' in line:
        macro_call, arg_list = line.split(' ', 1)
        macro_name = macro_call.split()[0]
        # Get argument list as an array of strings
        arg_list = [arg.strip() for arg in arg_list.split(',')]
        # Find macro definition in MDT
        try:
            macro_def_index = MNT.index([macro_name, None])+1
            macro_def = MDT[macro_def_index:]
        except ValueError:
            continue

        # Replace argument placeholders with actual arguments
        for i, arg in enumerate(arg_list):
            macro_def = [re.sub(r'\b'+f'{i+1}'+r'\b', arg, instr) for instr in macro_def]
        # Print macro expansion
        print('\n'.join(macro_def))

# Print MNT
print('\nMacro Name Table')
print('-' * 40)
print('Index\tMacro name\tMDT Index')
for i, entry in enumerate(MNT):
    print(f'{i+1}\t{entry[0]}\t\t{entry[1]}')

# Print MDT
print('\nMacro Definition Table')
print('-' * 40)
print('Index\tMacro Definition')
for i, entry in enumerate(MDT):
    print(f'{i+1}\t{entry}')

# Note: The Argument List Array is handled within the macro expansion logic above.
