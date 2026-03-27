
class Material:
    def __init__(self, idMaterial, titulo, añoPublicacion, categoria):
        self.idMaterial = idMaterial
        self.titulo = titulo
        self.añoPublicacion = añoPublicacion
        self.categoria = categoria
        self.disponible = True

    def mostrar_detalle(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"[{self.idMaterial}] {self.titulo} ({self.añoPublicacion}) | {self.categoria} | {estado}"

class Libro(Material):
    def __init__(self, idMaterial, titulo, añoPublicacion, autor, isbn, genero):
        super().__init__(idMaterial, titulo, añoPublicacion, "Libro")
        self.autor = autor
        self.isbn = isbn
        self.genero = genero

class Revista(Material):
    def __init__(self, idMaterial, titulo, añoPublicacion, edicion, periodicidad):
        super().__init__(idMaterial, titulo, añoPublicacion, "Revista")
        self.edicion = edicion
        self.periodicidad = periodicidad

class MaterialDigital(Material):
    def __init__(self, idMaterial, titulo, añoPublicacion, tipoArchivo, urlDescarga, tamañoMB):
        super().__init__(idMaterial, titulo, añoPublicacion, "Digital")
        self.tipoArchivo = tipoArchivo
        self.urlDescarga = urlDescarga
        self.tamañoMB = tamañoMB

class Persona:
    def __init__(self, nombre, id_p):
        self.nombre = nombre
        self.id_p = id_p

class Usuario(Persona):
    def __init__(self, nombre, id_p, limite=3):
        super().__init__(nombre, id_p)
        self.limitePrestamos = limite
        self.listaActiva = []
        self.bloqueado = False

class Bibliotecario(Persona):
    def gestionarPrestamo(self, usuario, material):
        print("\nINICIAndo PRESTAMO")
        print(f"Verificando disponibilidad de '{material.titulo}'...")
        
        if material.disponible and not usuario.bloqueado:
            material.disponible = False
            usuario.listaActiva.append(material)
            print(f"{material.titulo} seleccionado con éxito.")
            return True
        print("Error: No se pudo procesar el préstamo.")
        return False

class Sucursal:
    def __init__(self, idSucursal, nombre):
        self.idSucursal = idSucursal
        self.nombre = nombre
        self.catalogoLocal = []

class Prestamo:
    def __init__(self, idPrestamo, fechaInicio, fechaDevolucion, usuario, material):
        self.idPrestamo = idPrestamo
        self.fechaInicio = fechaInicio
        self.fechaDevolucion = fechaDevolucion
        self.usuario = usuario
        self.material = material

class Penalizacion:
    def __init__(self, monto, motivo):
        self.monto = monto
        self.motivo = motivo
        self.pagada = False

    def bloquearUsuario(self, usuario):
        usuario.bloqueado = True
        print(f"Usuario {usuario.nombre} bloqueado por penalización.")

class Catalogo:
    def buscarPorAutor(self, autor, lista_materiales):
        print(f"Buscando materiales de: {autor}")
        for m in lista_materiales:
            if hasattr(m, 'autor') and m.autor == autor:
                print(f"Encontrado: {m.titulo}")