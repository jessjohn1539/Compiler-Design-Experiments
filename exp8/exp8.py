import ply.lex as lex
import ply.yacc as yacc

tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
)

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'

t_ignore = ' \t\n'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
)

def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = p[1] + p[3]
    print("+", end=' ')

def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = p[1] - p[3]
    print("-", end=' ')

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_times(p):
    'term : term TIMES factor'
    p[0] = p[1] * p[3]
    print("*", end=' ')

def p_term_divide(p):
    'term : term DIVIDE factor'
    p[0] = p[1] / p[3]
    print("/", end=' ')

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_number(p):
    'factor : NUMBER'
    p[0] = p[1]
    print(p[1], end=' ')

def p_factor_group(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]

def p_error(p):
    print("Syntax error in input!")

parser = yacc.yacc()

def infix_to_postfix(infix_expr):
    result = parser.parse(infix_expr, lexer=lexer)
    return result

if __name__ == "__main__":
    while True:
        try:
            infix_expr = input("\nEnter infix expression => ")
            if infix_expr == '':  # Exit on empty input
                break
            result = infix_to_postfix(infix_expr)
        except Exception as e:
            print("Error:", e)
