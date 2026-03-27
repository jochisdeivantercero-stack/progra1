from Bilioteca import Libro, Revista, MaterialDigital, Usuario, Bibliotecario

def main():
    print("Libros Disponibles")
    
    inventario = [
        Libro(1, "Cálculo Stewart", "2015", "James Stewart", "123-A", "Matemáticas"),
        Libro(2, "Física Mecánica", "2018", "Sears", "124-B", "Física"),
        Revista(3, "National Geographic", "2024", 502, "Mensual"),
        MaterialDigital(4, "Python Guide", "2023", ".pdf", "http://dl.com/1", 12.5),
        Libro(5, "Álgebra Lineal", "2019", "Lay", "125-C", "Matemáticas"),
        Libro(6, "Estructuras de Datos", "2020", "Joyanes", "126-D", "Sistemas"),
        Revista(7, "IEEE Spectrum", "2024", 12, "Mensual"),
        MaterialDigital(8, "Intro a IA", "2024", ".mp4", "http://dl.com/2", 500.0),
        Libro(9, "Circuitos Lógicos", "2017", "Mano", "127-E", "Electrónica"),
        Libro(10, "Termodinámica", "2021", "Cengel", "128-F", "Física")
    ]

    for item in inventario:
        print(item.mostrar_detalle())

    print("\nValidando datos")

    admin = Bibliotecario("Ing. Alberto", "B-01")
    alumno = Usuario("Santiago Hernandez", "U-2026")

    print(f"\nSeleccione el num de su material: 4")
    material_elegido = inventario[3]

    if admin.gestionarPrestamo(alumno, material_elegido):
        print("\nResumen de Pedido:")
        print(f"Producto: {material_elegido.titulo} ({material_elegido.categoria})")
        print(f"Usuario: {alumno.nombre}")
        print(f"Estado: REGISTRADO.")

    print("\nSeleccione el num de su material: 11")
    if 11 > len(inventario):
        print("ID de producto no encontrado.")

if __name__ == "__main__":
    main()