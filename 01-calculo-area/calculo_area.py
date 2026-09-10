"""Calcula el área de un círculo a partir de su radio."""

import math


def calcular_area(radio):
    return math.pi * radio**2


def main():
    try:
        radio = float(input("Ingresá el radio del círculo: "))
        if radio < 0:
            raise ValueError
    except ValueError:
        print("El radio debe ser un número mayor o igual que cero.")
        return

    print(f"El área del círculo es: {calcular_area(radio):.2f}")


if __name__ == "__main__":
    main()

