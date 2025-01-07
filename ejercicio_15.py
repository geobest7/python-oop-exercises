""" 
Definir una clase Empleado que contien dos atributos: el nombre del empleado y su edad.

La clase Empleado debe contener el constructor y los siguientes métodos:

    - __init__(self,...): un constructor que permite inicializar todos los atributos de la clase Empleado.
      Además, este constructor debe mostrar una cadena de caracteres. (Ver visualización en consola)
    - __del__(self): un destructor que permite eliminar todas las referencias de un objeto. Este método
      especial tambièn debe mostrar una cadena de caracteres en la consola.

"""

class Empleado:
    
    def __init__(self, n_empleado, edad_empleado):
        self.n_empleado = n_empleado 
        self.edad_empleado = edad_empleado
        print(f'Se ha creado un objeto empleado con nombre {self.n_empleado} y edad {self.edad_empleado} años')

    def __del__(self):
        print(f'Se ha eliminado el objeto empleado con nombre {self.n_empleado} y edad {self.edad_empleado} años')

empleado_1 = Empleado("Alessandro", 32)
empleado_2 = Empleado("Giulia", 17)

# Verifica las direcciones de memoria
print(f"ID de empleado_1: {id(empleado_1)}")
print(f"ID de empleado_2: {id(empleado_2)}")

del empleado_1

print(f"ID de empleado_2: {id(empleado_2)}")


