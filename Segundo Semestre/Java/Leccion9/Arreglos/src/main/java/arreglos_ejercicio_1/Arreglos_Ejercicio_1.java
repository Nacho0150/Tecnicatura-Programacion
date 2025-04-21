package arreglos_ejercicio_1;

import java.util.Scanner;

/*
Ejercicio 1: Leer 5 números, guardarlos en un arreglo y
mostrarlos en el mismo orden introducido.
*/
public class Arreglos_Ejercicio_1 {
    public static void main(String[] args) {
        int numeros[]  = new int[5];
        Scanner scanner = new Scanner(System.in);

        System.out.println("Ingrese 5 números");
        System.out.print("1. ");
        numeros[0] = scanner.nextInt();

        System.out.print("2. ");
        numeros[1] = scanner.nextInt();

        System.out.print("3. ");
        numeros[2] = scanner.nextInt();

        System.out.print("4. ");
        numeros[3] = scanner.nextInt();

        System.out.print("5. ");
        numeros[4] = scanner.nextInt();

        System.out.println("\nLos números en el mismo orden introducido son:");
        for (int i = 0; i < numeros.length; i++) {
            System.out.println((i + 1) + ": " + numeros[i]);
        }
    }
}