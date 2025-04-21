package org.example.Ejercicio_1;

import java.util.Scanner;

/*
Ejercicio 1: Construir un programa que, dado un número total de
horas, devuelve el número de semanas, días y horas equivalentes.
Por ejemplo dado un total de 1000 horas debe mostrar 5 semanas,
6 días y 16 horas.
 */
public class Ejercicio_1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Ingrese el número de horas y le mostraremos el resultado en semanas, días y horas equivalentes:");
        int totalHoras = scanner.nextInt();

        int semanas = totalHoras / (7 * 24) ;
        int dias = (totalHoras % (7 * 24)) / 24;
        int horas = totalHoras % 24;

        System.out.println("Según las horas, estos son los resultados: Semanas: " + semanas + ", Días: " + dias + " y Horas: " + horas);
    }
}