//Ejercicio 1: Calcular estación del año
let mes = 4;
let estacion; //Undefined
if(mes == 1 || mes == 2 || mes == 12){
    estacion = "Verano";
} else if(mes == 3 || mes == 4 || mes == 5){
    estacion = "Otoño";
} else if(mes == 6 || mes == 7 || mes == 8){
    estacion = "Invierno";
} else if(mes == 9 || mes == 10 || mes == 11){
    estacion = "Primavera";
} else {
    estacion = "Valor incorrecto";
}
console.log("El valor corresponde a la estación de: " + estacion);

//Ejercicio 2: Hora del día
let horaDia = 9;
let mensaje;
if(horaDia >= 6 && horaDia <= 11){
    mensaje = "Good Morning";
} else if(horaDia >= 12 && horaDia <= 16){
    mensaje = "Good Afternoon";
} else if(horaDia >= 17 && horaDia <= 19){
    mensaje = "Good Evening";
} else if(horaDia >= 20 && horaDia <= 23){
    mensaje = "Good Night";
} else {
    mensaje = "Valor incorrecto";
}
console.log(mensaje);

//Estructura switch(la sintaxis es igual a Java)
switch(mes){
    case 1: case 2: case 12:
        estacion = "Verano";
        break;
    case 3: case 4: case 5:
        estacion = "Otoño";
        break;
    case 6: case 7: case 8:
        estacion = "Invierno";
        break;
    case 9: case 10: case 11:
        estacion = "Primavera";
        break;
    default:
        estacion = "Valor incorrecto";
}
console.log("Bienvenido a la estación de: " + estacion);

//Ampliando el uso de var let y const
/*
Con var puedes reasignar en cualquier momento
este forma parte del ambito global
Un error es que sesobreescriba su scot
*/

var nombre = 'Ariel';
nombre = 'Osvaldo';
console.log(nombre);

function saludar(){
    var nombre3 = 'Natalia';
    console.log(nombre3);
}
//console.log(nombre3); //Aquí no lee el dato en la función

if(true){
    var edad = 34;
    console.log(edad);
}
console.log(edad); //En la dunción funciono correctamente, en la estructura if fallo

/*
let: esta puede ser reasignada en cualquier en cualquier momento
la diferencia es que su ambito es de bloque,
solo disponible dentro de un bloque de llaves
o dentro de una funcion
*/

function saludar2(){
    let nombre2 = 'Ariel';
    console.log(nombre2);
}
//console.log(nombre2);

if(true){
    let nombre2 = 33;
    console.log(nombre2);
}
//console.log(edad2);

/*
const se utiliza para valores constantes que no pueden ser reasignadas
*/

const fechaNacimiento = 2006;
console.log(fechaNacimiento);
//fechaNacimiento = 2003;
//console.log(fechaNacimiento); //solo se ejecuta el console anterior

//Enviar repetir tu código
//Dry don't repeat yourself

let days = 5;
switch (days) {
    case 1:
        console.log('hoy es Lunes');
        break;
    case 2:
        console.log('hoy es Martes');
        break;
    case 3:
        console.log('hoy es Miércoles');
        break;
    case 4:
        console.log('hoy es Jueves');
        break;
    case 5:
        console.log('hoy es Viernes');   
        break;
    case 6:
        console.log('hoy es Sábado');
        break;
    case 7:
        console.log('hoy es Domingo');   
        break; 
    default:
        console.log('Error en el ingreso del día de la semana');   
        break;
}

//Esta es la opción mejorada

let days2 = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo'];
function getDay(n){
    if(n < 1 || n > 7) {
        throw new Error('out of range');
    }
    return days2[n-1];
}
console.log(getDay(3));

//Hacer un ejercicio similar al que esta hecho, pero ahora con los
//meses del año, debes hacerlo con la estructura switch y luego con
//la función en la opción mejorada

let month = 5;
switch (month) {
    case 1:
        console.log('Estamos en Enero');
        break;
    case 2:
        console.log('Estamos en Febrero');
        break;
    case 3:
        console.log('Estamos en Marzo');
        break;
    case 4:
        console.log('Estamos en Abril');
        break;
    case 5:
        console.log('Estamos en Mayo');   
        break;
    case 6:
        console.log('Estamos en Junio');
        break;
    case 7:
        console.log('Estamos en Julio');   
        break;
    case 8:
        console.log('Estamos en Agosto');   
        break;
    case 9:
        console.log('Estamos en Septiembre');   
        break;
    case 10:
        console.log('Estamos en Octubre');   
        break;
    case 11:
        console.log('Estamos en Noviembre');   
        break;
    case 12:
        console.log('Estamos en Diciembre');   
        break; 
    default:
        console.log('Error en el ingreso del día de la semana');   
        break;
}

//Esta es la opción mejorada

let month2 = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'];
function getMonth(n){
    if(n < 1 || n > 7) {
        throw new Error('out of range');
    }
    return month2[n-1];
}
console.log(getMonth(3));