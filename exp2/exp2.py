with open('exp2.txt', 'r') as file:
    content = file.read()
    lines = content.split('\n')

variables = ['DS', 'DC']
counter = 1  # Initialize a counter
with open('symbol.txt', 'w') as output_file:
    for line in lines:
        for var in variables:
            if var in line:
                parts = line.split(var)
                if len(parts) == 2:
                    output_file.write(f" {counter}: {parts[0].strip()}\n")
                    counter += 1  # Increment the counter

literals = ['=']
ltcount = 1
with open('literals.txt', 'w') as output_file:
    for line in lines:
        for var in literals:
            if var in line:
                parts = line.split(var)
                if len(parts) == 2:
                    output_file.write(f" {ltcount}: {parts[1].strip()}\n")
                    ltcount += 1