""" 
Definir una clase Vehiculo y una clase Coche que herede de la clase Vehiculo.
La clase Vehiculo contiene dos atriubutos: marca del vehiculo y una velocidad inicial
con un valor predeterminado = 0.
La sublase Coche tiene un atributo adicional llamado bocina con un valor predeterminado = "¡tuuut!"

La clase Vehiculo debe contener el constructor y los siguientes métodos:

- __init__(self,...): un constructor que permite inicializar los atributos
de la clase Vehiculo-

- acelerar(self, v): un método que permite aumentar la velocidad actual del vehículo con
una velocida v pasada como parámetro.

- desacelerar(self, v): un método que permite reducir la velocidad actual del vehículo con una
velocidad v pasada como parémetro.

- mostrar_velocidad(self): este método muestra la velocidad actual del vehículo. (Ver visualización
en consola)

La subclase Coche debe contener un constructor y un método adicional:

- __init__(self,...): un constructor para inicializar los atributos.

- tocar_claxon(self): este método sirve para tocar la bocina mostrando una cadena de carcteres.
(Ver visualización en la consola)

"""
class Vehiculo:
    
    def __init__(self, marca, v_i = 0):
        self.marca = marca
        self.velocidad = v_i
        
    def acelerar(self, v):
        self.velocidad += v
        
    def decelerar (self, v):
        self.velocidad -= v
        
    def mostrar_velocidad(self):
        print(f"Tu velocidad actual es {self.velocidad} Km/h")
        
class Coche(Vehiculo):
    
    def __init__(self, marca, v_i = 0, bocina = "¡tuuut!"):
        super().__init__(marca, v_i)
        self.bocina = bocina
        
    def tocar_claxon(self):
        print(self.bocina)
        
        
coche_1 = Coche("Peugeot 208", 10.7)
print(f"La velocidad inicial del coche {coche_1.marca} es {coche_1.velocidad} Km/h")

coche_1.acelerar(60)
coche_1.decelerar(24)
coche_1.mostrar_velocidad()
coche_1.tocar_claxon()