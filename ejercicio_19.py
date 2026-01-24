"""
 Definimos 3 clases relaxionada con texto:
    - una clase principal llamada Texto como único atributo una frase en forma de cadena de caracteres.
    - una clase hija llamada TextoItalico que hereda de la clase Texto y tiene como único atributo una frase.
    - una segunda clase hija llamada TextoNegrita que hereda de la clase Texto y tiene como único atributo una frase.

Las tres clases contienen un método mostrar_texto(self) que se definá de manera diferente segùn la clase a la 
que pertence:
    - el método mostrar_texto(self) de la clase Texto: este método muestra la frase en consola.
    - el métod mostrar_text(self) de la clase TextoItalico: este método muestra la frase en itálica.
      Para indicar que una frase està en itálico, agregaremos un guion bajo "_" al principio y al final de la frase.
    - el métod mostrar_texto(self) de la clase TextoNegrita: este método muestra la frase en negrita. Para indicar
      que una frase está en negrita, agregaremos un doble asterisco "**" al principio y al final de la frase.

"""

class Texto:
    def __init__(self, frase):
        self.frase = frase

    def mostrar_texto(self):
        return self.frase
    
class TextoItalico(Texto):
    def __init__(self, frase):
        super().__init__(frase)

    def mostrar_texto(self):
        return f'_{self.frase}_'
    
class TextoNegrita(Texto):
    def __init__(self, frase):
        super().__init__(frase)

    def mostrar_texto(self):
        return f'**{self.frase}**'
    
ita = TextoItalico("esto es Itálico")
negrita = TextoNegrita("Esto es negrita")

print(ita.mostrar_texto())
print(negrita.mostrar_texto())

