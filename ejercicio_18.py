"""
Definimos 3 clases:
    - una clase principal llamada Animal, que tiene como único atributo el nombre del animal
    - una clase hija llamada Gato que hereda de la clase Animal, con el único atributo del nombre del gato.
    - una clase hija llamada Perro que hereda de la clase Animal, con el único atributo el nombre del perro.

Las tres clases contienen un método hablar(self) que se definá de manera diferente según la clase a 
la que pertenece:
    - el método hablar(self) de la clase Animal: este método no devuelve ni muestra nada en la consola.
      Debe permanecer vacío.
    - el método hablar(self) de la clase Gato: este método devuelve una cadena de caracteres que contiene el nombre del gato
      y su mallido. (Ver salida en consola)
    - el método hablar(self) de la clase Perro: este método tambén devuelve una cadena de caracteres que contiene
      el nombre del perro y su ladrido. (Ver salida en consola)

"""

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        pass

class Gato(Animal):
    def __init__(self, nombre):
        super().__init__(nombre)

    def hablar(self):
        return f'El gato se llama {self.nombre} y hace Miauuuu'
    

class Perro(Animal):
    def __init__(self, nombre):
        super().__init__(nombre)

    def hablar(self):
        return f'El perro se llama {self.nombre} y hace Bauuuu'
    
gato = Gato("Micio")
perro = Perro("Rex")

print(gato.hablar())
print(perro.hablar())