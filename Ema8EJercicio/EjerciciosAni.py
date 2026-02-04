class Animales:
    def __init__(self,nombre,color,patas):
        self.nombre=nombre
        self.color=color
        self.patas=patas
    
    def Sonido(self):
       print("sonido")

class Conejo(Animales):
    def __init__(self, nombre, color, patas):
        super().__init__(nombre, color, patas)
    
    def sonido(self):
        print("ribit ribit")

    def presentacion(self):
        print(f"Mi conejo se llama {self.nombre}, es de color {self.color} y tiene {self.patas} patas")

class Ornitorrinco(Animales):
    def __init__(self, nombre, color, patas, pico):
        super().__init__(nombre, color, patas)
        self.pico=pico

    def sonido(self):
        print("ornitorrinco")

    def presentacion(self):
        print(f"Mi ornitorrinco se llama {self.nombre}, es de color {self.color}, tiene {self.patas} patas y su pico mide {self.pico}")

class Dinosaurio (Animales):
    def __init__(self, nombre, color, patas, dinosaurio):
        super().__init__(nombre, color, patas)
        self.tipo=dinosaurio
    def sonido(self):
        print("ruarrrr")
    
    def presentacion(self):
        print(f"Mi dino se llama {self.nombre}, es de color {self.color}, tiene {self.patas} patas es un {self.tipo}")
    