"""Convierte una medida de centímetros a pulgadas."""

CENTIMETROS_POR_PULGADA = 2.54


def convertir_a_pulgadas(centimetros):
    return centimetros / CENTIMETROS_POR_PULGADA


def main():
    try:
        centimetros = float(input("Ingresá la medida en centímetros: "))
    except ValueError:
        print("La medida debe ser un número.")
        return

    pulgadas = convertir_a_pulgadas(centimetros)
    print(f"La medida en pulgadas es: {pulgadas:.3f}")


if __name__ == "__main__":
    main()

