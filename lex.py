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
   'Int':'INT',
   'Float':'FLOAT',
   'Char':'CHAR',
   'String':'STRING',
   'var':'VAR',
   'true':'BOOL',
   'false':'BOOL'
}

literals = ['+','-','*','/','%','=','&','{','}','(',')','[',']',';',':','.',',','\'','\"','\\']

tokens = [
   'NUMBER',
   'DECIMAL',
   'STRINGLITERAL',
   'ID',
   'LT',
   'GT',
   'LTE',
   'GTE',
   'EQ',
   'NE',
   'INC',
   'DEC'

]+list(set(reserved.values()))

# Regular expression rules for simple tokens
t_LT=r'<'
t_GT=r'>'
t_LTE=r'<='
t_GTE=r'>='
t_EQ=r'=='
t_NE=r'!='
t_INC=r'\+\+'
t_DEC=r'--'

# Check for reserved words
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')
    if(t.type=='BOOL'):
    	t.value = True if t.value == 'true' else False    
    return t


def t_STRINGLITERAL(t):
	r'"([^\\\"]|\\.)*\"'
	t.value=t.value[1:len(t.value)-1]
	return t

def t_DECIMAL(t):
	r'(\d*\.?\d+e[+-]?\d+)|(\d*\.\d+)'
	t.value = float(t.value)
	return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_comments(t):
	r'((?s)/\*.*?\*/)|(//.*)'

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
data = '''int x = 40*50+(4/5)'''

# Give the lexer some input
lexer.input(data)

# Tokenize
for tok in lexer:# No more input
    print(tok)

