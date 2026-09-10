"""Juego de piedra, papel o tijeras para dos personas."""

OPCIONES = {"piedra", "papel", "tijeras"}
VENCE_A = {
    "piedra": "tijeras",
    "papel": "piedra",
    "tijeras": "papel",
}


def pedir_opcion(nombre):
    while True:
        opcion = input(f"{nombre}, elegí piedra, papel o tijeras: ").strip().lower()
        if opcion in OPCIONES:
            return opcion
        print("Opción no válida. Intentá nuevamente.")


def main():
    nombres = [input("Nombre del jugador 1: "), input("Nombre del jugador 2: ")]
    puntajes = [0, 0]

    for ronda in range(1, 4):
        print(f"\nRonda {ronda}")
        elecciones = [pedir_opcion(nombres[0]), pedir_opcion(nombres[1])]

        if elecciones[0] == elecciones[1]:
            print("Empate.")
        elif VENCE_A[elecciones[0]] == elecciones[1]:
            puntajes[0] += 1
            print(f"Gana la ronda {nombres[0]}.")
        else:
            puntajes[1] += 1
            print(f"Gana la ronda {nombres[1]}.")

    print(f"\nResultado final: {nombres[0]} {puntajes[0]} - {puntajes[1]} {nombres[1]}")
    if puntajes[0] == puntajes[1]:
        print("La partida terminó empatada.")
    else:
        ganador = nombres[0] if puntajes[0] > puntajes[1] else nombres[1]
        print(f"Ganador: {ganador}.")


if __name__ == "__main__":
    main()

