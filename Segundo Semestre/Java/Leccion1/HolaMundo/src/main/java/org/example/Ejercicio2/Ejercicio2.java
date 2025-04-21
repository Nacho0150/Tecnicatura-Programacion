package org.example.Ejercicio2;

import java.util.Scanner;

public class Ejercicio2 {
    public static void main(String[] args) {
//        Ejercicio: El mayor de 2 números
//        Usaremos el Operador Ternario

        Scanner scanner = new Scanner(System.in);
        System.out.println("Ingrese dos números y le diremos cual es el mayor: ");
        int num = scanner.nextInt();
        int num1 = scanner.nextInt();

        if (num > num1) {
            System.out.println("El núemero mayor es: " + num);
        } else {
            System.out.println("El núemero mayor es: " + num1);
        }
    }
}