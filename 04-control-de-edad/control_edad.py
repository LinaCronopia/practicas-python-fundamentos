"""Informa si una persona cumple con la edad mínima de ingreso."""

EDAD_MINIMA = 18


def puede_ingresar(edad):
    return edad >= EDAD_MINIMA


def main():
    try:
        edad = int(input("Ingresá la edad de la persona: "))
        if edad < 0:
            raise ValueError
    except ValueError:
        print("La edad debe ser un número entero mayor o igual que cero.")
        return

    if puede_ingresar(edad):
        print("Puede ingresar.")
    else:
        print("No tiene la edad mínima requerida para ingresar.")


if __name__ == "__main__":
    main()

