package domain;

public class Escritor extends Empleado {
    final TipoEscritura tipoEscritura;

    public Escritor(String nombre, double sueldo, TipoEscritura tipoEscritura) {
        super(nombre, sueldo);
        this.tipoEscritura = tipoEscritura;
    }

    //Método para la sobreescritura
    @Override
    public String obtenerDetalles() {
        return super.obtenerDetalles() + ", Tipo de Escritura: " + tipoEscritura.getDescripcion();
    }

    @Override
    public String toString() {
        return "Escritor{" +
                "tipoEscritura=" + tipoEscritura +
                "} " + super.toString();
    }

    public TipoEscritura getTipoEscritura() {
        return tipoEscritura;
    }
}