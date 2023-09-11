
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"{self.nombre} - ${self.precio}"


class Playstation(Producto):
    def __init__(self, nombre, precio, modelo):
        super().__init__(nombre, precio)
        self.modelo = modelo

    def __str__(self):
        return f"{self.nombre} - {self.modelo} - ${self.precio}"


class Computadora(Producto):
    def __init__(self, nombre, precio, marca):
        super().__init__(nombre, precio)
        self.marca = marca

    def __str__(self):
        return f"{self.nombre} - {self.marca} - ${self.precio}"


class Celular(Producto):
    def __init__(self, nombre, precio, sistema_operativo):
        super().__init__(nombre, precio)
        self.sistema_operativo = sistema_operativo

    def __str__(self):
        return f"{self.nombre} - {self.sistema_operativo} - ${self.precio}"


print("=============================")
print("         CATALOGO            ")
print("=============================\n")

playstation1 = Playstation("PlayStation 4", 299.99, "SLIM")
computadora1 = Computadora("Laptop", 899.99, "HP")
celular1 = Celular("iPhone X", 999.99, "iOS")

print(playstation1)
print(computadora1)
print(celular1)
