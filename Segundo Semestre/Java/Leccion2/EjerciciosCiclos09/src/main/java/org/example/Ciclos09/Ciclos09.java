package org.example.Ciclos09;

import java.util.Scanner;

/*
Ejercicio 9: Pedir el día, mes y año de una fecha e
indicar si la fecha es correcta. Suponiendo que
todos los meses son de 30 días
Scanner
*/
public class Ciclos09 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Ingrese el día: ");
        int dia = scanner.nextInt();
        System.out.print("Ingrese el mes: ");
        int mes = scanner.nextInt();
        System.out.print("Ingrese el año: ");
        int año = scanner.nextInt();

        if (dia <= 30 && dia > 0 && mes <= 12 && mes > 0 && año > 0) {
            System.out.println("La fecha: " + dia + "/" + mes + "/" + año + ", es correcta");
        } else {
            System.out.println("La fecha: " + dia + "/" + mes + "/" + año + ", es incorrecta");
        }
    }
}