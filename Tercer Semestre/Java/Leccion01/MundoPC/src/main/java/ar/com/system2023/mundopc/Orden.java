package ar.com.system2023.mundopc;

import java.util.List;

public class Orden {
    private final int idOrden;
    private Computadora computadora[]; //Arreglo de objetos
    private static int contadorOrdenes;
    private static final int MAX_COMPUTADORAS = 10;
    private int contadorComputadora;

    public Orden() {
        this.idOrden = ++Orden.contadorOrdenes;
        this.computadora = new Computadora[Orden.MAX_COMPUTADORAS];
    }

    //Método para agreagar una nueva computadora al arreglo
    public void agregarComputadora(Computadora computadora) {
        if (this.contadorComputadora < Orden.MAX_COMPUTADORAS) {
            this.computadora[this.contadorComputadora++] = computadora;
        } else {
            System.out.println("Has superado el limite: " + Orden.MAX_COMPUTADORAS);
        }
    }

    //Mostrar orden
    public void mostrarOrden() {
        System.out.println("Orden #: " + this.idOrden);
        System.out.println("Computadoras de la orden #: " + this.idOrden);
        for(int i = 0; i < this.contadorComputadora; i++) {
            System.out.println(this.computadora[i]);
        }
    }

//    public Orden(List computadoras) {
//        this();
//        this.computadora = computadoras;
//    }
//
//    public List<Computadora> getComputadoras() {
//        return this.computadora;
//    }
//
//    public void setComputadoras(List<Computadora> computadoras) {
//        this.computadora = computadoras;
//    }
//
//    public int getidOrden() {
//        return this.idOrden;
//    }
//
//    @Override
//    public String toString() {
//        return "Orden{" +
//                "idOrden=" + idOrden +
//                ", computadoras=" + computadora +
//                '}';
//    }
}