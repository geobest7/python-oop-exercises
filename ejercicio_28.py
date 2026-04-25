""" 
El objetivo de este ejercicio es redefinir la clase de diccionario del lenguaje Python 
personalizándolo según nuestras preferencias.
La clase que vamos a crear se llama MiDiccionario y debe contener el constructor y los siguientes métodos:

    - __init__(self): un constructor que permite inicializar una variable de instancia con un diccionario vacío.
    - agregar_elemento(self, clave, valor): este método permite agregar un elemento al objeto de la clase.
    - eliminar_elemento(self, clave): este método permite eliminar un elemento del objeto de la clase a partir
      de su clave.
    - __iter__(self): este método especial permite obtener un iterador del objeto de la clase.
    - __getitem__(self,clave): este método especial permite obtener el valor asociado a una clave en un objeto de 
      la clase.
    - __setitem__(self, clave,valor). este método especial permite modificar el valor asociado a una clave en un 
      objeto de la clase.
    - __len__(self): este método especial devuelve el número de elementos contenidos en un objeto de la clase.
    - __str__(self): este método especial permite personalizar la representación del objeto de la clase.
    - listar_claves(self): este método devuelve todas las claves de un objeto de la clase en forma de lista.
    - listar_valores(self): este método devuelve todos los valores de un objeto de la clase en forma de lista.
    - listar_elementos(self): este método devuelve todos los elementos contenidos en un objeto de la clase.
    - limpiar_diccionario(self): este método permite eleiminar todos los elementos contenidos en un objeto de la clase.
    - contiene_clave(self, clave): este método verifica si una clave existe en un objeto de la clase.

## ejemplos de pruebas / casos de uso:

>> dicc_1 = Midiccionario()
>> dicc_1.agregar_elemento("fruta", "manzana")
>> dicc_1.agregat_elemento("vegetal", "zanahoria")
>> dicc_1.agregar_elemento("carne", "res")
>> print(dicc_1)
>> print("-" * 20)
>> iter_dicc_1 = iter(dicc_1)
>> print("Primera iteración: ")
>> print(...) ## a completar
>> print("Segunda iteración: ")
>> print(...) ## a completar
>> print("Tercera iteración: ")
>> print(...) ## a completar
>> print("-" * 20)
## a completar
>> print(f"El número de elementos en el diccionario es: {..}")
## a completar
>> print(f"Las claves del diccionario 'dicc_1' son: {...})
## a completar
>> print(f"Los valores del diccionario 'dicc_1' son: {...})
## a completar
>> print(f"'fruta està en 'dicc_1': {...})
## a completar
>> print(f"La lista de elementos del diccionario 'dicc_1' es: {...})
>> print("-" * 20)
dicc_1.limpiar_diccionario()
>> print("Después de limpiar el diccionario: ")
>> print(dicc_1)
"""

class MiDiccionario:
    def __init__(self):
        self.datos = {}

    def agregar_elemento(self, clave, valor):
        self.datos[clave] = valor

    def eliminar_elemento(self, clave):
        if clave in self.datos:
            del self.datos[clave]

    def __iter__(self):
        return iter(self.datos)
    
    def __getitem__(self, clave):
        return self.datos[clave]
    
    def __setitem__(self, clave,valor):
        self.datos[clave] = valor

    def __len__(self):
        return len(self.datos)
    
    def __str__(self):
        return f'MiDiciconario: {self.datos}'
    
    def listar_claves(self):
        return list(self.datos.keys())
    
    def listar_valores(self):
        return list(self.datos.values())
    
    def listar_elementos(self):
        return list(self.datos.items())
    
    def limpiar_diccionario(self):
        self.datos.clear()

    def contiene_clave(self, clave):
        return clave in self.datos
    


dicc_1 = MiDiccionario()
dicc_1.agregar_elemento("fruta", "manzana")
dicc_1.agregar_elemento("vegetal", "zanahoria")
dicc_1.agregar_elemento("carne", "res")
print(dicc_1)
print("-" * 20)

iter_dicc_1 = iter(dicc_1)
print("Primera iteración: ")
print(next(iter_dicc_1))
print("Segunda iteración: ")
print(next(iter_dicc_1))
print("Tercera iteración: ")
print(next(iter_dicc_1))
print("-" * 20)

print(f"El número de elementos en el diccionario es: {len(dicc_1)}")

print(f"Las claves del diccionario 'dicc_1' son: {dicc_1.listar_claves()}")

print(f"Los valores del diccionario 'dicc_1' son: {dicc_1.listar_valores()}")

print(f"fruta està en 'dicc_1': {dicc_1.contiene_clave('fruta')}")

print(f"La lista de elementos del diccionario 'dicc_1' es: {dicc_1.listar_elementos()}")
print("-" * 20)

dicc_1.limpiar_diccionario()
print("Después de limpiar el diccionario: ")
print(dicc_1)
    
