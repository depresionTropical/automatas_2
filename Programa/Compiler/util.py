import re

identifier = r'^_[A-Za-z]+[0-9]+$'
decimal = r'^decimal$'
numero = r'^numero$'
palabra = r'^palabra$'



operation_type = {
    '+': 'add',
    '-': 'sub',
    '*': 'mul',
    '/': 'div',
    '%': 'mod',
    '==': 'eq'
}

data_type = {
    'int': 'numero',
    'float': 'decimal',
    'String': 'palabra'
}

separation_symbol ={
    ';': 'punto_y_coma',
    ',': 'coma',
    '(': 'parentesis_abierto',
    ')': 'parentesis_cerrado',
    '{': 'llave_abierta',
    '}': 'llave_cerrada',
    '[': 'corchete_abierto',
    ']': 'corchete_cerrado',
    ':': 'dos_puntos'
}

def match_lexema(lexema:str)->str:
    if re.match(identifier, lexema):
        return 'identificador'
    elif re.match(decimal, lexema):
        return 'decimal'
    elif re.match(numero, lexema):
        return 'numero'
    elif re.match(palabra, lexema):
        return 'palabra'
    # elif lexema in operation_type:
    #     return operation_type[lexema]
    # elif lexema in data_type:
    #     return data_type[lexema]
    # elif lexema in separation_symbol:
    #     return separation_symbol[lexema]
    else:
        return ' '