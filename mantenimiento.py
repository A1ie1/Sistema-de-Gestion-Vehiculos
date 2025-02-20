import re

class Mantenimiento:
    def __init__(self, fecha, descripcion, costo):
        self.fecha = fecha
        self.descripcion = descripcion
        self.costo = costo

    @property
    def fecha(self):
        return self._fecha

    @fecha.setter
    def fecha(self, valor):
        if re.match(r"\d{4}-\d{2}-\d{2}", valor): 
            self._fecha = valor
        else:
            raise ValueError("❌ Formato de fecha inválido. Usa YYYY-MM-DD.")

    @property
    def costo(self):
        return self._costo

    @costo.setter
    def costo(self, valor):
        if valor >= 0:
            self._costo = valor
        else:
            raise ValueError("❌ El costo debe ser un número positivo.")

    def __str__(self):
        return f"🛠️ {self.fecha} - {self.descripcion} - Costo: Q{self.costo:.2f}"
