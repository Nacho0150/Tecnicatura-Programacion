package org.example.Ejercicio_3;

import java.util.Scanner;

/*Ejercicio 3: La calificacion final de un estudiante de informática
se calcula con base a las calificaciones de cuatro aspectos de su
rendimiento académico: participación, primer examen parcial, segundo
examen parcial y examen final. Sabiendo que las calificaciones anteriores
entran a la calificación final con ponderaciones de 10%, 25%, 25%
y 40%, Hacer un programa que calcule e imprima la calificación final
obtenida por un estudiante.
Que el usuario digite las calificaciones de estos 4 datos y así podremos tener,
la calificación final.
*/
public class Ejercicio_3 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Segun los datos que le pediremos, le sacaremos la nota final del estudiante de informática");
        System.out.println("Ingrese la calificación de participación:");
        double participacion = scanner.nextDouble();

        System.out.println("Ingrese la calificación del primer examen parcial:");
        double primParcial = scanner.nextDouble();

        System.out.println("Ingrese la calificación del segundo examen parcial:");
        double segParcial = scanner.nextDouble();

        System.out.println("Ingrese la calificación del examen final:");
        double exaFinal = scanner.nextDouble();

        double califFinal = (participacion * 0.10) + (primParcial * 0.25) + (segParcial * 0.25) + (exaFinal * 0.40);

        System.out.println("La calificación final es de: " + califFinal);
    }
}