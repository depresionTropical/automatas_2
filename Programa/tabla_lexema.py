import re
class tabla_lexema:
    tabla = set()
    def __init__(self) -> None:
        pass

    def get_lexema(self,text:str)->str:
        lexemas = []
        for linea in text.split('\n'):
            if not linea.strip():
                continue  # Saltar líneas en blanco

            # Utilizar expresiones regulares para identificar lexemas
            lexemas = re.findall(r'\b\w+\b|[-+*/=;]', linea)

        return lexemas
    def get_text(self,lexemas:str)->str:
        return lexemas.split(';')
tabla_lexema = tabla_lexema()

print(tabla_lexema.get_text("""numero _A1 = _A2 + _A3;palabra = _Bueno1;"""))