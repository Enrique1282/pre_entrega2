from cliente import Cliente


class Compra:
    def __init__(self, cliente, producto, empresa, monto):
        self.cliente = cliente
        self.producto = producto
        self.empresa = empresa
        self.monto = monto

    def modificar_cliente(self, nuevo_cliente):
        self.cliente = nuevo_cliente

    def modificar_producto(self, nuevo_producto):
        self.producto = nuevo_producto

    def modificar_empresa(self, nueva_empresa):
        self.empresa = nueva_empresa

    def modificar_monto(self, nuevo_monto):
        self.monto = nuevo_monto

    def __str__(self) -> str:
        return f">>> Se te enviara un correo a {cliente1.email} con la factura de la compra."


cliente1 = Cliente("Juan", "Perez", "j_perez@gmail.com",
                   "AV. Siempre Viva 123")

compra1 = Compra(cliente1, "Play Station", "Sony", "u$d 299.99")

print("=============================")
print("     COMPRA REALIZADA        ")
print("=============================\n")
print("Información de la compra:")
# print("Cliente:", compra1.cliente.nombre)
print("Producto:", compra1.producto)
print("Empresa:", compra1.empresa)
print(f"Monto:  {compra1.monto}\n")

print(compra1)
