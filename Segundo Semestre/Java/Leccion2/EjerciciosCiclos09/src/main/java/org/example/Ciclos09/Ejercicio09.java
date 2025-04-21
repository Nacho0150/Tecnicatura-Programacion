package org.example.Ciclos09;

import java.util.Scanner;

/*
Ejercicio 9: Pedir el día, mes y año de una fecha e
indicar si la fecha es correcta. Suponiendo que
todos los meses son de 30 días
JOption
*/
public class Ejercicio09 {
    public static void main(String[] args) {
        int dia = Integer.parseInt(javax.swing.JOptionPane.showInputDialog("Ingrese un día: "));
        int mes = Integer.parseInt(javax.swing.JOptionPane.showInputDialog("Ingrese un mes: "));
        int año = Integer.parseInt(javax.swing.JOptionPane.showInputDialog("Ingrese un año: "));

        if (dia <= 30 && dia > 0 && mes <= 12 && mes > 0 && año > 0) {
            System.out.println("La fecha: " + dia + "/" + mes + "/" + año + ", es correcta");
        } else {
            System.out.println("La fecha: " + dia + "/" + mes + "/" + año + ", es incorrecta");
        }
    }
}