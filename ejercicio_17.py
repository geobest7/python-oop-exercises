""" 
Definir una clase MiCadenaPersonal que contiene un atributo: una cadena de caracteres.

La clase MiCadenaPersonal tiene un constructor y los siguientes métodos especiales:

    - __init__(self, variable_str): un constructor que permite inicializar el atributo de la clase.
    - __add__(self, cadena): este método especial permite concatenar dos cadenas de caracteres. El
      carácter que separa las dos cadena después de la concatenación es '|'.
    - __mul__(self, escalar): este método especial permite repetir una cadena una cantidad de veces igual
      al número escalar pasado como parámetro.
    - __len__(self): este método permite contar la cantidad de caracteres en una cadena sin considera comas,
      puntos, exclamaciones, interrogaciones, espacios y el carácter '|'.
    - __str__(self): este método permite devolver la representación del objeto de la clase en forma de cadena.
    - __contains__(self, subCadena): este método permite verificar si la cadena subCadena está contenida en el
      objeto de la clase.

"""

class MiCadenaPersonal:
    
    def __init__(self, variable_str):
        self.variable_str = variable_str
        
    def __add__(self, cadena):
        return self.variable_str + '|' + cadena.variable_str
    
    def __mul__(self, escalar):
        return self.variable_str * escalar
    
    def __len__(self):
        caracteres_a_excluir = [',', '.', '!', '?', ' ', '|']
        return len([c for c in self.variable_str if c not in caracteres_a_excluir])
    
    def __str__(self):
        return self.variable_str
    
    def __contains__(self, subCadena):
        return  subCadena in self.variable_str
    
cad_1 = MiCadenaPersonal('Hola, que tal cariño?')
cad_2 = MiCadenaPersonal('Muy bien! De resaca, jajajaja!!!')


# add
print('Concatenación:', cad_1 + cad_2)
print('-' * 40)

# mul
print('Repetir:', cad_1 * 2)
print('Repetir:', cad_2 * 4)        
print('-' * 40)

# len
print('Cantidad de caracteres:', cad_1)
print('Cantidad de caracteres:', len(cad_2))
print('-' * 40)

# str
print('Representación de mi cadena:', cad_1)
print('Representación de mi cadena:', cad_2)
print('-' * 40)

# contains
print('Contiene "que":', 'que' in cad_1)
print('Contiene "ciao":', 'ciao' in cad_2)
print('-' * 40)