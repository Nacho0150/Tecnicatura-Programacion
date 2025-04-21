# Ejercicio 4: Etapas de Vida

edad = int(input("Ingrese su edad y le diremos en que etapa de su vida está "))

if (edad >= 0 and edad <= 10):
    print("La infancia es increíble y bella")
elif (edad > 10 and edad <= 19):
    print("Tienes muchos cambios, mucho que estudiar")
elif (edad > 19 and edad <= 29):
    print("Amor y comienza un trabajo")
else:
    print("Para las siguientes etapas deberás completarlo...")