"""Convierte dólares o euros a pesos mexicanos con tasas de ejemplo."""

TASAS_A_MXN = {
    "eur": 23.70,
    "usd": 20.75,
}


def convertir_a_mxn(moneda, monto):
    return monto * TASAS_A_MXN[moneda]


def main():
    moneda = input("Ingresá la moneda de origen (USD/EUR): ").strip().lower()
    if moneda not in TASAS_A_MXN:
        print("Tipo de conversión no disponible.")
        return

    try:
        monto = float(input("Ingresá el monto a convertir: "))
    except ValueError:
        print("El monto debe ser un número.")
        return

    resultado = convertir_a_mxn(moneda, monto)
    print(f"Resultado: {resultado:.2f} pesos mexicanos.")
    print("Nota: las tasas son valores históricos usados con fines educativos.")


if __name__ == "__main__":
    main()

