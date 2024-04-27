import re

# Regular expressions for token patterns
token_patterns = [
    ('IDENTIFIER', r'[a-zA-Z_][a-zA-Z0-9_]*'),
    ('INTEGER_LITERAL', r'\d+'),
    ('OPEN_CURLY_BRACE', r'\{'),
    ('END_CURLY_BRACE', r'\}'),
    ('SEMICOLON', r';'),
    ('PARENTHESIS', r'[()]'),
    ('STRING_LITERAL', r'"([^"\\]|\\.)*"'),
    ('WHITESPACE', r'\s+'),
]

# Function to tokenize input C code
def tokenize_c_code(code):
    tokens = []
    while code:
        match = None
        # Ignore preprocessor directives
        if code.startswith('#'):
            end_of_line = code.find('\n')
            if end_of_line == -1:
                break
            code = code[end_of_line:]
            continue
        for token_type, pattern in token_patterns:
            regex = re.compile(pattern)
            match = regex.match(code)
            if match:
                value = match.group(0)
                if token_type != 'WHITESPACE':
                    tokens.append((token_type, value))
                break
        if not match:
            raise ValueError('Invalid token: ' + code[0])
        code = code[len(match.group(0)):]
    return tokens

# Example input C code
input_code = """
#include <stdio.h>

int main() {
    printf("Hello, world!\n");
    return 0;
}
"""

# Tokenize the input code
tokens = tokenize_c_code(input_code)

# Print the tokens
for token in tokens:
    print(token)
