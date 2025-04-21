package matriz_ejercicio_5;

import javax.swing.*;
import java.util.Scanner;

/*
Ejercicio 5: Crear y cargar una matriz de tamaño n x m, mostrar la suma
de cada fila y de cada columna.
*/
public class Matriz_Ejercicio_5 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int matriz[][], nFilas, nCol, sumaFila, sumaColumna;
        int posFila, posCol;

        nFilas = Integer.parseInt(JOptionPane.showInputDialog("Digite el numero de filas: "));
        nCol = Integer.parseInt(JOptionPane.showInputDialog("Digite el numero de columnas: "));

        matriz = new int[nFilas][nCol];
        int filas[] = new int[nFilas];
        int columnas[] = new int[nCol];

        System.out.println("Rellenando la matriz: ");
        for (int i = 0; i < nFilas; i++) {
            for (int j = 0; j < nCol; j++) {
                System.out.print("Matriz [" + i + "][" + j + "]: ");
                matriz[i][j] = entrada.nextInt();
            }
        }

        System.out.println("\nMatriz Original: ");
        for (int i = 0; i < nFilas; i++) {
            for (int j = 0; j < nCol; j++) {
                System.out.print(matriz[i][j] + " ");
            }
            System.out.println("");
        }

        //Sumando las filas
        posFila = 0;
        for (int i = 0; i < nFilas; i++) {
            sumaFila = 0;
            for (int j = 0; j < nCol; j++) {
                sumaFila += matriz[i][j];
            }
            filas[posFila] = sumaFila;
            posFila++;
        }

        //Sumando las columnas
        posCol = 0;
        for (int j = 0; j < nCol; j++) {
            sumaColumna = 0;
            for (int i = 0; i < nFilas; i++) {
                sumaColumna += matriz[i][j];
            }
            columnas[posCol] = sumaColumna;
            posCol++;
        }

        System.out.println("\nLa suma de las filas es: ");
        for (int i = 0; i < nFilas; i++) {
            System.out.print(filas[i] + " - ");
        }
        System.out.println("");

        System.out.println("\nLa suma de las columnas es: ");
        for (int j = 0; j < nCol; j++) {
            System.out.print(columnas[j] + " - ");
        }
        System.out.println("");
    }
}