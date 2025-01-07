""" 
Definir una clase ManipuladoresArchivos que contien dos atributos: un atributo que hace referecia
al nombre del archivo (o ruta) y un atributo que contiene el objrto retornado después de abrir el
archivo en modo lectura y escritura.

La clase ManipuladoresArchivos debe contener un constructor, un destructor y el siguiente método:

    - __init__(self, nombreArchivo): un contructor que permite inicializar
      los atributos de la clase y mostrar una cadena en la consola. (Ver salida en la consola)
    - __del__(self): un destructor que permite cerrar el archivo y eliminar las referencias del
      objeto de la instancia y luego mostrar una cadena en la consola. (Ver salida en la consola)
    - escribir_archivo( self, frase): este método nos debe permitir escribir la frase pasada como
      parámetro en el archivo. También permite mostrar una cadena en la consola: (Ver salida en la consola)

""" 

class ManipuladoresArchivos:
    
    def __init__(self, nombreArchivo):
        self.nombreArchivo = nombreArchivo
        try:
            self.archivo = open(nombreArchivo, 'r+')
            print(f'Se ha abierto el archivo: {self.nombreArchivo}.')
        except FileNotFoundError:
            self.archivo = open(nombreArchivo, 'w+')
            print(f'Archivo no encontrado, se ha creado el archivo: {self.nombreArchivo}.')
    
    def __del__(self):
        if hasattr(self, 'archivo'):
            self.archivo.close()
            print(f'Se ha cerrado el archivo: {self.nombreArchivo}')
            
    def escribir_archivo(self, frase):
        if hasattr(self, 'archivo'):
            self.archivo.write(frase + '\n')
            print(f'Se ha escrito en el archivo: {frase}')
            
archivo = ManipuladoresArchivos('ejemplo.txt')
archivo.escribir_archivo('Forza Milan')
del archivo