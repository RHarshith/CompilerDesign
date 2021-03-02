import ply.yacc as yacc
import lex
tokens=lex.tokens

def p_start(p):
	'''start : assign |
	| expr '''
	p[0]=p[1]

def p_assign(p):
    '''assign : ID '=' expr'''
    #vars(p[1]) = p[3]
    p[0] = ('ASSIGN',p[1],p[3])
    #print(vars(p))
    #print(p[1]);print(type(p[1]))
    #print(p[3]);print(type(p[3]))

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
    '''factor : DECIMAL
    | NUMBER'''
    p[0] = p[1]

def p_factor_expr(p):
     "factor : '(' expr ')'"
     p[0] = p[2]

def p_error(p):
     print("Syntax error in input!")

yacc.yacc()
data= " (3*4) + (5-6)"
t=yacc.parse(data)
print(t)

