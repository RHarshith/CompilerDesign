import ply.yacc as yacc
import mylex
import sys
import re
l=-1
t=-1
def label():
	global l
	l+=1
	return 'L'+str(l)

def variable():
	global t
	t+=1
	return 't'+str(t)

pattern = re.compile(r'[a-zA-Z_][a-zA-Z_0-9]*') 

VarSize={
	'Int': 2,
	'Float': 4,
	'Char': 1,
	'String':None,
	'Bool': 1
}

tokens=mylex.tokens
stmtnum=1

lookup={}

data='''
var a:Int=10;
if(a+10>a+20)
{	a=(a+10)*20;
a=10+20;}
a=10+20;
'''
mylex.lexer.input(data)
for tok in mylex.lexer:# No more input
	lookup[tok.value]={'dtype':None,'value':None,'size':None,'scope':None,'declared':False,'referred':False, 'lineNo':tok.lineno}


print("\n\n----------------------------Lookup Table INITIALIZATION--------------------------\n\n")
for i in lookup:
	print(i,lookup[i])

print("\n\n------------------------------------------------------\n\n")

def p_start(p):
	'''start : code
	'''
	r=open('icg.txt','w')
	r.write(p[1])
	p[0]=p[1]
	r.close()

def p_code(p):
	'''code : stmt
	| stmt code  
	'''
	#p[0]=tuple([i for i in p[1:]])
	p[0]=p[1]+'\n'+p[2] if len(p)==3 else p[1]	

def p_stmt(p):
	'''stmt : declare ';'
	| ifelse
	| ';'
	'''
	if(p[1]!=';'):
		p[0]=p[1]
		

def p_ifelse(p):
	'''ifelse : IF '(' ifexpr ')' stmt
	| IF '(' ifexpr ')' '{' code '}'
	'''
	#p[0]=tuple([i for i in p[1:]])
	L=label()
	if(len(p)==6):
		p[0]=p[3]+'\n'+'ifFalse('+p[3].split('\n')[-1].split(' ')[0]+') goto '+L+'\n'+p[5]+'\n'+L+':'
	else:
		p[0]=p[3]+'\n'+'ifFalse('+p[3].split('\n')[-1].split(' ')[0]+') goto '+L+'\n'+p[6]+'\n'+L+':'

def p_ifexpr(p):
	'''ifexpr : expression LT expression
	| expression EQ expression
	| expression GT expression
	| expression GTE expression
	| expression LTE expression
	| expression NE expression
	| expression
	'''
	if(len(p)==2):
		p[0]=p[1]
	else:
		p[0]=p[1]+'\n'+p[3]+'\n'+variable()+' = '+p[1].split('\n')[-1].split(' ')[0]+' '+p[2]+' '+p[3].split('\n')[-1].split(' ')[0]

def p_expression_plus(p):
	'''expression : expression '+' term'''
	p[0] = p[1]+'\n'+p[3]+'\n'+variable()+' = '+p[1].split('\n')[-1].split(' ')[0]+' '+p[2]+' '+p[3].split('\n')[-1].split(' ')[0]
 
def p_expression_minus(p):
	'''expression : expression '-' term'''
	p[0] = p[1]+'\n'+p[3]+'\n'+variable()+' = '+p[1].split('\n')[-1].split(' ')[0]+' '+p[2]+' '+p[3].split('\n')[-1].split(' ')[0]
 
def p_expression_term(p):
	'''expression : term'''
	p[0] = p[1]
 
def p_term_times(p):
	'''term : term '*' factor'''
	p[0] = p[1]+'\n'+p[3]+'\n'+variable()+' = '+p[1].split('\n')[-1].split(' ')[0]+' '+p[2]+' '+p[3].split('\n')[-1].split(' ')[0]
 
def p_term_div(p):
	'''term : term '/' factor'''
	p[0] = p[1]+'\n'+p[3]+'\n'+variable()+' = '+p[1].split('\n')[-1].split(' ')[0]+' '+p[2]+' '+p[3].split('\n')[-1].split(' ')[0]
 
def p_term_factor(p):
	'''term : factor'''
	p[0] = p[1]
 
def p_factor_num(p):
	'''factor : rval'''
	p[0] = variable()+' = '+p[1]

 
def p_factor_expr(p):
	'''factor : '(' expression ')' '''
	p[0] = p[2]

def p_operator(p):
	'''operator : '+'
	| '-'
	| '*'
	| '/'
	'''
	p[0]=p[1]	

def p_declare(p):
	'''declare : VAR ID ':' type ASSIGN expression
	| VAR ID ':' type
	| ID ASSIGN expression
	'''
	
	
	if(len(p)==7):
		s='define'
		if(p[2] in lookup and lookup[p[2]]['declared']):
			print('error: ',p[2],' redeclared')
			#sys.exit()
		lookup[p[2]]['dtype']=p[4]
		lookup[p[2]]['value']=p[6]
		lookup[p[2]]['declared']=True
		lookup[p[2]]['size']=VarSize[p[4]]
		ls=p[6]+'\n'+p[2]+' = '+p[6].split('\n')[-1].split(' ')[0]	
	
	elif(p[2]=='='):
		s='assign'
		if(p[1] in lookup and not lookup[p[1]]['declared']):
			print('error: ',p[1],' not declared')
			#sys.exit()

		lookup[p[1]]['referred']=True
		lookup[p[1]]['value']=p[3]
		ls=p[3]+'\n'+p[1]+' = '+p[3].split('\n')[-1].split(' ')[0]
	else:
		s='declare'
		if(p[2] in lookup and lookup[p[2]]['declared']):
			print('error: ',p[2],' redeclared')
			#sys.exit()
		lookup[p[2]]['dtype']=p[4]
		lookup[p[2]]['declared']=True
	
	p[0]=ls

def p_type(p):
	'''type : INT
	| FLOAT
	| BOOL
	| CHAR
	| STRING    
	'''
	p[0]=p[1]


def p_rval(p):
	'''rval : NUMBER
	| DECIMAL
	| BOOLEAN
	| STRINGLITERAL
	| ID
	'''
	if(isinstance(p[1], str) and p[1].isidentifier()):
		if(p[1] in lookup and not lookup[p[1]]['declared']):
			print('error: ',p[1],' not declared')
			#sys.exit()
		if(p[1] in lookup):
			lookup[p[1]]['referred']=True		

	p[0]=str(p[1])


def p_error(p):
    print("Syntax error in input!!")

yacc.yacc()
t=yacc.parse(data)
print("\n\n----------------------------Lookup Table--------------------------\n\n")
for i in lookup:
	print(i,lookup[i])
print("\n\n------------------------------------------------------\n\n")
print("\n\n----------------------------SYNTAX TREE--------------------------\n\n")
print(t)
print("\n\n------------------------------------------------------\n\n")

