from vehiculo import Vehiculo


class Motocicleta(Vehiculo):

    def __init__(self, patente, marca, modelo, año, precio, cilindrada, tipo):

        super().__init__(patente, marca, modelo, año, precio)

        self.cilindrada = cilindrada
        self.tipo = tipo

    def encenderMotor(self):
        print("La motocicleta está encendida.")

    def esDeAltaCilindrada(self):
        #VERIFICAMO SI LA CILINDRADO ES ALTA O BAJA
        if self.cilindrada >= 600:
            return True
        else:
            return False