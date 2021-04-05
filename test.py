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
	| ASSIGN
	| EQ
	| NE
	| GTE
	| LTE
	| GT
	| LT
	'''
	p[0]=p[1]