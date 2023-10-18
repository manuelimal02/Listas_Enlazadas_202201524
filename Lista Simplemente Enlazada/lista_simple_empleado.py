# Importación de la clase nodo_empleado desde el módulo nodo_empleado.
from nodo_empleado import nodo_empleado

# Definición de una clase llamada "lista_simple_empleado" para representar una lista enlazada simple de empleados.
class lista_simple_empleado:
    # Constructor de la clase lista_simple_empleado, que inicializa la lista como vacía.
    def __init__(self):
        # Inicialización del atributo "primero" como None, indicando que la lista está vacía.
        self.primero = None

    # Método "insertar" para agregar un nuevo nodo a la lista con un empleado dado.
    def insertar(self, empleado):
        # Verifica si la lista está vacía.
        if self.primero is None:
            # Si la lista está vacía, crea el primer nodo con el empleado proporcionado.
            self.primero = nodo_empleado(empleado=empleado)
        else:
            # Si la lista no está vacía, se recorre la lista hasta el último nodo.
            actual = self.primero
            while actual.siguiente:
                actual = actual.siguiente
            # Se agrega un nuevo nodo al final de la lista con el empleado proporcionado.
            actual.siguiente = nodo_empleado(empleado=empleado)

    # Método "imprimir" para mostrar los empleados en la lista.
    def imprimir(self):
        # Verifica si la lista está vacía.
        if self.primero is None:
            print("Vacío")
            return
        actual = self.primero
        while actual is not None:
            # Imprime los detalles del empleado en el nodo actual.
            print("Código: ", actual.empleado.codigo, "-- Nombre: ", actual.empleado.nombre, "-- Teléfono: ", actual.empleado.telefono, "-- Correo: ", actual.empleado.correo)
            actual = actual.siguiente
