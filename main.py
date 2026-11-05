from clases.empleados import Empleado, Vendedor, EmpleadoPorHoras

def main():
    empleado1 = Empleado("Mike", 0.50)
    vendedor1 = Vendedor("Ana", 2500, ventas=1000)
    empleado_horas1 = EmpleadoPorHoras("Luis", horas=20, tarifa=100)

    print(empleado1.descripcion())
    print(vendedor1.descripcion())
    print(empleado_horas1.descripcion())

if __name__ == "__main__":
    main()