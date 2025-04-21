package org.example.Ejercicio_2;

import java.util.Scanner;

// Ejercicio 2: En un almacén se hace un 20 MOD de descuento a los clientes
// cuya compra supere los $100. ¿Cuál será la cantidad que
// pagara una persona por su compra?
public class Ejercicio_2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double compra, descuento, precio_final;

        System.out.println("Digite la cantidad a pagar");
        compra = Double.parseDouble(scanner.nextLine());

        if (compra > 100) {
            descuento = compra * 0.2;
        } else {
            descuento = 0;
        }
        precio_final = compra - descuento;
        System.out.println("El precio a pagar es: " + precio_final);
    }
}