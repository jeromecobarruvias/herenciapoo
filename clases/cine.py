class boletocine(object):
    def __init__(self, cliente, funcion, precio_base):
       self.cliente = cliente
       self.funcion = funcion
       self.precio_base = precio_base

    def calcular_precio(self):
        return 90

    def ticket(self):
        return f"Cliente: {self.cliente}, Funcion: {self.funcion}, Precio: ${self.calcular_precio():,.2f}"

class boletoestudiante(boletocine):
    def __init__(self, cliente, funcion, precio_base, descuento=0.3):
        super().__init__(cliente, funcion, precio_base)
        self.descuento = descuento

    def calcular_precio(self):
        return super().calcular_precio() * (1 - self.descuento)

class boletocortesia(boletocine):
    def __init__(self, cliente, funcion, precio_base):
        super().__init__(cliente, funcion, precio_base)

    def calcular_precio(self):
        return 0