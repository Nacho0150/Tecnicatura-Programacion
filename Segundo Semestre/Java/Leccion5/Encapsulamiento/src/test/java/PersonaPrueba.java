package test.java;

import org.example.Dominio.Persona;

public class PersonaPrueba {
    public static void main(String[] args) {
        Persona persona1 = new Persona ("Osvaldo", 57.000, false);
        System.out.println("personal = " + persona1);
        System.out.println("personal su nombre es: " + persona1.getNombre());
        //Modificar a través de los métodos
        persona1.setNombre("Juan Ignacio");
        //persona1.nombre = "Juan Ignacio"; //Ya no se puede utilizar
        //System.out.println("Nombre es: " + persona1.nombre); //Error
        System.out.println("personal con su nombre modificado: " + persona1.getNombre());
        System.out.println("personal el resultado para el sueldo: " + persona1.getSueldo());
        System.out.println("personal para obtener el booleano: " + persona1.isEliminado());

        //Tarea: Crear otro objeto de tipo Persona, asignar valores de manera inicial
        //y imprimir, luego modificar sus valores y volver a imprimir
        System.out.println("personal = " + persona1);

        Persona persona2 = new Persona ("Nacho", 500.000, false);
        System.out.println("personal con su nombre: " + persona2.getNombre());
        System.out.println("personal el resultado para el sueldo: " + persona2.getSueldo());
        System.out.println("personal para obtener el booleano: " + persona2.isEliminado());
        //Modificar a través de los métodos
        persona1.setNombre("Ignacio");
        persona1.setSueldo(550.000);
        persona1.setEliminado(false);
        System.out.println("personal con su nombre modificado: " + persona1.getNombre());
        System.out.println("personal el resultado para el sueldo: " + persona1.getSueldo());
        System.out.println("personal para obtener el booleano: " + persona1.isEliminado());
    }
}