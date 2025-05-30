/*
Uso de la plabra Final
Esta palabra tiene diferentes significados dependiendo donde
se aplique:
    variables: Evita cambiar el valor que almacena la variable
    métodos: Evita que se  modifique la definición o el comportamiento
             de un método desde una subclase (hija)
    clases: Evita que se creen clases hijas
Otras caracteristica es que normalmente, cuando trabajamos con variables
se combina con el modificador de acceso estático para convertir una
variable en una constante, es decir que no se puede mofidificar su valor,
el ejemplo de esto es la clase Math en la cuál todos sus atributos
son de tipo static y final, es por esto que la variable pi* se conoce
como una constante.
*/

import domain.Persona;

public class TestFinal {
    public static void main(String[] args) {
        final int miDni = 3955278;
        System.out.println("miDni = " + miDni);
//        miDni = 20312321; //No se puede modificar el valor de una constante
        System.out.println("Mi atributo constante es: " + Persona.CONSTANTE_AQUI);

        final Persona persona1 = new Persona();
//        persona1 = new Persona(); No se puede asignar una nueva referencia
        persona1.setNombre("Ariel Betancud");
        System.out.println("persona1 nombre: " + persona1.getNombre());
        persona1.setNombre("Liliana");
        System.out.println("persona1 nombre: " + persona1.getNombre());
    }
}