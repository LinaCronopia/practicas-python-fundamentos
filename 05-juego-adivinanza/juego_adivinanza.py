"""Juego de consola para adivinar un número secreto."""

import random

MINIMO = 1
MAXIMO = 100
MAX_INTENTOS = 5


def main():
    numero_secreto = random.randint(MINIMO, MAXIMO)

    print(f"Adiviná un número entre {MINIMO} y {MAXIMO}.")

    for intento in range(1, MAX_INTENTOS + 1):
        try:
            numero = int(input(f"Intento {intento}/{MAX_INTENTOS}: "))
        except ValueError:
            print("Ingresá un número entero.")
            continue

        if numero == numero_secreto:
            print("¡Felicitaciones! Adivinaste el número secreto.")
            return
        if numero < numero_secreto:
            print("El número secreto es mayor.")
        else:
            print("El número secreto es menor.")

    print(f"Fin del juego. El número secreto era {numero_secreto}.")


if __name__ == "__main__":
    main()

