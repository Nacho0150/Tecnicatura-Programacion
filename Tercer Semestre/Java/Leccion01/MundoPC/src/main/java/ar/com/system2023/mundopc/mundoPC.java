package ar.com.system2023.mundopc;

public class mundoPC {
    public static void main(String[] args) {
        Monitor monitorHP = new Monitor("HP", 13); //Importar la clase
        Teclado tecladoHP = new Teclado("Bluetooth", "HP");
        Raton ratonHP = new Raton("Bluetooth", "HP");
        Computadora computadoraHP = new Computadora("Computadora HP", monitorHP, tecladoHP, ratonHP);

        //Creamos otros objetos de diferentes marcas
        Monitor monitorGamer = new Monitor("Gamer", 32);
        Teclado tecladoGamer = new Teclado("Bluetooth", "Gamer");
        Raton ratonGamer = new Raton("Bluetooth", "Gamer");
        Computadora ComputadoraGamer = new Computadora("Computadora Gamer", monitorGamer, tecladoGamer, ratonGamer);

        Monitor monitorSamsung = new Monitor("Samsung", 28);
        Teclado tecladoSamsung = new Teclado("Bluetooth", "Samsung");
        Raton ratonSamsung = new Raton("Bluetooth", "Samsung");
        Computadora ComputadoraSamsung = new Computadora("Computadora Samsung", monitorSamsung, tecladoSamsung, ratonSamsung);

        Monitor monitorPhilips = new Monitor("Philips", 19);
        Teclado tecladoPhilips = new Teclado("Bluetooth", "Philips");
        Raton ratonPhilips = new Raton("Bluetooth", "Philips");
        Computadora ComputadoraPhilips = new Computadora("Computadora Philips", monitorPhilips, tecladoPhilips, ratonPhilips);

        Monitor monitorDell = new Monitor("Dell", 24);
        Teclado tecladoDell = new Teclado("Bluetooth", "Dell");
        Raton ratonDell = new Raton("Bluetooth", "Dell");
        Computadora ComputadoraDell = new Computadora("Computadora Dell", monitorDell, tecladoDell, ratonDell);

        Monitor monitorAsus = new Monitor("Asus", 26);
        Teclado tecladoAsus = new Teclado("Bluetooth", "Asus");
        Raton ratonAsus = new Raton("Bluetooth", "Asus");
        Computadora ComputadoraAsus = new Computadora("Computadora Asus", monitorAsus, tecladoAsus, ratonAsus);

        Monitor monitorMSI = new Monitor("MSI", 36);
        Teclado tecladoMSI = new Teclado("Bluetooth", "MSI");
        Raton ratonMSI = new Raton("Bluetooth", "MSI");
        Computadora ComputadoraMSI = new Computadora("Computadora MSI", monitorMSI, tecladoMSI, ratonMSI);

        Monitor monitorAcer = new Monitor("Acer", 22);
        Teclado tecladoAcer = new Teclado("Bluetooth", "Acer");
        Raton ratonAcer = new Raton("Bluetooth", "Acer");
        Computadora ComputadoraAcer = new Computadora("Computadora Acer", monitorAcer, tecladoAcer, ratonAcer);

        Monitor monitorAorus = new Monitor("Aorus", 15);
        Teclado tecladoAorus = new Teclado("Bluetooth", "Aorus");
        Raton ratonAorus = new Raton("Bluetooth", "Aorus");
        Computadora ComputadoraAorus = new Computadora("Computadora Aorus", monitorAorus, tecladoAorus, ratonAorus);

        Monitor monitorAMD = new Monitor("AMD", 30);
        Teclado tecladoAMD = new Teclado("Bluetooth", "AMD");
        Raton ratonAMD = new Raton("Bluetooth", "AMD");
        Computadora ComputadoraAMD = new Computadora("Computadora AMD", monitorAMD, tecladoAMD, ratonAMD);

        Monitor monitorRedragon = new Monitor("Redragon", 30);
        Teclado tecladoRedragon = new Teclado("Bluetooth", "Redragon");
        Raton ratonRedragon = new Raton("Bluetooth", "Redragon");
        Computadora ComputadoraRedragon = new Computadora("Computadora Redragon", monitorRedragon, tecladoRedragon, ratonRedragon);

        Orden orden1 = new Orden(); //Inicializamos el arreglo vacio
//        Orden orden2 = new Orden(); //Una nueva lista para el objeto orden2
        orden1.agregarComputadora(computadoraHP);
        orden1.agregarComputadora(ComputadoraGamer);
        orden1.agregarComputadora(ComputadoraSamsung);
        orden1.agregarComputadora(ComputadoraPhilips);
        orden1.agregarComputadora(ComputadoraDell);
        orden1.agregarComputadora(ComputadoraAsus);
        orden1.agregarComputadora(ComputadoraMSI);
        orden1.agregarComputadora(ComputadoraAcer);
        orden1.agregarComputadora(ComputadoraAorus);
        orden1.agregarComputadora(ComputadoraAMD);
        orden1.agregarComputadora(ComputadoraRedragon);
        orden1.mostrarOrden();

//        Computadora computadorasVarias = new Computadora("Computadora de diferentes marcas", monitorHP, tecladoGamer, ratonHP);
//        orden2.agregarComputadora(computadorasVarias);

//        orden2.mostrarOrden();

        //Crear mas objetos de tipo computadora con todos sus elementos
        //completar una lista en el objeto orden1 que llegue a los 10 elementos
        //probar de esta manera los métodos al máximo rendimiento
    }
}