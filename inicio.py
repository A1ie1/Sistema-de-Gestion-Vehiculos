import os
from vehiculo import Vehiculo
from mantenimiento import Mantenimiento

def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    vehiculos = {}

    while True:
        limpiar_pantalla()
        print("🚗✨ Gestión de Flota Vehicular ✨🚗")
        print("1️⃣ Agregar vehículo")
        print("2️⃣ Agregar mantenimiento a un vehículo")
        print("3️⃣ Eliminar mantenimiento de un vehículo")
        print("4️⃣ Listar mantenimientos de un vehículo")
        print("5️⃣ Salir")

        opcion = input("\n👉 Selecciona una opción: ")

        if opcion == "1":
            placa = input("Ingrese la placa del vehículo: ").upper()
            marca = input("Ingrese la marca del vehículo: ")
            modelo = input("Ingrese el modelo del vehículo: ")
            año = input("Ingrese el año del vehículo: ")
            kilometraje = float(input("Ingrese el kilometraje actual: "))

            vehiculos[placa] = Vehiculo(placa, marca, modelo, año, kilometraje)
            print("✅ Vehículo agregado con éxito.")
        
        elif opcion == "2":
            placa = input("Ingrese la placa del vehículo: ").upper()
            if placa not in vehiculos:
                print("❌ Vehículo no encontrado.")
            else:
                fecha = input("Ingrese la fecha del mantenimiento (YYYY-MM-DD): ")
                descripcion = input("Ingrese la descripción del servicio: ")
                try:
                    costo = float(input("Ingrese el costo del mantenimiento: "))
                    mantenimiento = Mantenimiento(fecha, descripcion, costo)
                    vehiculos[placa].agregar_mantenimiento(mantenimiento)
                    print("✅ Mantenimiento agregado correctamente.")
                except ValueError as e:
                    print(f"❌ Error: {e}")

        elif opcion == "3":
            placa = input("Ingrese la placa del vehículo: ").upper()
            if placa not in vehiculos:
                print("❌ Vehículo no encontrado.")
            else:
                fecha = input("Ingrese la fecha del mantenimiento a eliminar (YYYY-MM-DD): ")
                vehiculos[placa].eliminar_mantenimiento(fecha)

        elif opcion == "4":
            placa = input("Ingrese la placa del vehículo: ").upper()
            if placa not in vehiculos:
                print("❌ Vehículo no encontrado.")
            else:
                vehiculos[placa].listar_mantenimientos()
        
        elif opcion == "5":
            print("👋 ¡Gracias por usar el sistema de gestión de flota! 🚗")
            break

        input("\nPresiona ENTER para continuar...")

if __name__ == "__main__":
    main()
