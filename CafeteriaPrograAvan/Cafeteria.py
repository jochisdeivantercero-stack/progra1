# MÓDULO DE PERSONAS
class Persona:
    def __init__(self, idPersona, nombre, email):
        self.idPersona = idPersona
        self.nombre = nombre
        self.email = email

    def login(self):
        return f"Sesión iniciada: {self.nombre}"

    def actualizarPerfil(self, nuevo_nombre):
        self.nombre = nuevo_nombre
        return f"Perfil actualizado a: {self.nombre}"

class Cliente(Persona):
    def __init__(self, idPersona, nombre, email, puntosFidelidad=0):
        super().__init__(idPersona, nombre, email)
        self.puntosFidelidad = puntosFidelidad
        self.historialPedidos = []

    def realizarPedido(self, pedido):
        self.historialPedidos.append(pedido)
        return f"Pedido {pedido.idPersona_pedido} guardado."

    def consultarHistorial(self):
        return [p.idPedido for p in self.historialPedidos]

    def canjearPuntos(self, cantidad):
        if self.puntosFidelidad >= cantidad:
            self.puntosFidelidad -= cantidad
            return True
        return False

class Empleado(Persona):
    def __init__(self, idPersona, nombre, email, idEmpleado, rol):
        super().__init__(idPersona, nombre, email)
        self.idEmpleado = idEmpleado
        self.rol = rol # Ejemplo: "BARISTA", "MESERO"

    def actualizarInventario(self, inventario, ingrediente, cantidad):
        if ingrediente in inventario.ingredientes:
            inventario.ingredientes[ingrediente] += cantidad
        else:
            inventario.ingredientes[ingrediente] = cantidad
        return f"Inventario: {ingrediente} ahora tiene {inventario.ingredientes[ingrediente]}"

    def cambiarEstadoPedido(self, pedido, nuevo_estado):
        pedido.estado = nuevo_estado
        return f"Pedido {pedido.idPedido} marcado como {nuevo_estado}"

# MÓDULO DE PRODUCTOS
class ProductoBase:
    def __init__(self, idProducto, nombre, precioBase):
        self.idProducto = idProducto
        self.nombre = nombre
        self.precioBase = precioBase

class Bebida(ProductoBase):
    def __init__(self, idProducto, nombre, precioBase, tamaño, temperatura):
        super().__init__(idProducto, nombre, precioBase)
        self.tamaño = tamaño
        self.temperatura = temperatura
        self.modificadores = []

    def agregarExtra(self, extra, costo):
        self.modificadores.append(extra)
        self.precioBase += costo

    def calcularPrecioFinal(self):
        return self.precioBase

class Postre(ProductoBase):
    def __init__(self, idProducto, nombre, precioBase, esVegano, sinGluten):
        super().__init__(idProducto, nombre, precioBase)
        self.esVegano = esVegano
        self.sinGluten = sinGluten

# LOGÍSTICA Y VENTAS
class Pedido:
    def __init__(self, idPedido, productos):
        self.idPedido = idPedido
        self.productos = productos # Lista de objetos ProductoBase
        self.estado = "PENDIENTE"
        self.total = 0.0

    def calcularTotal(self):
        self.total = sum(p.precioBase for p in self.productos)
        return self.total

    def validarStock(self, inventario):
        # Lógica: Verifica si hay al menos un ingrediente registrado
        return len(inventario.ingredientes) > 0

class Inventario:
    def __init__(self):
        self.ingredientes = {} # Diccionario String: Integer

    def reducirStock(self, ingrediente, cantidad):
        if ingrediente in self.ingredientes and self.ingredientes[ingrediente] >= cantidad:
            self.ingredientes[ingrediente] -= cantidad
            return True
        return False

    def notificarFaltante(self):
        return [k for k, v in self.ingredientes.items() if v < 5]