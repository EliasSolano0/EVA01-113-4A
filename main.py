from auto import Auto
from motocicleta import Motocicleta
from vendedor import Vendedor
from automotora import Automotora


def main():

    # Crear automotora
    automotora1 = Automotora("Los pits")
    automotora2 = Automotora("Los angeles")


    # Crear 2 automóviles
    auto1 = Auto("AJER23", "Chevrolet", "Optra", 2010, 2500000, 4, 1.4)
    auto2 = Auto("AUAR36", "Chevrolet", "Sail", 2016, 5000000, 4, 1.4)


    # Crear motocicleta
    moto1 = Motocicleta("715DMA","Bugati", "203", 2001, 2000000, 800, "Chopera")
    moto2 = Motocicleta("PA32UE","Nissan", "Escailai", 1998, 1800000, 300, "Deportiva")


    # Agregar vehículos a la automotora
    
    


    # Mostrar vehículos
    print("===== VEHÍCULOS DE LA AUTOMOTORA =====")
    #Automotora.mostrarVehiculos()
    

    # Probar métodos de un Auto
    print("\n===== AUTO =====")
    auto1.abrirMaletero()
    print(f"Cuenta con aire acondicionado: {auto1.tieneAireAcondicionado()}")


    # Calcular años de uso del auto
    



    # Probar métodos de Motocicleta
    print("\n===== MOTOCICLETA =====")
    moto1.encenderMotor()
    print(f"Es de alta cilindrada: {moto1.esDeAltaCilindrada()}.")



    # Calcular años de uso de la motocicleta


    # Crear vendedor
    vendedor1 = Vendedor(
            "Juan Pérez",
            "12.345.678-9",
            "987654321"
      )

    print("\n===== VENDEDOR =====")
    vendedor1.mostrar_datos()




    

if __name__ == "__main__":
    main()


# Link git hub: https://github.com/EliasSolano0/EVA01-113-4A.git