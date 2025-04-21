package org.example;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

//        Guillermo tiene N dólares. Luis tiene la mitad de
//        lo que posee Guillermo. Juan tiene la mitad de
//        lo que poseen Luis y Guillermo juntos. Hacer
//        un programa que calcule e imprima la
//        cantidad de dinero que tienen entre los tres.
//        Crear un nuevo proyecto llamado Ejercicio6

        System.out.println("Ingrese una cantidad de dolares y sacaremos el total de los tres: ");
        Scanner scanner = new Scanner(System.in);
        double dolares = scanner.nextDouble();

        double dolares1 = dolares / 2;
        double dolares2 = (dolares + dolares1) / 2;
        double dolares3 = (dolares + dolares1 + dolares2);

        System.out.println("La cantidad de dolares que tiene Guillermo es: $" + dolares + " dolares");
        System.out.println("La cantidad de dolares que tiene Luis es: $" + dolares1 + " dolares");
        System.out.println("La cantidad de dolares que tiene Juan es: $" + dolares2 + " dolares");
        System.out.println("La cantidad de dolares que tienen en total es: $" + dolares3 + " dolares");
    }
}