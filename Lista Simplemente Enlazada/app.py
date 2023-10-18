# Importación de la clase "lista_simple_empleado" desde el módulo "lista_simple_empleado".
from lista_simple_empleado import lista_simple_empleado
# Importación de la clase "empleado" desde el módulo "empleado".
from empleado import empleado

# Creación de una instancia de la clase "lista_simple_empleado" llamada "manejador_lista".
manejador_lista = lista_simple_empleado()

# Creación de cuatro instancias de la clase "empleado" con datos específicos.
Empleado1 = empleado("A782", "Juan Perez", 45676802, "juan@gmail.com")
Empleado2 = empleado("B840", "Mario Lopez", 78095432, "mario@gmail.com")
Empleado3 = empleado("C719", "Carlos Lima", 78309204, "carlos@gmail.com")
Empleado4 = empleado("E399", "Manuel Juarez", 67654389, "manuel@gmail.com")

# Llamada al método "insertar" en "manejador_lista" para agregar cada instancia de empleado a la lista.
manejador_lista.insertar(Empleado1)
manejador_lista.insertar(Empleado2)
manejador_lista.insertar(Empleado3)
manejador_lista.insertar(Empleado4)

# Llamada al método "imprimir" en "manejador_lista" para mostrar los detalles de los empleados en la lista.
manejador_lista.imprimir()
