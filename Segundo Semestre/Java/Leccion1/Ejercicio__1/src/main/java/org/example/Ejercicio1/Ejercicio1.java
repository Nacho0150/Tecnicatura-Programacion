package org.example.Ejercicio1;

import java.util.Scanner;

public class Ejercicio1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Digite el nombre del libro: ");
        String nombreLibro = scanner.nextLine();
        System.out.println("Digite el id del libro: ");
        int idLibro = Integer.parseInt(scanner.nextLine());
        System.out.println("Digite el precio del libro: ");
        double precioLibro = Double.parseDouble(scanner.nextLine());
        System.out.println("Confirme si eñ envio es gratuito: ");
        boolean envioGratuito = Boolean.parseBoolean(scanner.nextLine());

        System.out.println(nombreLibro + " #" + idLibro);
        System.out.println("Precio del libro: $" + precioLibro);
        System.out.println("El envio del libro gratuito es: " + envioGratuito);
    }
}