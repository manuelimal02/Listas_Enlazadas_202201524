# Definición de una clase llamada "nodo_persona" para representar un nodo en una lista doblemente enlazada.
class nodo_persona:
    # Constructor de la clase "nodo_persona" que recibe tres parámetros: persona, siguiente y anterior (por defecto, todos son None).
    def __init__(self, persona=None, siguiente=None, anterior=None):
        # Inicialización del atributo "persona" con el valor pasado como argumento (por defecto, None).
        self.persona = persona
        # Inicialización del atributo "siguiente" con el valor pasado como argumento (por defecto, None).
        self.siguiente = siguiente
        # Inicialización del atributo "anterior" con el valor pasado como argumento (por defecto, None).
        self.anterior = anterior
