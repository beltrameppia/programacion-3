#programa anterior, mejorado con las actualizaciones.

class Producto:
    def __init__(self, nombre, tipo, precio, stock):
        self.nombre = nombre
        self.tipo = tipo
        self.precio = precio
        self.__stock = 0
        self.set_stock(stock)

    def get_stock(self):
        return self.__stock

    def set_stock(self, nuevo_stock):
        if nuevo_stock >= 0:
            self.__stock = nuevo_stock
        else:
            print("Stock inválido")

    def mostrar_datos(self):
        print(self.nombre, self.tipo, self.precio,
              "Stock:", self.__stock)

    def vender(self, cantidad):
        if cantidad <= 0:
            print("Cantidad inválida")
        elif cantidad <= self.__stock:
            self.__stock -= cantidad
            print("Venta realizada")
        else:
            print("Stock insuficiente")


# Crear un producto
producto1 = Producto("Leche", "Lácteo", 1500, 10)

# Probar el stock
print("Stock inicial:", producto1.get_stock())

# Venta válida
producto1.vender(3)
print("Stock después de vender:", producto1.get_stock())

# Venta sin stock suficiente
producto1.vender(20)

# Intentar colocar stock negativo
producto1.set_stock(-500)

# Mostrar datos finales
producto1.mostrar_datos()


#f) evitamos que el programa pueda modificar el stock incorrectamente, como asigandole un alor negativo.
# El encapsulamiento controla el acceso y la modificacion de los datos internos. Mientras tanto, la validación comprueva que los datos cumplan ciertos parámetros como que el stock sea mayor que cero.

# Actividad 2: dos tipos de producto.
 class Alimento(producto):
   def __init__(self, nombre, precio, stock, vencimiento):
     super().__init__(nombre, "Alimento", precio, stock)
     self.vencimiento = vencimiento

def mostrar_vencimiento(self):
  print("vence", self.vencimiento)

class Electronico(producto):
   def __init__(self, nombre, precio, stock, garantia_meses):
     super().__init__(nombre "Electronico", precio, stock)
     self.garantia_meses = garantia_meses

def mostrar_garantia(self):
  print("Garantia", self.garantia_meses. "meses")

#aca se crean los objetos
leche = Alimento("leche", 1500, 10, "30/10/2026")
notebook = Electronico("notebook", 800000, 4, 12) 

#metodos heredados y propios de las nuevas clases:
leche.mostrar_datos()
leche.mostrar_vencimiento()
leche.vender(2)

notebook.mostrar_datos()
notebook.mostrar_garantia()

#acá creamos la lista para luego recorrerla.
productos = [leche, notebook]
# aca la recorremos:
for producto in productos:
  producto.mostrar_datos()
  print("---")

# evité repetir los atributos y métodos comunes de la clase Producto, como nombre, precio, stock, mostrar_datos() y vender().
#los propios de casa hija son: Alimento:vencimiento;  Electronico:garantia_meses;


#preguntas teorixas: 
# 1) ¿Por qué es posible llamar a leche.vender(2) si ese método no está escrito en Alimento?

# Porque Alimento hereda de Producto y recibe sus atributos y métodos, entre ellos vender().

# 2) ¿Qué pasaría si quitamos super().init(...) y no inicializamos los atributos comunes?

# Los atributos comunes de Producto no se inicializarían y podrían producirse errores al intentar utilizar métodos que los necesitan.

# 3) ¿Cada objeto comparte el stock con los demás, o tiene el suyo?

# Cada objeto tiene su propio stock independiente. Si modificamos el stock de un producto, no afecta al otro.

# 4) ¿Por qué get_stock() usa return y mostrar_datos() usa print?

# get_stock() utiliza return para devolver el valor del stock y permitir que otros métodos o partes del programa lo utilicen. mostrar_datos() utiliza print para mostrar la información directamente en pantalla.

# 5) ¿Qué diferencia hay entre modificar el stock con un setter y vender un producto?

# El setter permite establecer un nuevo valor de stock siempre que sea válido. En cambio, vender() descuenta una cantidad del stock solamente si hay suficientes unidades disponibles.
