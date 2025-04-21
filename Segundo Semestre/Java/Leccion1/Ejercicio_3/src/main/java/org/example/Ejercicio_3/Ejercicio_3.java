package org.example.Ejercicio_3;

import java.util.Scanner;

//Ejercicio 3: Leer 2 números: sí son iguales que los multiplique, si el
//primero es mayor que el segundo que los reste y si no que los sume
public class Ejercicio_3 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        double num1, num2, resultado;
        System.out.println("Digite dos números: ");
        num1 = Double.parseDouble(scanner.nextLine());
        num2 = Double.parseDouble(scanner.nextLine());

        if (num1 == num2) {
            // Si son iguales multiplicamos
            resultado = num1 * num2;
        } else {
            if (num1 > num2) {
                // Si el primer número es mayor los restamos
                resultado = num1 - num2;
            } else {
                resultado = num1 + num2;
            }
        }

        System.out.println("El resultado es: " + resultado);
    }
}