# ------------------------------------------------------------
# calclex.py
#
# tokenizer for a simple expression evaluator for
# numbers and +,-,*,/
# ------------------------------------------------------------
import ply.lex as lex

# List of token names.   This is always required
reserved = {
   'if' : 'IF',
   'else' : 'ELSE',
   'while' : 'WHILE',
   'for':'FOR',
   'do':'DO',
   'int':'INTEGER',
   'float':'FLOAT',
   'char':'CHAR',
   'var':'VAR'
}
literals = ['+','-','{','}','(',')','[',']',';',':','=','?',',','%','*','&']
tokens = [
   'NUMBER',
   'ID',
   'LT',
   'GT',
   'LTE',
   'GTE',
   'EQ',
   'NE',
   'INC',
   'DEC'

]+list(reserved.values())

# Regular expression rules for simple tokens
t_LT=r'<'
t_GT=r'>'
t_LTE=r'<='
t_GTE=r'>='
t_EQ=r'=='
t_NE=r'!='
t_INC=r'\+\+'
t_DEC=r'--'


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t
# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()
# Test it out
data = '''
for(int i=0;i<=10;i++)
{
	if(i==0)
	{
		int j=0;
		while(j<5):
			j+=1
	}
	else
	{
		215.37+E-32;`
	}
}
'''

# Give the lexer some input
lexer.input(data)

# Tokenize
for tok in lexer:# No more input
    print(tok)

