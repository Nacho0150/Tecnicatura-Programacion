# Eiercicio 11: Agenda telefonica
# Hacer un programa que simule una agenda de contactos. Crear un
# diccionario donde la clave sea el nombre del usuario y el valor
# sea el telefono, el programa tendrá el siguiente menu de opciones:
#      1. Nuevo contacto
#      2. Borrar contacto
#      3. Ver contactos existentes
#      4. Salir

print('Agenda telefónica, qué acción desea realizar?')
diccionario = {}
numero = 0
encontrado = ''

while numero != 4:
    print('\n1. Nuevo contacto')
    print('2. Borrar contacto')
    print('3. Ver contactos existentes')
    print('4. Salir')
    numero = int(input("\nElija una opción \n"))

    if numero == 1:
        user = input("Nombre del nuevo contacto \n")
        num = int(input("Número del nuevo contacto \n"))
        diccionario[user] = num
        print('Contacto Agendado')
    elif numero == 2:
        if len(diccionario) != 0:
            user1 = input("Qué contacto desea eliminar? \n").lower()

            while encontrado != user1:
                for key in diccionario:
                    if key.lower() == user1:
                        encontrado = key
                        break

                if encontrado.lower() == user1:
                    break

                if encontrado.lower() != user1:
                    print('No existe ese contacto en su agenda')

                opt = input("Volver al menú? s/n\n").lower()
                if opt == 's':
                    break

                user1 = input("Qué contacto desea eliminar? \n").lower()
            if encontrado.lower() != user1:
                continue

            diccionario.pop(encontrado)
            print('Contacto Eliminado')
        else:
            print('Su agenda está vacia, volverá al menú principal')
            continue
    elif numero == 3:
        if len(diccionario) != 0:
            for termino, valor in diccionario.items():
             print(termino, valor)
        else:
            print('Su agenda está vacia, volverá al menú principal')
            continue
