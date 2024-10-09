import re
import logging

class NombreExtractor:
    def __init__(self):
        self.patrones_nombre = [
            r"me llamo\s+([a-zA-Z]+)",  # "Me llamo Juan"
            r"mi nombre es\s+([a-zA-Z]+)",  # "Mi nombre es Juan"
            r"puedes llamarme\s+([a-zA-Z]+)",  # "Puedes llamarme Juan"
            r"soy\s+(?:el|la)?\s*([a-zA-Z]+)",  # "Soy Juan" or "Soy el Juan"
            r"nombre:\s*([a-zA-Z]+)",  # "Nombre: Juan"
            r"me dicen\s+([a-zA-Z]+)",  # "Me dicen Juan"
            r"mis amigos me llaman\s+([a-zA-Z]+)",  # "Mis amigos me llaman Juan"
            r"(?:llámame|dime|puedes decirme)\s+([a-zA-Z]+)",  # "Llámame Juan" or "Dime Juan"
            r"yo soy\s+(?:el|la)?\s*([a-zA-Z]+)",  # "Yo soy Juan" or "Yo soy el Juan"
            r"es\s+(?:el|la)?\s*([a-zA-Z]+)",  # "Es Juan" or "Es el Juan"
            r"por favor, llámame\s+([a-zA-Z]+)",  # "Por favor, llámame Juan"
            r"hola,\s*([a-zA-Z]+)",  # "Hola, Juan"
            r"¡hola\s*([a-zA-Z]+)! ¿en qué puedo ayudarte hoy?",  # "¡Hola Juan! ¿En qué puedo ayudarte hoy?"
            r"hola, me llamo\s+([a-zA-Z]+)",  # "Hola, me llamo Juan"
            r"hola, mi nombre es\s+([a-zA-Z]+)",  # "Hola, mi nombre es Juan"
            r"hola, puedes llamarme\s+([a-zA-Z]+)",  # "Hola, puedes llamarme Juan"
            r"hola, soy\s+(?:el|la)?\s*([a-zA-Z]+)",  # "Hola, soy Juan" or "Hola, soy el Juan"
            r"hola, me dicen\s+([a-zA-Z]+)",  # "Hola, me dicen Juan"
            r"hola, mis amigos me llaman\s+([a-zA-Z]+)",  # "Hola, mis amigos me llaman Juan"
            r"hola, (?:llámame|dime|puedes decirme)\s+([a-zA-Z]+)",  # "Hola, llámame Juan"
            r"hola, yo soy\s+(?:el|la)?\s*([a-zA-Z]+)",  # "Hola, yo soy Juan" or "Hola, yo soy el Juan"
            r"hola, es\s+(?:el|la)?\s*([a-zA-Z]+)",  # "Hola, es Juan" or "Hola, es el Juan"
            r"hola, soy el/la\s+([a-zA-Z]+)",  # "Hola, soy el Juan" or "Hola, soy la Ana"
            r"hola, por favor, llámame\s+([a-zA-Z]+)",  # "Hola, por favor, llámame Juan"
        ]

    def extraer_nombre(self, texto):
        texto = texto.lower()  # Convertir todo el texto a minúsculas
        for patron in self.patrones_nombre:
            resultado = re.findall(patron, texto)
            if resultado:
                logging.debug(f"Patrón encontrado: {patron} con resultado: {resultado[0]}")
                return resultado[0].capitalize()  # Retorna el primer nombre encontrado y lo capitaliza
        return None  # Si no encuentra un nombre, retorna None
