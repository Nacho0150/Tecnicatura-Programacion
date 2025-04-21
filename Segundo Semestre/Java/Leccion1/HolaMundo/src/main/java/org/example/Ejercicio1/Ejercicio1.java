package org.example.Ejercicio1;

import java.util.Scanner;

public class Ejercicio1 {
    public static void main(String[] args) {
//        Ejercicio : Rectángulo
//        Se solicita calcular el área y el perímetro de un rectángulo, para esto deberemos crear las variables:
//        Alto (int)
//        Ancho(int)
//        El usuario debe proporcionar los valores de alto, ancho y después se debe imprimir el resultado en el siguiente formato:
//        (recuerden no usar acentos, respetar los espacios, mayúsculas, minúsculas y saltos de líneas.

        Scanner scanner = new Scanner(System.in);
        System.out.println("Digite el alto del rectángulo: ");
        double alto = scanner.nextDouble();
        System.out.println("Digite el ancho del rectángulo: ");
        double ancho = scanner.nextDouble();


        double area = alto * ancho;
        double perimetro = (alto + ancho) * 2;

        System.out.println("El area del rectángulo es: " + area);
        System.out.println("El perímetro del rectángulo es: " + perimetro);
    }
}