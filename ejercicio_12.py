"""
En este ejercicio, debes crear dos clases padres, a saber: la clase Video y la clase Audio.
Luego, debes crear una sublase Media que herede de las clases Video y Audio.
Aquí están los atributos que cada clase debe contener:
    - Para la clase Video: título del video, duración en minutos y categoría del video.
    - Para la clase Audio: título del audio y nombre del artista.
    - Para la clase Media: título del media, su categoría, su duración y el nombre del artista.
Cada clase tiene su proprio constructor y sus proprios métodos, aquí està la lista de métodos a crear
para cada clase:

    Para la clase Video:
    - __init__(self,...): Un constructor para inicializar los atributos de la clase video.
    - mirar_video(self): Un método que permite iniciar el video.
      Este método muestra en la consola una cadena indicando el inicio del video y la información
      relacionada con el video. (Ver la salida en la consola)
    - detener_video(self): Un método que permite detener el video mostrando un mensaje en la consola.

    Para la clase Audio:
    - __init__(self,...): Un constructor para inicializar los atributos de la clase Audio.
    - escuchar_audio(self): Este método permite escuchar el audio mostrando un mensaje en la consola
      indicando el inicio del audio y la información relacionada.
    - detener_audio: Este método permite detener la reproducción del audio mostrando un mensaje en la consola.
    
    
    Para la clase Media:
    - __init__(self,...): Un constructor que permite inicializar todos los atributos de la clase media.
    
"""

class Video:
    def __init__(self, titulo, duracion, categoria):
        self.titulo = titulo
        self.duracion = duracion
        self.categoria = categoria
        
    def mirar_video(self):
        print('El video ha iniciado...')
        print(f'El video que estás viendo se titula {self.titulo} de la categoria {self.categoria} y de la duración de {self.duracion} minutos.')
        
    def detener_video(self):
        print('El video se ha detenido...')
        
class Audio:
    def __init__(self, titulo, artista):
        self.titulo = titulo
        self.artista = artista
        
    def escuchar_audio(self):
        print('El audio ha empezado a reproducirse...')
        print(f'El audio que estas escuchando es {self.titulo} del artista {self.artista}.')
    def detener_audio(self):
        print('El audio se ha detenido...')

class Media(Audio, Video):
    def __init__(self, titulo, duracion, categoria, artista):
        Video.__init__(self, titulo, duracion, categoria)
        Audio.__init__(self, titulo, artista)
        
        
media = Media('Candy Shop', 4, "hip hop", "50 Cent")
media.mirar_video()
media.escuchar_audio()
media.detener_audio()
media.detener_video()