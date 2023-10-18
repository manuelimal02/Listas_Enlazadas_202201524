# Importación de la clase "lista_doble_persona" desde el módulo "lista_doble_persona".
from lista_doble_persona import lista_doble_persona
# Importación de la clase "persona" desde el módulo "persona".
from persona import persona

# Creación de una instancia de la clase "lista_doble_persona" llamada "lista_persona".
lista_persona = lista_doble_persona()

# Creación de cuatro instancias de la clase "persona" con datos específicos.
persona1 = persona("Carlos", "Lima", 18)
persona2 = persona("Siomara", "Lopez", 40)
persona3 = persona("Mario", "Ramirez", 10)
persona4 = persona("Marta", "Juarez", 45)

# Llamada al método "insertar_persona" en "lista_persona" para agregar cada instancia de persona a la lista doblemente enlazada.
lista_persona.insertar_persona(persona1)
lista_persona.insertar_persona(persona2)
lista_persona.insertar_persona(persona3)
lista_persona.insertar_persona(persona4)

# Llamada al método "imprimir_por_siguiente" en "lista_persona" para mostrar las personas en la lista siguiendo el enlace siguiente.
lista_persona.imprimir_por_siguiente()
print("")  # Salto de línea para separar la salida.

# Llamada al método "imprimir_por_anterior" en "lista_persona" para mostrar las personas en la lista siguiendo el enlace anterior.
lista_persona.imprimir_por_anterior()
