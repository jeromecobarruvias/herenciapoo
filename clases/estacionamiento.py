class estancia(object):
    def __init__(self, placas, hora):
        self.placas = placas
        self.hora = hora

    def calcular_costo(self):
        return self.hora * 20
    
    def ticket(self):
        return f"Placas: {self.placas}, Horas: {self.hora}, Cobro: ${self.calcular_costo():,.2f}"


class estanciapension(estancia):
    def __init__(self, placas, horas, tarifa=250):
        super().__init__(placas, horas)
        self.tarifa = tarifa

    def calcular_costo(self):
        return self.tarifa * (self.hora / 24)

class estancianocturna(estancia):
    def __init__(self, placas, hora, tarifa_nocturna=50):
        super().__init__(placas, hora)
        self.tarifa_nocturna = tarifa_nocturna

    def calcular_costo(self):
        return self.tarifa_nocturna + (self.hora * 20)