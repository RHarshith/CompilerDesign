import ply.yacc as yacc
import lex
tokens=lex.tokens

RELATIONAL = {
    '<': 'LT',
    '>': 'GT',
    '<=': 'LTE',
    '>=': 'GTE',
    '==': 'EQ',
    '!=': 'NE',
}

def p_start(p):
    '''start : assign
              | expr
              | condition
              | branch'''
    if p[1][0] == 'ASSIGN' or p[1][0] == 'IF':
        p[0] = p[1]
    elif p[1][0] == 'GT':
        p[0] = ('BOOL', p[1])
    else:
        p[0] = ('BOOL', p[1])

def p_branch(p):
    '''branch : IF '(' condition ')' body
              | IF '(' condition ')' '{' body '}' '''
    p[0] = ('IF', p[3])

def p_body(p):
    '''body : assign'''

def p_assign(p):
    '''assign : ID ASSIGN expr'''
    p[0] = ('ASSIGN',p[1],p[3])


def p_condition(p):
    '''condition : expr GT expr
                 | expr LT expr
                 | expr LTE expr
                 | expr GTE expr
                 | expr EQ expr
                 | expr NE expr'''
    p[0] = (RELATIONAL[p[2]], p[1], p[3])


def p_expr_plus(p):
    '''expr : expr '+' term'''
    #p[0] = p[1] + p[3]
    p[0] = ('+',p[1],p[3])

def p_expr_minus(p):
    '''expr : expr '-' term'''
    #p[0] = p[1] + p[3]
    p[0] = ('-',p[1],p[3])

def p_expr_term(p):
    'expr : term'
    p[0]=p[1]


def p_term_mul(p):
    '''term : term '*' factor'''
    #p[0] = p[1] * p[3]
    p[0] = ('*',p[1],p[3])

def p_term_div(p):
    '''term : term '/' factor'''
    #p[0] = p[1] * p[3]
    p[0] = ('/',p[1],p[3])

def p_term_factor(p):
    '''term : factor'''
    #p[0] = p[1]
    p[0] = p[1]

def p_factor(p):
    '''factor : NUMBER'''
    p[0] = p[1]

def p_factor_expr(p):
     "factor : '(' expr ')'"
     p[0] = p[2]


def p_error(p):
     print("Syntax error in input!")

yacc.yacc()
data= '''if(1>4) {
    a=5
}   '''
# data = input()
t=yacc.parse(data)
print(t)
# print(lex.tokens)