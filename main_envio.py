from clases.paqueteria import Envio, EnvioExpress, EnvioSobre

def main():
    envio1 = Envio("Juan", 5)
    envio_sobre1 = EnvioSobre("Maria")
    envio_express1 = EnvioExpress("Carlos", 3)

    print(envio1.resumen())
    print(envio_sobre1.resumen())
    print(envio_express1.resumen())


if __name__ == "__main__":
    main()