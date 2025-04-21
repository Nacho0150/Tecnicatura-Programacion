package org.example.Ejercicio1;

import java.util.Scanner;

// Ejercicio 1: Determinar si un alumno aprueba o reprueba un curso, sabiendo que
// aprobará si su promedio de tres calificaciones es mayor o igual a 70
// reprueba caso contrario.
public class Ejercicio1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        double nota1, nota2, nota3, promedio;
        System.out.println("Digite las 3 calificaciones: ");
        nota1 = Double.parseDouble(scanner.nextLine());
        nota2 = Double.parseDouble(scanner.nextLine());
        nota3 = Double.parseDouble(scanner.nextLine());

        promedio = ((nota1 * 10) + (nota2 * 10) + (nota3 * 10)) / 3;

        if (promedio >= 70) {
            System.out.println("EL alumno esta aprobado con: " + promedio);
        } else {
            System.out.println("EL alumno esta desaprobado con: " + promedio);
        }
    }
}