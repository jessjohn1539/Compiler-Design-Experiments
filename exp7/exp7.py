import ply.lex as lex
import ply.yacc as yacc

# Lexer
tokens = (
    'NUMBER',
    'VARIABLE',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'MOD',
    'LPAREN',
    'RPAREN',
    'EQUALS',  # Added token for '='
)

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_MOD = r'%'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_EQUALS = r'='  # Definition for the '=' token

t_ignore = ' \t\n'

def t_VARIABLE(t):
    r'[a-zA-Z]+'
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

# Parser
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE', 'MOD'),
    ('left', 'LPAREN', 'RPAREN'),
)

def p_statement_assign(p):
    'statement : VARIABLE EQUALS expression'  # Modified rule to use EQUALS token
    print("\nEntered arithmetic expression is Valid\n")

def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression MOD expression'''
    pass

def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    pass

def p_expression_number(p):
    'expression : NUMBER'
    pass

def p_expression_variable(p):
    'expression : VARIABLE'
    pass

def p_error(p):
    raise SyntaxError("Entered arithmetic expression is Invalid")

# Main
parser = yacc.yacc()
if __name__ == "__main__":
    print("\nEnter Any Arithmetic Expression which can have operations Addition, Subtraction, Multiplication, Divison, Modulus and Round brackets:\n")
    while True:
        try:
            s = input()
        except EOFError:
            break
        if s:
            parser.parse(s)
