package org.example.Cilcos08;

/*
Ejercicio 8: Pedir un número N, y mostrar todos los números
del 1 al N.
JOption
*/
public class Ejercicio08 {
    public static void main(String[] args) {
        int numero = Integer.parseInt(javax.swing.JOptionPane.showInputDialog("Ingrese un número: "));
        for (int i = 1; i <= numero; i++) {
            System.out.println(i);
        }
    }
}