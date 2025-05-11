package test;

import domain.Empleado;

public class TestClaseObject {
    public static void main(String[] args) {
        Empleado empleado1 = new Empleado("Juan", 5000);
        Empleado empleado2 = new Empleado("Juan", 5000);

        if(empleado1 == empleado2) {
            System.out.println("empleado1 y empleado2 son la misma referencia");
        } else {
            System.out.println("empleado1 y empleado2 son diferentes referencias");
        }

        if(empleado1.equals(empleado2)) {
            System.out.println("empleado1 y empleado2 son iguales");
        } else {
            System.out.println("empleado1 y empleado2 son diferentes");
        }

        if(empleado1.hashCode() == empleado2.hashCode()) {
            System.out.println("empleado1 y empleado2 tienen el mismo hashcode");
        } else {
            System.out.println("empleado1 y empleado2 tienen diferentes hashcodes");
        }
    }
}