# Definición de una clase llamada "nodo_empleado" para representar un nodo en una lista simple.
class nodo_empleado:
    # Constructor de la clase nodo_empleado que recibe dos parámetros: empleado y siguiente (por defecto, ambos son None).
    def __init__(self, empleado=None, siguiente=None):
        # Inicialización del atributo "empleado" con el valor pasado como argumento (por defecto, None).
        self.empleado = empleado
        # Inicialización del atributo "siguiente" con el valor pasado como argumento (por defecto, None).
        self.siguiente = siguiente
