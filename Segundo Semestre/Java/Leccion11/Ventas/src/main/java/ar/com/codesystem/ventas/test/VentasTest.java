package ar.com.codesystem.ventas.test;

import ar.com.codesystem.ventas.Orden;
import ar.com.codesystem.ventas.Producto;

public class VentasTest {
    public static void main(String[] args) {
        Producto producto1 = new Producto("Campera", 9500.00);
        Producto producto2 = new Producto("Pantalon", 29900.00);

        Orden orden1 = new Orden();
        //Agregamos productos al arreglo
        orden1.agregarProducto(producto1);
        orden1.agregarProducto(producto2);
        orden1.mostrarOrden();

        //Tareas:
        //Crear mas objetos de tipo Producto = 10
        //Crear mas objetos de tipo Orden = 2

        Producto producto3 = new Producto("Remera", 1500.00);
        Producto producto4 = new Producto("Gorra", 500.00);
        Producto producto5 = new Producto("Zapatos", 15000.00);
        Producto producto6 = new Producto("Buzo", 25000.00);
        Producto producto7 = new Producto("Medias", 1000.00);
        Producto producto8 = new Producto("Cinturon", 2000.00);
        Producto producto9 = new Producto("Bufanda", 1500.00);
        Producto producto10 = new Producto("Guantes", 2500.00);
        Producto producto11 = new Producto("Camisa", 3500.00);
        Producto producto12 = new Producto("Short", 2500.00);

        Orden orden2 = new Orden();
        orden2.agregarProducto(producto3);
        orden2.agregarProducto(producto4);
        orden2.agregarProducto(producto5);
        orden2.agregarProducto(producto6);
        orden2.agregarProducto(producto7);
        orden2.mostrarOrden();

        Orden orden3 = new Orden();
        orden3.agregarProducto(producto8);
        orden3.agregarProducto(producto9);
        orden3.agregarProducto(producto10);
        orden3.agregarProducto(producto11);
        orden3.agregarProducto(producto12);
        orden3.mostrarOrden();
    }
}