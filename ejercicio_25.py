""" 
En este ejercicio, crearemos dos clase: una clase GestionadorArchivos para manejar
nuestros archivos en un directorio especifico y una segunda clase GestionarArchivosAudio
para manejar nuestro archivos de audio.

La clase GestionadorArchivos contiene un solo atributo, que es la ruta del directorio que
queremos manipular, Luego, deben implementarse varios métodos para gestionar este directorio:

    - def __init__(self,...): un constructor para inicializar el atributo que contendrà la ruta
      del directorio.
    - def listar_archivos(self): este método nos ayudarà a listar todos los archivos existentes
      en el directorio y devolverà todos los nombres de los archivos en forma de lista.
    - def crear_archivo(self,archivo): este método nos permitirá crear un nuevo archivo en el directorio
      Solo toma como parámetro el nombre del archivo.
    - def eliminar_archivo(self, archivo): este método debe permitirnos eliminar un archivo. De nuevo,
      solo el nombre del archivo se pasa como parámetro.
    - def renombrar_archivo(self, nombre_antiguo, nuevo_nombre): este método debe usarse para cambiar el 
      nombre del archivo.
    - def extension_archivo(NombreArchivo). este método estático debe permitirnos extraer la extensión de 
      un archivo. Por ejemplo, para un archivo 'archivo1.txt', el método debe devolver 'txt'
.

La segunda clase GestionadorArchivosAudio es una clase que herede de la clase GestionadorArchivos. Esta
clase, a su vez, solo contiene la ruta del directorio como atributo. Además, solo contiene un constructor
y un método:

    - def __init__(self,...): un constructor para inicializar el atributo que contedrá la ruta del directorio.
    - def listar_archivos_audio(self): este método nos ayudará a listar todos los archivos de audio existentes 
      en el directorio. El resultado debe estar de forma de una lista que contenga todos los nombres de los 
      archivos de audio. NB: estamos especialmente interesados en archivos de audio con extensiones: .mp3, .waw o .flac.

""" 
import os

class GestionadorArchivos:
    def __init__(self, ruta):
        self.ruta = ruta  

    def listar_archivos(self):
       return os.listdir(self.ruta)
    
    def crear_archivos(self, nombre_archivo):
        open(f'{self.ruta}/{nombre_archivo}', 'w').close()

    def eliminar_archivo(self, archivo):
        os.remove(f'{self.ruta}/{archivo}')
    
    def renombrar_archivo(self, nombre_antiguo, nombre_nuevo):
        os.rename(f'{self.ruta}/{nombre_antiguo}', f'{self.ruta}/{nombre_nuevo}')

    @staticmethod
    def extension_archivo(nombreArchivo):
        return os.path.splitext(nombreArchivo)[1]
    

class GestionadorArchivosAudio(GestionadorArchivos):
    def __init__(self, ruta):
        super().__init__(ruta)

    def listar_archivos_audio(self):
        extension_archivos_audio = (".mp3", ".wav", ".flac")
        return [f for f in self.listar_archivos() if GestionadorArchivosAudio.extension_archivo(f) 
                in extension_archivos_audio]
    
gestion_archivos_texto = GestionadorArchivos(r"C:\Desktop\programming\PYTHON\30 ejercicios de programaciòn orientada a objetos en PYTHON para Practicar")
print(f'Los archivos existentes en el directorio <<{gestion_archivos_texto.ruta}>> :' + 
      f'{gestion_archivos_texto.listar_archivos()}')

gestion_archivos_texto.crear_archivos("archivo.txt")
print(f'Los archivos existentes en el directorio <<{gestion_archivos_texto.ruta}>> :' +
      'despues de la creación de un nuevo archivo son: ' +
      f'{gestion_archivos_texto.listar_archivos()}')

gestion_archivos_texto.eliminar_archivo("archivo.txt")
print(f'Los archivos existentes en el directorio <<{gestion_archivos_texto.ruta}>> :' +
      'despues de elimina un nuevo archivo son: ' +
      f'{gestion_archivos_texto.listar_archivos()}')

gestion_archivos_texto.renombrar_archivo("gatto.txt", "cane.txt")
print(
    f'Los archivos existentes en el directorio <<{gestion_archivos_texto.ruta}>> '
    f'después de renombrar un archivo son: '
    f'{gestion_archivos_texto.listar_archivos()}'
)

gestiona_audio = GestionadorArchivosAudio(r"C:\Desktop\programming\PYTHON\30 ejercicios de programaciòn orientada a objetos en PYTHON para Practicar")
print(f'la lista de archivos de audio existentes en el directorio' +
      f'<<{gestiona_audio.ruta}>> son: ' +
      f'{gestiona_audio.listar_archivos_audio()}')