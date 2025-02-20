from vehiculo import Vehiculo

class Flota:
    def __init__(self):
        self.vehiculos = {}

    def agregar_vehiculo(self, placa, marca, modelo, año, kilometraje):
        if placa in self.vehiculos:
            print("❌ Ya existe un vehículo con esa placa.")
        else:
            self.vehiculos[placa] = Vehiculo(placa, marca, modelo, año, kilometraje)
            print("✅ Vehículo agregado a la flota.")

    def eliminar_vehiculo(self, placa):
        if placa in self.vehiculos:
            del self.vehiculos[placa]
            print("✅ Vehículo eliminado de la flota.")
        else:
            print("❌ No se encontró un vehículo con esa placa.")

    def listar_vehiculos(self):
        if not self.vehiculos:
            print("🚫 No hay vehículos en la flota.")
            return

        print("\n🚗 Flota de vehículos registrados:")
        for vehiculo in self.vehiculos.values():
            print(f"🔹 {vehiculo.placa} - {vehiculo.marca} {vehiculo.modelo} ({vehiculo.año}) - {vehiculo.kilometraje} km")

    def obtener_vehiculo(self, placa):
        return self.vehiculos.get(placa, None)
