# Ejercicio 9: Mostrar una frase sin espacios y contar su longitud
# Hacer un programa donde el usuario ingrese una frase, se le
# devolverá la misma frase pero sin espacios en blanco, y
# además un contador de cuántos caracteres tiene la frase
# (sin contar los espacios en blanco)
# Eiemplo:      frase = vivir por siempre en paz
#               frase final = vivirporsiempreenpaz
#               Nº de caracteres = 20
fras = input('Ingrese una frase y se le mostrara sin espacios y la longitud \n')
fras2 = fras.replace(' ', '')
print(f'La frase quedo asi: {fras2}, con una logitud de {len(fras2)}')