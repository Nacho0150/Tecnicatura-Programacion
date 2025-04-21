# Ejercicio 8: Menú interactivo - Cajero automatico
# Hacer un programa que simule un cajero automatico con un saldo
# inicial de 1000$ y tendrá el siguiente menú de opciones:
#                1. Ingresar dinero en la cuenta
#                2. Retirar dinero de la cuenta
#                3. Mostrar dinero disponible
#                4. Salir
print('Cajero Automático, qué acción desea realizar?')
money = 1000
numero = 0
withdraw = 0
opt = ''

while numero != 4:
    print('\n1. Ingresar dinero en la cuenta')
    print('2. Retirar dinero de la cuenta')
    print('3. Mostrar dinero disponible')
    print('4. Salir')
    numero = int(input("\nElija una opción \n"))

    if numero == 1:
        deposit = int(input("Cuánto desa depositar? \n"))
        money += deposit
    elif numero == 2:
        withdraw = int(input("Cuánto desea retirar? \n"))
        while withdraw > money:
            if  withdraw > money:
                print('No posee esa cantidad de dinero en la cuenta')

            opt = input("Volver al menú? s/n\n").lower()
            if opt == 's':
                break

            withdraw = int(input("Cuánto desea retirar? \n"))
        if withdraw > money:
            continue

        money -= withdraw
    elif numero == 3:
        print(f'Dinero en la cuenta: {money}')