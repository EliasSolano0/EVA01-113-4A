class Vehiculo:
    def __init__(self, patente, marca, modelo, año, precio):
        self.patente = patente
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.precio = precio

    def mostrarInfo(self):
        #MOSTRAMOS LOS METODOS DEL VEHICULO.
        print(f"Patente: {self.patente}, Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.año}, Precio: {self.precio}")

    def calcularAñosUso(self, añoActual):
        #CALCULAMOS EL AÑO DE USO QUE TIENE EL VEHICULO Y LO DEVOLVEMOS.
        añoActual = 2026
        return f"{añoActual - self.año}" 