from Cafeteria import Bebida, Cliente, Pedido

p1 = Bebida(1, "Americano", 45.0, "Grande", "CALIENTE")
p2 = Bebida(2, "Capuchino", 55.0, "Mediano", "CALIENTE")
p3 = Bebida(3, "Latte Frío", 60.0, "Grande", "FRIA")
p4 = Bebida(4, "Expresso", 35.0, "Chico", "CALIENTE")
p5 = Bebida(5, "Té Verde", 40.0, "Mediano", "CALIENTE")
p6 = Bebida(6, "Frappé Mocha", 75.0, "Grande", "FRIA")
p7 = Bebida(7, "Chocolate", 50.0, "Grande", "CALIENTE")
p8 = Bebida(8, "Soda Italiana", 48.0, "Mediano", "FRIA")
p9 = Bebida(9, "Macchiato", 58.0, "Chico", "CALIENTE")
p10 = Bebida(10, "Infusión", 42.0, "Mediano", "CALIENTE")

catalogo = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]

print("MENu")

print("/nMenu")
for b in catalogo:
    print(f"[{b.idProducto}] {b.nombre} - ${b.precioBase}")

print("\n>>> INICIAndo PEDIDO...")
try:
    seleccion = int(input("Seleccione el num de su bebida: "))
    
    bebida_elegida = None
    for b in catalogo:
        if b.idProducto == seleccion:
            bebida_elegida = b
            break

    if bebida_elegida:
        print(f"Verificando disponibilidad de '{bebida_elegida.nombre}'...")
        print(f"{bebida_elegida.nombre} seleccionada con éxito.")
        monto = bebida_elegida.precioBase
        descuento = monto * 0.20
        total = monto - descuento
        
        print("\nDescuento")
        print(f"Aplicando descuento del 20%...")
        
        print(f"\nResumen de Pedido:")
        print(f"Producto: {bebida_elegida.nombre} ({bebida_elegida.tamaño})")
        print(f"Total Final: ${total:.2f}")
        print("Estado: PAGADA.")
    else:
        print("ID de producto no encontrado.")

except ValueError:
    print("Por favor, ingrese un número válido.")