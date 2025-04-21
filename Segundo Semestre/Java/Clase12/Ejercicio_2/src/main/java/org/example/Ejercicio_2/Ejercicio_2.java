package org.example.Ejercicio_2;

import java.util.Scanner;

/*
Ejercicio 2: Hacer un programa que calcule el cuadro de una suma,
el usuario debe ingresar el valor de a y el valor de b.
Formula: (a+b)2=a^2+b^2+2*a*b
Para esto deberán utilizar la clase Math y un método llamado pow
 */
public class Ejercicio_2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Ingrese dos valores y le calcularemos el cuadro de una suma");
        System.out.println("Valor a:");
        double a = scanner.nextDouble();
        System.out.println("Valor b:");
        double b = scanner.nextDouble();

        double cuadradoA = Math.pow(a, 2);
        double cuadradoB = Math.pow(b, 2);
        double dosAB = 2 * a * b;

        double suma = cuadradoA + cuadradoB + dosAB;

        System.out.println("Su cuadrado de la suma (" + a + " + " + b + ") al cuadrado es: " + a + " ^ 2 + " + b + " ^ 2 +" + " 2 * a * b = " + suma);
    }
}