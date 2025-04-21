package org.example;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
//        Hacer un programa que calcule
//        e imprima la suma de tres calificaciones.
//        Pedir las calificaciones al usuario, crear un
//        proyecto nuevo llamado Ejercicio5

        Scanner scanner = new Scanner(System.in);

        System.out.println("Ingrese 3 calificaciones y le daremos la suma");
        double nota1 = scanner.nextDouble();
        double nota2 = scanner.nextDouble();
        double nota3 = scanner.nextDouble();

        System.out.println("La suma es: " + (nota1 + nota2 + nota3));
    }
}