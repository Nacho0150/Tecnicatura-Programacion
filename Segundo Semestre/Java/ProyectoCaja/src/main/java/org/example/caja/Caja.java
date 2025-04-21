package org.example.caja;

/*
Proyecto caja:
Ejercicio 1: Crear un proyecto según las especificaciones
mostradas a continuación.
a formula es: volumen = ancho * alto * profundidad
 */
public class Caja {
    int ancho;
    int alto;
    int profundidad;

    public Caja() {
    }

    public Caja(int ancho, int alto, int profundidad) {
        this.ancho = ancho;
        this.alto = alto;
        this.profundidad = profundidad;
    }

    public int calcularVolumen(){
        return ancho * alto * profundidad;
    }
}