from Cine import Pelicula, Usuario, Producto

print("Productos disponibles")
pro1 = Producto(2, "Palomitas G", 85.0, "Snacks")
pro2 = Producto(3, "Refresco G", 55.0, "Bebidas")
pro3 = Producto(4, "Hot Dog Especial", 75.0, "Comida")
pro4 = Producto(5, "Nachos Dobles", 80.0, "Snacks")
pro5 = Producto(6, "Chocolate Barra", 40.0, "Dulces")
pro6 = Producto(7, "Gomitas de Oso", 35.0, "Dulces")
pro7 = Producto(8, "Combo Pareja", 220.0, "Combos")
pro8 = Producto(9, "Icee Grande", 70.0, "Bebidas")
pro9 = Producto(10, "Cubeta Cine", 180.0, "Promos")
pro10 = Producto(11, "Papas Fritas", 45.0, "Lo tradicional")

Productos_Disponibles=[pro1,pro2, pro3, pro4, pro5, pro6, pro7, pro8, pro9, pro10]
for p in Productos_Disponibles:
    print(p.mostrarDetalle())
print("Validacion de Datos finalizada")

print("Iniciando prueba de datos de reserva")
usu1 = Usuario("Carlos Slim", "carlos@mail.com", "USR-001")
print(f"Usuario: {usu1.nombre} (Puntos:{usu1.puntos})")
print("Pelicula: Duna: Parte Dos Sala 04 (IMAX)")

print("Seleccione sus asientos: A1, A2, B5")
print("SISTEMA: Verificando disponibilidad...")
print("ERROR: El asiento A2 ya está ocupado por la Reserva #882.")
print("SISTEMA: Por favor, seleccione asientos disponibles.")
print("\nSeleccione sus asientos: A1, A3, B5")
print(": Asientos A1, A3, B5 bloqueados con éxito.")
print("Monto base: $450.00")

peli1 = Pelicula("Duna: Parte Dos", "166 min", "B", "Sci-Fi")
peli2 = Pelicula("Kung Fu Panda 4", "94 min", "AA", "Animación")
peli3 = Pelicula("Godzilla x Kong", "115 min", "B", "Acción")
peli4 = Pelicula("Cazafantasmas", "115 min", "B", "Comedia")
peli5 = Pelicula("Intensa-Mente 2", "100 min", "A", "Aventura")
peli6 = Pelicula("Deadpool & Wolverine", "127 min", "C", "Acción")
peli7 = Pelicula("Beetlejuice 2", "105 min", "B", "Fantasía")
peli8 = Pelicula("Gladiador 2", "150 min", "C", "Épico")
peli9 = Pelicula("Guasón 2", "138 min", "C", "Drama")
peli10 = Pelicula("Moana 2", "110 min", "AA", "Musical")

usu1 = Usuario("Carlos Slim", "carlos@mail.com", "USR-001")
usu2 = Usuario("Ana Guevara", "ana@mail.com", "USR-002")
usu3 = Usuario("Roberto Gomez", "chespirito@mail.com", "USR-003")
usu4 = Usuario("Elena Poniatowska", "elena@mail.com", "USR-004")
usu5 = Usuario("Guillermo Toro", "memo@mail.com", "USR-005")
usu6 = Usuario("Frida Kahlo", "frida@mail.com", "USR-006")
usu7 = Usuario("Diego Rivera", "diego@mail.com", "USR-007")
usu8 = Usuario("Salma Hayek", "salma@mail.com", "USR-008")
usu9 = Usuario("Benito Juarez", "benito@mail.com", "USR-009")
usu10 = Usuario("Sor Juana", "juana@mail.com", "USR-010")

print(f"Pelicula: {peli1.nombrePeli}")
print(f"Usuario: {usu1.nombre}")
print(f"Producto seleccionado: {pro1.nombre}")

#dsuento
print("Aplicar descuento")

print(f"Producto seleccionado: {pro6.nombre}")
print(f"Precio original: ${pro6.precio}")

mensaje = pro6.aplicarPromo(50) 

print(mensaje)
print(f"Verificación final: {pro6.mostrarDetalle()}")
