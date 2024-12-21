""" 
Definir una clase Carta que contiene dos atributos: el rango de la carta y su símbolo.

La clase carta debe contener el constructor y los siguinetes métodos:

    - __init__(self, ...): un constructor que permite inicializar todos los atributos de la clase Carta.
    - __eq__(self,carta): este método especial nos debe permitir verificar si dos cartas son iguales comprobando 
      si tienen el mismo rango y el mismo símbolo.
    - __lt__(self,carta): este método especial nos permitirá comparar las cartas según su rango y su símbolo.
    - __str__(self): este método especial nos debe permitir personalizar la representación en cadena de 
      caracteres de la carta. Por lo tanto, la cadena de caracteres devuelta debe contener el rango y el símbolo
      de la carta. (Ver visulaización en la consola)
    
"""

class Carta:
    """
    Un juego de cartas que contiene 32 o 52 cartas
    """
    def __init__(self, rango, simbolo):
        self.rango = rango
        self.simbolo = simbolo
        
    def __eq__(self, carta):
        """ 
        Este método especial permite verificar si dos instancias de esta clase son iguales
        """
        if carta.rango == self.rango and carta.simbolo == self.simbolo:
            return True
        return False
    
    def __lt__(self, carta):
        """ 
        Este método especial permite comparar las cartas por rango y simbolo
        """
        # si las cartas contienen el mismo rango
        if self.rango == carta.rango:
            return self.simbolo < carta.simbolo
        return self.rango < carta.rango
    
    def __str__(self):
        """ 
        Este método especial permite personalizar la representación en cadena de texto de la carta
        """
        return f'La carta con tiene rango {self.rango} y simbolo {self.simbolo}'
    
# Definición de los símbolos / rangos de las diferentes cartas

signos = [chr(9824), chr(9825), chr(9826), chr(9827)]
rangos = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13, "A": 14}

# Definición de las propriedades de las cartas
# cartas que vamos a instanciar

trebol_1, rango_1 = signos[3], rangos["8"]
corazon_2, rango_2 = signos[1], rangos["3"]
pica_3, rango_3 = signos[0], rangos["8"]

# Creación de las instancias de cartas

carta_1 = Carta(rango_1, trebol_1)
carta_2 = Carta(rango_2, corazon_2)
carta_3 = Carta(rango_3, pica_3)

# Representación en cadena de texto de las instancias
print(carta_1)
print(carta_2)
print(carta_3)

# Comparaciòn entre las diferentes instancias

print(carta_1 > carta_2)
print(carta_1 == carta_3)