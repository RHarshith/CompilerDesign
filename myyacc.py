import ply.yacc as yacc
import mylex 
tokens=mylex.tokens
stmtnum=1
precedence = (
     ('left', '+', '-'),
     ('left', '*', '/'),
     )
def p_start(p):
	'''start : code
	'''
	p[0]=('start',p[1])

def p_code(p):
	'''code : stmt
	| stmt code
	| '{' code '}'  
	'''
	p[0]=tuple([i for i in p[1:]])

def p_stmt(p):
	'''stmt : declare ';'
	| expr ';'
	| ifelse
	| ';'
	'''
	global stmtnum
	p[0]=('stmt '+str(stmtnum),p[1])
	stmtnum+=1

def p_ifelse(p):
	'''ifelse : IF '(' expr ')' stmt
	'''
	p[0]=tuple([i for i in p[1:]])


def p_expr(p):
	'''expr : expr operator rval
	| '(' expr ')'
	| rval
	'''

	if(len(p)==2):
		p[0]=p[1]
	elif(len(p)==4):
		p[0]=(p[2],p[1],p[3])
	else:
		p[0]=(p[1],p[2],p[3])

def p_operator(p):
	'''operator : '+'
	| '-'
	| '*'
	| '/'
	| '%'
	'''
	p[0]=p[1]	

def p_declare(p):
	'''declare : VAR ID ':' type ASSIGN expr
	| VAR ID ':' type
	| ID ASSIGN expr
	'''
	ls=tuple([i for i in p[1:]])
	if(len(p)==7):
		s='define'
	elif(p[2]=='='):
		s='assign'
	else:
		s='declare'
	p[0]=(s,ls)

def p_type(p):
	'''type : INT
	| FLOAT
	| BOOL
	| CHAR
	| STRING    
	'''
	p[0]=('type',p[1])


def p_rval(p):
	'''rval : NUMBER
	| DECIMAL
	| BOOLEAN
	| STRINGLITERAL
	| ID
	'''
	p[0]=('rval',p[1])


def p_error(p):
    print("Syntax error in input!")

yacc.yacc()
data='''if(a+10)
a+10;
var a:Int=20+10*5/2;
'''
t=yacc.parse(data)
print(t)