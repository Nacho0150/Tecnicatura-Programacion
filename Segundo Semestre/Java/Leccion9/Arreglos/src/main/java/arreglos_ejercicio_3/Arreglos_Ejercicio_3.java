package arreglos_ejercicio_3;

import java.util.Scanner;

/*
Ejercicio 3: Leer 5 números por teclado, almacenarlos en
un arreglo y a continuación realizar la media de los
números positivos, la media de los negativos y contar el
número de ceros.
*/
public class Arreglos_Ejercicio_3 {
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

        System.out.println("\nEstos son los datos de los números introducido:");
        int pos = 0;
        int posCont = 0;
        int neg = 0;
        int negCont = 0;
        int ceros = 0;
        for (int i = 0; i < numeros.length; i++) {
            if (numeros[i] > 0) {
                pos += numeros[i];
                posCont++;
            } else if (numeros[i] < 0) {
                neg += numeros[i];
                negCont++;
            } else if (numeros[i] == 0){
                ceros++;
            }
        }
        System.out.println("La media de los números positivos es: " + (pos / posCont));
        System.out.println("La media de los números negativos es: " + (neg / negCont));
        System.out.println("La cantidad de 0 es: " + ceros);
    }
}