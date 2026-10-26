#Programa simulador de cajero automatico
#1.Pedir monto
#2.Verificar que sea multiplo de 100

print("====BIENVENIDO AL PROGRAMA SIMULADOR DE CAJERO AUTOMATICO====")

saldo = 5000
billetes = [500, 200, 100]

respuesta = input("Desea retirar dinero? (si/no): ").strip().lower()

while respuesta == "si":
    print(f"Su saldo actual es de: ${saldo:,.2f} pesos")

    while True:
        try:
            monto = int(input("Cuanto dinero desea retirar: "))
            break
        except ValueError:
            print("Ingresa un numero valido")

    while monto <= 0 or monto % 100 != 0 or monto > saldo:
        if monto <= 0:
            print("Ingresa un numero superior a cero")
        elif monto > saldo:
            print("La cantidad ingresada supera su saldo actual")
        else:
            print("El monto debe ser multiplo de 100")

        try:
            monto = int(input("Ingresa otra cantidad: "))
        except ValueError:
            print("Ingresa un numero valido")

    retiro = monto

    for billete in billetes:
        cantidad = monto // billete
        monto %= billete
        if cantidad > 0:
            print(f"{cantidad} billete(s) de ${billete}")

    saldo -= retiro
    print(f"Saldo nuevo: ${saldo:,.2f}")

    respuesta = input("Desea realizar otro retiro? (si/no): ").strip().lower()

print("====GRACIAS POR USAR EL CAJERO====")

