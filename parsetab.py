
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "ASSIGN BOOL BOOLEAN CHAR DEC DECIMAL DO ELSE EQ FLOAT FOR GT GTE ID IF INC INT LT LTE NE NEWLINE NUMBER STRING STRINGLITERAL VAR WHILEstart : code\n\tcode : stmt\n\t| stmt code  \n\tstmt : declare ';'\n\t| ifelse\n\t| ';'\n\tifelse : IF '(' ifexpr ')' stmt\n\t| IF '(' ifexpr ')' '{' code '}'\n\tifexpr : expression LT expression\n\t| expression EQ expression\n\t| expression GT expression\n\t| expression GTE expression\n\t| expression LTE expression\n\t| expression NE expression\n\t| expression\n\texpression : expression '+' termexpression : expression '-' termexpression : termterm : term '*' factorterm : term '/' factorterm : factorfactor : rvalfactor : '(' expression ')' operator : '+'\n\t| '-'\n\t| '*'\n\t| '/'\n\tdeclare : VAR ID ':' type ASSIGN expression\n\t| VAR ID ':' type\n\t| ID ASSIGN expression\n\ttype : INT\n\t| FLOAT\n\t| BOOL\n\t| CHAR\n\t| STRING    \n\trval : NUMBER\n\t| DECIMAL\n\t| BOOLEAN\n\t| STRINGLITERAL\n\t| ID\n\t"
    
_lr_action_items = {';':([0,3,4,5,6,11,16,17,18,19,20,22,23,24,25,28,29,30,31,32,33,39,47,48,49,50,51,52,53,60,62,],[5,5,11,-6,-5,-4,-40,-30,-18,-21,-22,-36,-37,-38,-39,-29,-31,-32,-33,-34,-35,5,-16,-17,-19,-20,-23,-7,5,-28,-8,]),'VAR':([0,3,5,6,11,39,52,53,62,],[7,7,-6,-5,-4,7,-7,7,-8,]),'ID':([0,3,5,6,7,11,13,14,21,34,35,36,37,39,40,41,42,43,44,45,46,52,53,62,],[8,8,-6,-5,12,-4,16,16,16,16,16,16,16,8,16,16,16,16,16,16,16,-7,8,-8,]),'IF':([0,3,5,6,11,39,52,53,62,],[9,9,-6,-5,-4,9,-7,9,-8,]),'$end':([1,2,3,5,6,10,11,52,62,],[0,-1,-2,-6,-5,-3,-4,-7,-8,]),'}':([3,5,6,10,11,52,61,62,],[-2,-6,-5,-3,-4,-7,62,-8,]),'ASSIGN':([8,28,29,30,31,32,33,],[13,46,-31,-32,-33,-34,-35,]),'(':([9,13,14,21,34,35,36,37,40,41,42,43,44,45,46,],[14,21,21,21,21,21,21,21,21,21,21,21,21,21,21,]),':':([12,],[15,]),'NUMBER':([13,14,21,34,35,36,37,40,41,42,43,44,45,46,],[22,22,22,22,22,22,22,22,22,22,22,22,22,22,]),'DECIMAL':([13,14,21,34,35,36,37,40,41,42,43,44,45,46,],[23,23,23,23,23,23,23,23,23,23,23,23,23,23,]),'BOOLEAN':([13,14,21,34,35,36,37,40,41,42,43,44,45,46,],[24,24,24,24,24,24,24,24,24,24,24,24,24,24,]),'STRINGLITERAL':([13,14,21,34,35,36,37,40,41,42,43,44,45,46,],[25,25,25,25,25,25,25,25,25,25,25,25,25,25,]),'INT':([15,],[29,]),'FLOAT':([15,],[30,]),'BOOL':([15,],[31,]),'CHAR':([15,],[32,]),'STRING':([15,],[33,]),'*':([16,18,19,20,22,23,24,25,47,48,49,50,51,],[-40,36,-21,-22,-36,-37,-38,-39,36,36,-19,-20,-23,]),'/':([16,18,19,20,22,23,24,25,47,48,49,50,51,],[-40,37,-21,-22,-36,-37,-38,-39,37,37,-19,-20,-23,]),'+':([16,17,18,19,20,22,23,24,25,27,38,47,48,49,50,51,54,55,56,57,58,59,60,],[-40,34,-18,-21,-22,-36,-37,-38,-39,34,34,-16,-17,-19,-20,-23,34,34,34,34,34,34,34,]),'-':([16,17,18,19,20,22,23,24,25,27,38,47,48,49,50,51,54,55,56,57,58,59,60,],[-40,35,-18,-21,-22,-36,-37,-38,-39,35,35,-16,-17,-19,-20,-23,35,35,35,35,35,35,35,]),'LT':([16,18,19,20,22,23,24,25,27,47,48,49,50,51,],[-40,-18,-21,-22,-36,-37,-38,-39,40,-16,-17,-19,-20,-23,]),'EQ':([16,18,19,20,22,23,24,25,27,47,48,49,50,51,],[-40,-18,-21,-22,-36,-37,-38,-39,41,-16,-17,-19,-20,-23,]),'GT':([16,18,19,20,22,23,24,25,27,47,48,49,50,51,],[-40,-18,-21,-22,-36,-37,-38,-39,42,-16,-17,-19,-20,-23,]),'GTE':([16,18,19,20,22,23,24,25,27,47,48,49,50,51,],[-40,-18,-21,-22,-36,-37,-38,-39,43,-16,-17,-19,-20,-23,]),'LTE':([16,18,19,20,22,23,24,25,27,47,48,49,50,51,],[-40,-18,-21,-22,-36,-37,-38,-39,44,-16,-17,-19,-20,-23,]),'NE':([16,18,19,20,22,23,24,25,27,47,48,49,50,51,],[-40,-18,-21,-22,-36,-37,-38,-39,45,-16,-17,-19,-20,-23,]),')':([16,18,19,20,22,23,24,25,26,27,38,47,48,49,50,51,54,55,56,57,58,59,],[-40,-18,-21,-22,-36,-37,-38,-39,39,-15,51,-16,-17,-19,-20,-23,-9,-10,-11,-12,-13,-14,]),'{':([39,],[53,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'start':([0,],[1,]),'code':([0,3,53,],[2,10,61,]),'stmt':([0,3,39,53,],[3,3,52,3,]),'declare':([0,3,39,53,],[4,4,4,4,]),'ifelse':([0,3,39,53,],[6,6,6,6,]),'expression':([13,14,21,40,41,42,43,44,45,46,],[17,27,38,54,55,56,57,58,59,60,]),'term':([13,14,21,34,35,40,41,42,43,44,45,46,],[18,18,18,47,48,18,18,18,18,18,18,18,]),'factor':([13,14,21,34,35,36,37,40,41,42,43,44,45,46,],[19,19,19,19,19,49,50,19,19,19,19,19,19,19,]),'rval':([13,14,21,34,35,36,37,40,41,42,43,44,45,46,],[20,20,20,20,20,20,20,20,20,20,20,20,20,20,]),'ifexpr':([14,],[26,]),'type':([15,],[28,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start","S'",1,None,None,None),
  ('start -> code','start',1,'p_start','myyacc.py',47),
  ('code -> stmt','code',1,'p_code','myyacc.py',55),
  ('code -> stmt code','code',2,'p_code','myyacc.py',56),
  ('stmt -> declare ;','stmt',2,'p_stmt','myyacc.py',62),
  ('stmt -> ifelse','stmt',1,'p_stmt','myyacc.py',63),
  ('stmt -> ;','stmt',1,'p_stmt','myyacc.py',64),
  ('ifelse -> IF ( ifexpr ) stmt','ifelse',5,'p_ifelse','myyacc.py',71),
  ('ifelse -> IF ( ifexpr ) { code }','ifelse',7,'p_ifelse','myyacc.py',72),
  ('ifexpr -> expression LT expression','ifexpr',3,'p_ifexpr','myyacc.py',82),
  ('ifexpr -> expression EQ expression','ifexpr',3,'p_ifexpr','myyacc.py',83),
  ('ifexpr -> expression GT expression','ifexpr',3,'p_ifexpr','myyacc.py',84),
  ('ifexpr -> expression GTE expression','ifexpr',3,'p_ifexpr','myyacc.py',85),
  ('ifexpr -> expression LTE expression','ifexpr',3,'p_ifexpr','myyacc.py',86),
  ('ifexpr -> expression NE expression','ifexpr',3,'p_ifexpr','myyacc.py',87),
  ('ifexpr -> expression','ifexpr',1,'p_ifexpr','myyacc.py',88),
  ('expression -> expression + term','expression',3,'p_expression_plus','myyacc.py',96),
  ('expression -> expression - term','expression',3,'p_expression_minus','myyacc.py',100),
  ('expression -> term','expression',1,'p_expression_term','myyacc.py',104),
  ('term -> term * factor','term',3,'p_term_times','myyacc.py',108),
  ('term -> term / factor','term',3,'p_term_div','myyacc.py',112),
  ('term -> factor','term',1,'p_term_factor','myyacc.py',116),
  ('factor -> rval','factor',1,'p_factor_num','myyacc.py',120),
  ('factor -> ( expression )','factor',3,'p_factor_expr','myyacc.py',125),
  ('operator -> +','operator',1,'p_operator','myyacc.py',129),
  ('operator -> -','operator',1,'p_operator','myyacc.py',130),
  ('operator -> *','operator',1,'p_operator','myyacc.py',131),
  ('operator -> /','operator',1,'p_operator','myyacc.py',132),
  ('declare -> VAR ID : type ASSIGN expression','declare',6,'p_declare','myyacc.py',137),
  ('declare -> VAR ID : type','declare',4,'p_declare','myyacc.py',138),
  ('declare -> ID ASSIGN expression','declare',3,'p_declare','myyacc.py',139),
  ('type -> INT','type',1,'p_type','myyacc.py',175),
  ('type -> FLOAT','type',1,'p_type','myyacc.py',176),
  ('type -> BOOL','type',1,'p_type','myyacc.py',177),
  ('type -> CHAR','type',1,'p_type','myyacc.py',178),
  ('type -> STRING','type',1,'p_type','myyacc.py',179),
  ('rval -> NUMBER','rval',1,'p_rval','myyacc.py',185),
  ('rval -> DECIMAL','rval',1,'p_rval','myyacc.py',186),
  ('rval -> BOOLEAN','rval',1,'p_rval','myyacc.py',187),
  ('rval -> STRINGLITERAL','rval',1,'p_rval','myyacc.py',188),
  ('rval -> ID','rval',1,'p_rval','myyacc.py',189),
]
