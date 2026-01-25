"""
En este ejercicio, vamos a implementar 3 clases, una clase principal llamada TrabajadorEmpresa y dos
clases hijas que llamaremos respectivamente Director e Ingeniero.

Cada una de las clases debe contener los siguientes métodos:
    - la clase TrabajadorEmpresa:
        - __init__(self,...): un constructor que nos permite inicializar tres atributos, a saber,
          el nombre del trabajador, su salario y su edad.
        - mostrar_funcion(self): un método que permite mostrar la frase "Soy un trabajador de la empresa".
        - mostrar_info(self): un método que permite mostrar la información relacionada con el trabajador, como su nombre,
          salario y edad.

    - la clase Director:
        - __init__(self, ...): un constructor que nos permite inicializar cuatro atributos, a saber, el nombre del director,
          su salario, su edad y la prima que ha recibido.
        - moatrar_funcion(self): un método que permite mostrar la frase "Soy un director de empresa".
        - mostrar_info(self): un método que permite mostrar la información relacionada con el director, como su nombre,
          salario, edad y la prima que ha recibido en euros. (Ver salida consola)

    - la clase Ingeniero:
        - __init__(self, ...): un constructor que nos permite inicializar cuatro atributos, a saber, el nombre del ingeniero,
          su salario, su edad y su especialidad.
        - moatrar_funcion(self): un método que permite mostrar la frase "Soy un ingeniero".
        - mostrar_info(self): un método que permite mostrar la información relacionada con el ingeniero, como su nombre,
          salario, edad y especialidad. (Ver salida consola)

"""

class TrabajadorEmpresa:
    def __init__(self, nombre, salario, edad):
        self.nombre = nombre
        self.salario = salario
        self.edad = edad

    def mostrar_funcion(self):
        print("Soy un trabajador de la empresa")

    def mostrar_info(self):
        print(f'Soy {self.nombre}, trabajador de la empresa, con salario de {self.salario} € y edad {self.edad} años')


class Director(TrabajadorEmpresa):
    def __init__(self, nombre, salario, edad, prima):
        super().__init__(nombre, salario, edad)
        self.prima = prima 
    
    def mostrar_funcion(self):
        print("Soy un director de empresa")

    def mostrar_info(self):
        print(
            f'Soy {self.nombre}, Director de empresa, con salario de {self.salario} € y edad {self.edad} años y una prima anual de {self.prima} €')
        

class Ingeniero(TrabajadorEmpresa):
    def __init__(self, nombre, salario, edad, especialidad):
        super().__init__(nombre, salario, edad)
        self.especialidad = especialidad 
    
    def mostrar_funcion(self):
        print("Soy un ingeniero")

    def mostrar_info(self):
        print(
            f'Soy {self.nombre}, ingeniero, con salario de {self.salario} € y edad {self.edad} años especializado en {self.especialidad} ')


trabajador = TrabajadorEmpresa("Alessandro", 1400, 34)
director = Director("Draghi", 5000, 72, 3500)
ingeniero = Ingeniero("Galileo", 2700, 45, "Electrónica")

trabajador.mostrar_funcion()
trabajador.mostrar_info()

director.mostrar_funcion()
director.mostrar_info()

ingeniero.mostrar_funcion()
ingeniero.mostrar_info()