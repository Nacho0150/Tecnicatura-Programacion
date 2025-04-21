package org.example.Ciclos10;

import javax.swing.*;

/*
Ejercicio 10: Pedir 10 números y escribir la suma total
JOptionPane
*/
public class Ejercicio10 {
    public static void main(String[] args) {
        int suma = 0;
        for (int i = 0; i < 10; i++) {
            int numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un número: "));
            suma += numero;
        }
        JOptionPane.showMessageDialog(null, "La suma total es: " + suma);
    }
}