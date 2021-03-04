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
    # if p[1][0] == 'ASSIGN' or p[1][0] == 'IF':
    p[0] = p[1]
    # elif p[1][0] == 'GT':
        # p[0] = ('BOOL', p[1])
    # else:
        # p[0] = ('BOOL', p[1])

def p_branch(p):
    '''branch : if branchif'''
    p[0] = (p[1], ) + tuple([i for i in p[2]]) if p[2] else (p[1],)


def p_branchif(p):
    '''branchif : elseif branchif
                | else
                | empty'''
    if len(p) > 2:
        # p[0] = ('ELSE', p[2])
        p[0] = p[1], p[2]
    elif len(p) == 2:
        p[0] = p[1]

def p_if(p):
    '''if : IF '(' condition ')' body
          | IF '(' condition ')' '{' body '}' '''
    p[0] = ('IF', p[3], p[6]) if len(p)>6 else ('IF', p[3], p[5])

def p_elseif(p):
    '''elseif : ELSE IF '(' condition ')' body
              | ELSE IF '(' condition ')' '{' body '}' '''
    # print(len(p), tuple(p))
    p[0] = ('ELSEIF', p[4], p[7]) if len(p)>7 else ('ELSEIF', p[4], p[6])
    
def p_else(p):
    '''else : ELSE body
            | ELSE '{' body '}' '''
    p[0] = ('ELSE', p[3]) if len(p) > 3 else ('ELSE', p[2])

def p_body(p):
    '''body : assign body
            | assign'''
    # print(len(p), 'as', (p[1], p[2]) if len(p) > 2 else (p[1],))
    p[0] = (p[1], p[2]) if len(p) > 2 else p[1]

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

def p_empty(p):
     'empty :'
     pass

def p_error(p):
     print("Syntax error in input!")

yacc.yacc()
data= '''if(1>5) {
    a=12564
    b=45
} else if(3==3) {
    d=846
} else {
    e=7
}
'''
# data = input()
t=yacc.parse(data)
print(t)
# print(lex.tokens)

('BOOL', (('IF', ('GT', 1, 5), (('ASSIGN', 's', 12564), 
                                (('ASSIGN', 'b', 45), ('ASSIGN', 'c', 456)))), ('ELSEIF', ('IF', ('GT', 5, 10), ('ASSIGN', 's', 489)), ('ELSEIF', ('IF', ('GT', 78, 7), ('ASSIGN', 's', 45)), None))))
