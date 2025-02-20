class NodoMantenimiento:
    def __init__(self, mantenimiento):
        self.mantenimiento = mantenimiento
        self.siguiente = None

class Vehiculo:
    def __init__(self, placa, marca, modelo, año, kilometraje):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.kilometraje = kilometraje
        self.historial_mantenimientos = None  

    def agregar_mantenimiento(self, mantenimiento):
        nuevo_nodo = NodoMantenimiento(mantenimiento)
        if not self.historial_mantenimientos:
            self.historial_mantenimientos = nuevo_nodo
        else:
            actual = self.historial_mantenimientos
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def eliminar_mantenimiento(self, fecha):
        if not self.historial_mantenimientos:
            print("❌ No hay mantenimientos registrados.")
            return
        
        actual = self.historial_mantenimientos
        previo = None
        
        while actual and actual.mantenimiento.fecha != fecha:
            previo = actual
            actual = actual.siguiente
        
        if not actual:
            print("❌ No se encontró un mantenimiento con esa fecha.")
            return
        
        if previo:
            previo.siguiente = actual.siguiente
        else:
            self.historial_mantenimientos = actual.siguiente
        
        print("✅ Mantenimiento eliminado correctamente.")

    def listar_mantenimientos(self):
        if not self.historial_mantenimientos:
            print("🚫 No hay mantenimientos registrados.")
            return
        
        actual = self.historial_mantenimientos
        print(f"📜 Historial de mantenimientos para {self.placa}:\n")
        while actual:
            print(actual.mantenimiento)
            actual = actual.siguiente
