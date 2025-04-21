// Ejercicio: Encontrar números Pares e Impares
let num = 16;

if (num % 2 == 0) {
    console.log("El número es par")
} else {
    console.log("El número es impar")
}


// Ejercicio: Es mayor de edad
let edad = 15;

if (edad >= 18) {
    console.log("Usted es mayor de edad!");
} else {
    console.log("Usted es menor de edad!");
}

//Ejercicio: Dentro de un rango
let dentroRango = 10; //Aquí vamos a ir cambiando el valor
let valMin = 0, valMax = 10;
if(dentroRango >= valMin && dentroRango <= valMax){
    console.log('Esta dentro del rango establecido');
} else {
    console.log('Esta fuera del rango establecido');
}

//Ejercicio: Si el padre puede asistir al juego de su hijo
let vacaciones = true, diaDescanso = false;
if(vacaciones || diaDescanso){
    console.log("El padre puede asistir al juego de su hijo")
} else {
    console.log("El padre no puede asistir al juego de su hijo")
}

//Operador ternario
let resultado2 = 3 > 2 ? "Verdadero" : "Falso";
console.log(resultado2);
let numero = 9;
resultado2 = numero % 2 == 0 ? "Es un número PAR" : "Es un número IMPAR";
console.log(resultado2);

//Convertir String a Number
let miNumero = "21"; //Es una cadena
console.log(typeof miNumero);
let edad2 = Number(miNumero);
console.log(typeof edad2);
//Función isNaN
if(isNaN(edad2)){ //No es un número = is Not a Number(devuelve un resultado booleano)
    console.log("Esta variable no contiene solo numeros");
} else {
    if(edad2 >= 18){
        console.log("Puede votar");
    } else {
        console.log("Muy joven para votar");
    }
}

//Operador ternario
let resultado3 = edad2 >= 18 ? "Puede votar" : "Muy joven para votar";
console.log(resultado3);