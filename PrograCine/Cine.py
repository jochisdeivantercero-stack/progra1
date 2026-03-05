class Persona:
    def  __init__(self, nombre, email, idPersona):
        self.nombre= nombre
        self.email= email
        self.idPersona= idPersona

class Usuario(Persona):
    def __init__(self, nombre, email, idPersona):
        super().__init__(nombre, email, idPersona)
        self.reservas = []
        self.puntos= 150

class Producto:
    def __init__(self, id_prod, nombre, precio, categoria):
        self.id_prod = id_prod
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
    
    def mostrarDetalle(self):
         return f"ID: {self.id_prod} | {self.nombre} - ${self.precio}-{self.categoria}"
    
    def aplicarPromo(self, porcentaje):
          descuento = self.precio * (porcentaje/100)
          self.precio -= descuento
          return f"Descuento del {porcentaje}% aplicado"

    def hacer_reservas(self, reservas):
        self.reservas= reservas
        print(f"{self.nombre} hizo una reservacion")

class Empleado(Persona):
    def __init__(self,nombre, rol):
            super().__init__(nombre)
            self.rol=rol

class Espacio:
     def __init__(self,nombre):
          self.nombre= nombre

class Sala(Espacio):
     def __init__(self, numdeSala, tipodeSala, capdeSala):
          super().__init__(numdeSala)
          self.tipoSala= tipodeSala
          self.capdeSala= capdeSala
          self.disponible= True

class ZonaComida(Espacio):
     def __init__(self, nombre):
          super.__init__(nombre)
          self.productos = []

     def agregarProductos(self,productos):
          self.productos.append(productos)
class Pelicula:
     def __init__(self,nombrePeli, duracion, clasificacion, genero):
          self.nombrePeli= nombrePeli
          self.duracion= duracion
          self. clasificacion= clasificacion
          self.genero= genero

class Promocion:
     def __init__ (self, nombre, descuento):
          self.nombre= nombre
          self.descuento= descuento
class Funcion:
     def __init__(self, pelicula, sala, hora):
          self.pelicula=pelicula
          self.sala=sala
          self.hora=hora
class EstadoReserva:
     PENDIENTE = "Pendiente"
     PAGADA = "Pagada"


class Reserva:
     contador = 1

     def __init__(self, usuario, funcion, asientos):
          self.NumReserva = Reserva.contador
          Reserva.contador += 1

          self.usuario= usuario
          self.funcion= funcion
          self.asientos= asientos
          self.estado= EstadoReserva.PENDIENTE
          self.montoTotal= funcion.precio*len(asientos)

     def confirmarPago(self):
          self.estado= EstadoReserva.PAGADA

     def aplicarPromo(self, promo):
          descuento = self.montoTotal * (promo.descuento/100)
          self.montoTotal -= descuento
          print(f"Promocion {promo.nombre} aplicada")
    
     def GenerarTicket(self):
          print("_____Ticket____")
          print("Reserva:", self.NumReserva)
          print("Usuario", self.usuario.nombre)
          print("Pelicula:",self.funcion.pelicula.nombrePeli)
          print("Hora", self.funcion.hora)
          print("Asientos:", self.asientos)
          print("Total:", self.montoTotal)