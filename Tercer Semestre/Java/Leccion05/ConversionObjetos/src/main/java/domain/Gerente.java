package domain;

public class Gerente {
    private String nombre;
    private double sueldo;
    private String departamento;

    public Gerente(String nombre, double sueldo, String departamento) {
        this.nombre = nombre;
        this.sueldo = sueldo;
        this.departamento = departamento;
    }

    //Sobreescribimos el método
    public String obtenerDetalles() {
        return "Nombre: " + this.nombre + ", Sueldo: " + this.sueldo + ", Departamento: " + this.departamento;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
}