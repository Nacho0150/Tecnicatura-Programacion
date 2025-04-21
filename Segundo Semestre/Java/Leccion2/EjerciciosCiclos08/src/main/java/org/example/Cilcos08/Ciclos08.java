package org.example.Cilcos08;

import java.util.Scanner;

/*
Ejercicio 8: Pedir un número N, y mostrar todos los números
del 1 al N.
Scanner
*/
public class Ciclos08 {
    public static void main(String[] args) {
        int numero = 0;
        Scanner sc = new Scanner(System.in);
        System.out.println("Ingrese un número: ");
        numero = sc.nextInt();
        for (int i = 1; i <= numero; i++) {
            System.out.println(i);
        }
    }
}