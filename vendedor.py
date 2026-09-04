class Vendedor:
    def __init__(self, nombre, rut, telefono):
        self.nombre = nombre
        self.rut = rut
        self.telefono = telefono

    def mostrar_datos(self):
        print("---Datos de los vendedores---")
        print(f"Nombre: {self.nombre}, Rut: {self.rut}, Telefono: {self.telefono}")

    def calcular_comision(self):
        pass
