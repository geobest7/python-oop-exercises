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

# Aquí, al finalizar el script, el recolector de basura eliminará los objetos sin necesidad de llamar explícitamente a un `print("Fin del programa")`
# El recolector de basura llamará a `__del__` cuando ya no haya más referencias a los objetos.
# Nota explicativa:

"""
Nota explicativa sobre los métodos __init__ y __del__:

- Método __init__(self, ...): 
   El constructor __init__ se llama automáticamente cuando se crea una nueva instancia de la clase. 
   En este caso, se utiliza para inicializar los atributos n_empleado (nombre del empleado) y edad_empleado (edad del empleado). 
   Además, imprime un mensaje en consola indicando que se ha creado un nuevo objeto Empleado.

- Método __del__(self):
   El método __del__ es el destructor de la clase y se invoca automáticamente cuando el objeto está a punto de ser destruido. 
   Este método se utiliza para liberar los recursos o referencias asociadas al objeto. En este caso, simplemente imprime un mensaje en consola indicando que el objeto Empleado está siendo eliminado.
   
   Importante: El método __del__ no se ejecuta de manera inmediata al usar del en el objeto. En cambio, cuando ya no hay más referencias al objeto, el recolector de basura de Python se encarga de eliminarlo, lo que incluye la llamada al método __del__.

- Funcionamiento del recolector de basura:
   En el caso de que un objeto ya no tenga referencias activas (por ejemplo, cuando se usa del para eliminar el nombre de referencia o cuando el objeto sale del alcance), 
   el recolector de basura de Python se encargará de liberar la memoria ocupada por ese objeto. Si el objeto tiene un método __del__, este se ejecutará antes de que el objeto sea destruido.
   
   Es importante tener en cuenta que si hay ciclos de referencia entre objetos, el recolector de basura puede no destruir los objetos inmediatamente.

   Al final del script, cuando no haya más referencias a los objetos empleado_1 y empleado_2, el recolector de basura llamará al método __del__ de cada uno, liberando la memoria y eliminando los objetos. 
   Si no se usan más referencias, el método __del__ se ejecutará antes de la destrucción final del objeto.

Comportamiento observado al ejecutar el script:

1. Creación de objetos: Al crear los objetos empleado_1 y empleado_2, se ejecuta el método __init__, que imprime un mensaje indicando que se han creado los objetos con sus respectivos atributos.

2. Eliminación del objeto: Después de usar del empleado_1, el objeto empleado_1 pierde su referencia, y al final del script, el recolector de basura llamará a __del__, imprimiendo un mensaje indicando que el objeto ha sido eliminado.

3. Observación de direcciones de memoria: El script también imprime las direcciones de memoria de los objetos empleado_1 y empleado_2 mediante la función id(). Esto muestra que ambos objetos son instancias separadas en memoria.

4. Fin del programa: Cuando el script termina y no hay más referencias a empleado_2, el recolector de basura se encargará de llamar a __del__ para eliminar también a empleado_2, aunque esto no se muestra explícitamente en el código.
"""




