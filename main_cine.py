from clases.cine import boletocine, boletoestudiante, boletocortesia

def main():
    boleto = boletocine("Juan", "Sala 2, 18:00", 90)
    boleto_estudiante = boletoestudiante("Maria", "Sala 1, 20:00", 63)
    boleto_cortesia = boletocortesia("Carlos", "Sala 3, 22:00", 0)

    print(boleto.ticket())
    print(boleto_estudiante.ticket())
    print(boleto_cortesia.ticket())


if __name__ == "__main__":
    main()