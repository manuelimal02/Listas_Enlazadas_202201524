from nodo_persona import nodo_persona

class lista_doble_persona:
    def __init__(self):
        # Referencia al primer nodo
        self.cabeza = None  
        # Referencia al último nodo
        self.cola = None  

    def insertar_persona(self, persona):
        # Creamos un nuevo nodo con el objeto proporcionado
        nuevo_nodo = nodo_persona(persona=persona) 
        # Si la lista está vacía
        if self.cabeza is None:
            # El nuevo nodo se convierte en la cabeza 
            self.cabeza = nuevo_nodo
            # El nuevo nodo también se convierte en la cola  
            self.cola = nuevo_nodo  
        else:
            # El nuevo nodo apunta al nodo anterior
            nuevo_nodo.anterior = self.cola  
            # El nodo anterior apunta al nuevo nodo
            self.cola.siguiente = nuevo_nodo  
            # El nuevo nodo se convierte en la cola de la lista
            self.cola = nuevo_nodo 

    def imprimir_por_siguiente(self):
        # Comenzamos desde la cabeza
        actual = self.cabeza  
        print("----------------")
        while actual:
            # Imprimimos el objeto del nodo actual
            print(actual.persona.nombre, actual.persona.apellido, actual.persona.edad)
            # Avanzamos al siguiente nodo  
            actual = actual.siguiente 
        print("----------------")
    
    def imprimir_por_anterior(self):
        # Comenzamos desde la cola
        actual = self.cola
        print("----------------")
        while actual:
            # Imprimimos el objeto del nodo actual
            print(actual.persona.nombre, actual.persona.apellido, actual.persona.edad)
            # Avanzamos al anterior nodo  
            actual = actual.anterior
        print("----------------")
