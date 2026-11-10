from clases.estacionamiento import estancia, estanciapension, estancianocturna

def main():
    estacionamiento = estancia("ABC123", 3)
    estacionamiento_pension = estanciapension("XYZ789", 24, 250)
    estacionamiento_nocturna = estancianocturna("LMN456", 5)

    print(estacionamiento.ticket())
    print(estacionamiento_pension.ticket())
    print(estacionamiento_nocturna.ticket())

if __name__ == "__main__":
    main()