class Cliente:
    def __init__(self, nombre, apellido, email, direccion):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.direccion = direccion

    def modificar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def modificar_apellido(self, nuevo_apellido):
        self.apellido = nuevo_apellido

    def modificar_email(self, nuevo_email):
        self.email = nuevo_email

    def modificar_direccion(self, nueva_direccion):
        self.direccion = nueva_direccion

    def __str__(self):
        return f"Se ha creado cliente: {self.nombre} {self.apellido}"


cliente1 = Cliente("Juan", "Perez", "j_perez@gmail.com",
                   "AV. Siempre Viva 123")


# Imprimir información del cliente
print("=============================")
print("  Información del cliente    ")
print("=============================\n")

print("Nombre:", cliente1.nombre)
print("Apellido:", cliente1.apellido)
print("Email:", cliente1.email)
print("Dirección:", cliente1.direccion)
print(cliente1)
