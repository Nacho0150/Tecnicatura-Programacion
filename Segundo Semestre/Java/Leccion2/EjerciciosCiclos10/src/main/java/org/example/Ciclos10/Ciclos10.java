package org.example.Ciclos10;

import java.util.Scanner;

/*
Ejercicio 10: Pedir 10 números y escribir la suma total
Hacerlo con la clase Scanner
*/
public class Ciclos10 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int suma = 0;
        for (int i = 0; i < 10; i++) {
            System.out.print("Ingrese un número: ");
            int numero = scanner.nextInt();
            suma += numero;
        }
        System.out.println("La suma total es: " + suma);
    }
}