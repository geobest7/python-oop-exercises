""" 
El objetivo de este ejercicio es crear una clase CarritoCompra que nos permite gestionar el 
carrito de compras de un comercio electrónico.

La clase CarritoCompra contiene tres variables de instancia: una variable de instancia que 
nos permitirá almacenar el articulo y su coste total en carrito, una segunda variable de instancia
para almcenar el articúlo y su canitdad en el carrito, y finalmente una tercera para almacenar el 
articúlo y su precio unitario.

Indicación: el diccionario es la esctrucutra más adecuada para crear estos atributos de clase.

Para una buena gestión de nuestro carrito de compra, necesitaremos implementar los siguientes métodos:

    - def __init__(self,...): un constructor para inicializar los atributos  de la clase.
    - def agregar_articulo(self, articulo, precio_u, cantidad): este métod permite agregar un articulo al carrito
      y selecionar el precio unitario y la cantidad por articulo.
    - def eliminar_articulo(self, articulo, cantidad): este método permite eliminar un artículo del carrito.
      También debe actualizar las variables de instancia con cada eliminación de articúlo.
    - def precio_total(self): este método devuelve el precio total del carrito contando los artículos.
    - def listar_articulos(self): este método devuelve una lista con todos los articulos del carrito.
    - def costo_total_articulo(self, articulo): este método devuelve el costo total de un articulo en el carrito.
    - def_obtener_cantidad(self, articulo): este método devuelve la cantidad asociada al artìculo en el carrito.
    - def contar_articulos_distintos(self): este método cuenta una cantidad de articulos distinto en el carrito.
    - __str__(self): este método especial permite personalizar la rapresentación de un objeto de la clase. La 
      cadena de caracteres devuelta hace referencia al estado actual del carrito indicando la lista de articulos 
      existentes en el carrito y el costo toal actual del carrito.

"""

class CarritoCompra:
    def __init__(self):
        
        self.articulo_precio_total = {}
        self.articulo_cantidad = {}
        self.articulo_precio_u = {}

    def agregar_articulo(self, articulo, precio_u, cantidad):
        if articulo in self.articulo_precio_total:
            self.articulo_precio_total[articulo] += round(precio_u * cantidad, 2) 
            self.articulo_cantidad[articulo] += cantidad
        else:
            self.articulo_precio_total[articulo] = round(precio_u * cantidad, 2) 
            self.articulo_cantidad[articulo] = cantidad

        self.articulo_precio_u[articulo] = precio_u

    def eliminar_articulo(self, articulo, cantidad):
        if articulo in self.articulo_precio_total:
            self.articulo_precio_total[articulo] -= round(self.articulo_precio_u[articulo] * cantidad, 2) 
            self.articulo_cantidad[articulo] -= cantidad
            if self.articulo_precio_total[articulo] <= 0 or self.articulo_cantidad[articulo] <= 0:
                del self.articulo_precio_total[articulo]
                del self.articulo_cantidad[articulo]
                del self.articulo_precio_u[articulo]

        else:
            print("El articulo no existe en el carrito.")

    def precio_total(self):
        return sum(self.articulo_precio_total.values())
    
    def listar_articulos(self):
        return list(self.articulo_precio_total.keys())
    
    def costo_total_articulos(self, articulo):
        return self.articulo_precio_total[articulo]
    
    def obtener_cantidad(self, articulo):
        return self.articulo_cantidad[articulo]
    
    def contar_articulos_distintos(self):
        return len(self.articulo_precio_total)
    
    def __str__(self):
        return f'Los artículos contenidos en el carrito son: {self.listar_articulos()}\n' + \
        f'El costo actual del carrito es: {self.precio_total()} euros.'
    
carrito_1 = CarritoCompra()
print("-" * 20)
carrito_1.agregar_articulo("zumo de naranja", 2, 4)
carrito_1.agregar_articulo("pan", 1.2, 3)

print("la cantidad de zumo de naranja seleccionada es:", carrito_1.obtener_cantidad("zumo de naranja"))
print("El costo total de pan es:", round(carrito_1.costo_total_articulos("pan"), 2), "euros.")
print("-" * 20)
print("Estado actual del carrito:")
print(carrito_1)
print("-" * 20)
carrito_1.eliminar_articulo("pan", 2)
print("El costo total del articulo pan después de haber quitado 2 unidades del carrito es:",
      round(carrito_1.costo_total_articulos("pan"), 2))
print("-" * 20)
print("Estado actual del carrito:")
print(carrito_1)
print("-" * 20)
print("El número de artículos distintos comprados es:", carrito_1.contar_articulos_distintos())
print("Articulos y precio total correspondiente en el carrito:", carrito_1.articulo_precio_total)





