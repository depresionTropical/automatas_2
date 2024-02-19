import re

decimal = r'^decimal$'
numero = r'^numero$'
palabra = r'^palabra$'


cadena1 = 'decimal'
cadena2 = 'numero'
cadena3 = 'palabra'

# Comprobar si las cadenas cumplen con el patrón
if re.match(decimal, cadena1):
    print(f'{cadena1} cumple con el patrón {decimal}')
else:
    print(f'{cadena1} no cumple con el patrón {decimal}')

if re.match(numero, cadena2):
    print(f'{cadena2} cumple con el patrón {numero}')
else:
    print(f'{cadena2} no cumple con el patrón {numero}')

if re.match(palabra, cadena3):
    print(f'{cadena3} cumple con el patrón {palabra}')
else:
    print(f'{cadena3} no cumple con el patrón {palabra}')