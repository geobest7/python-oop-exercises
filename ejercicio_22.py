"""  
En este ejercicio vamos a implementar 3 clases, de las cuales 
una es una clase Padre y las otras dos son subclases.

Detalle de las clases con los diferentes constructores y métodosa crear:

    - la clase Computadora: esta clase tiene tres atributos que son la marca
      de la computadora, el modelo y el precio.
      Se deben implementar varios métodos para esta clase Padre:
        - __init__(self,..): un constrcutor que permite inicializar los atributos
            de la clase Computadora.
        - listar_marcas(): este método estático permite listar las diferentes marcas
            disponibles: "Dell", "HP", "Lenovo" et "Apple".

    - la clase ComputadoraDeEscritorio: esta clase hereda de la clase Computadora y 
      tiene 4 atributos: la marca de la computadora de escritorio, el modelo, el precio
      y el tamaño de la unidad central en cm.
      La lista de métodos a crear para la clase ComputadoraDeEscritorio es:
        - __init__(self,...): este método permite inicializar los atributos de la clase
        ComputadoraDeEscrito.
        - mostrar_informacion(self): este método permite mostrar la información relcionada
        con el objeto de clase. (Ver salida en consola)

    - la clase ComputdoraPortatil: esta segunda clase hija hereda de la clase Computadora
      y tiene 4 atributos: la marca de la computadora portátil, el modelo, el precio y el 
      tamaño de la pantalla en pulgadas.
      Esta clase contendrá dos métodos:
        - __init__(self,...): este método permite inicializar los atributos de la clase
        ComputadoraPortatil.
        - mostrar_informacion(self): este método permite mostrar la información relacionada con
          el objeto de esta clase. (Ver salida en consola)

"""       

class Computadora:
    def __init__(self, marca, modelo, precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio

    @staticmethod
    def listar_marcas():
        return "Dell", "HP", "Lenovo", "Apple"
    
class ComputadoraDeEscritorio(Computadora):
    def __init__(self, marca, modelo, precio, tamano_unidad_central):
        super().__init__(marca, modelo, precio)
        self.tamano_unidad_central = tamano_unidad_central

    def mostrar_informacion(self):
        print(f'Esta computadora de escritorio es de marca {self.marca},'
              f' modelo {self.modelo} y el tamaño de su unidad central es de {self.tamano_unidad_central} cm.'
              f' El precio es de {self.precio} €.')


class ComputadoraPortatil(Computadora):
    def __init__(self, marca, modelo, precio, tamano_pantalla):
        super().__init__(marca, modelo, precio)
        self.tamano_pantalla = tamano_pantalla

    def mostrar_informacion(self):
        print(f'Esta computadora portátil es de marca {self.marca},'
              f' modelo {self.modelo} y el tamaño de la pantalla es {self.tamano_pantalla} pulgadas.'
              f' El precio es de {self.precio} €.')
        


comp = Computadora("PCSpecialist", "granmodelo", 900)
print(comp.listar_marcas())

comp_escr = ComputadoraDeEscritorio("Lenovo", "AHJ8789", 1400, 60)
comp_escr.mostrar_informacion()
comp_port = ComputadoraPortatil("Dell", "AFG945", 1600, 15)
comp_port.mostrar_informacion()
