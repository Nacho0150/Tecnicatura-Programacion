package org.example;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
//        Una compañía de venta de carros usados, paga a su
//        personal de ventas un salario de $1000
//        mensuales mas una comisión de $150 por cada
//        carro vendido, más el 5% del valor de la venta por
//        carro. Cada mes el capturista de la empresa
//        ingresa en la computadora los datos pertinentes.
//        Hacer un programa que calcule e imprima el salario
//        mensual de un vendedor dado.
//        El salario de 1000 lo vamos a manejar como un dato
//        constante, para asignarlo debemos usar la
//        palabra reservada "final"

        final double salarario = 1000;
        Scanner scanner = new Scanner(System.in);

        System.out.println("Le vamos a calcular su salario");
        System.out.println("Ingrese la cantidad de autos vendidos en el mes");
        int autosVendidios = scanner.nextInt();

        double porcentajeAutosVendidos = 0;
        for (int i = 0; i < autosVendidios ; i++) {
            System.out.println("Precio del " + (i + 1) + " auto");
            double precio = scanner.nextDouble();
            porcentajeAutosVendidos += (precio * (5.0 / 100.0));
        }

        double salarioFinal = 0;
        salarioFinal = porcentajeAutosVendidos + (150.0 * autosVendidios) + salarario;

        System.out.println("Su salario es de: " + salarioFinal);
    }
}