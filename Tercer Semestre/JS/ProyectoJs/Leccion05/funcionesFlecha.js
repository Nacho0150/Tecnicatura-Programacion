

function miFuncion(){
    console.log('Saludos desde mi funcion');
}
miFuncion();

let myFuncion = function () {
    console.log('Saludos desde la función anonima');
}

//Ahora vamos a crear una función flecha
let miFuncionFlecha = () => {
    console.log('Saludos desde mi funcion flecha'); 
}
//Hay mas variantes para funciones flecha que vamos a ir viendo
miFuncionFlecha();

//lo hacemos en una línea
const saludar = () => console.log('Saludos a todos desde esta función flecha');

saludar();

//otro ejemplo
const saludar2 = () => {
    return 'Saludos desde la función flecha dos';
}

console.log(saludar2());

//Simplificamos la función anterior
const saludar3 = () => 'Saludos desde la función flecha tres';

console.log(saludar3());

//Continuamos con otro ejemplo
const regresaObjeto = () => ({nombre: 'Juan', apellido: 'Lara'});

console.log(regresaObjeto());

//Funciones que reciben parámetros
const funcionParametros = ( mensaje ) => console.log( mensaje );

funcionParametros('saludos desde esta función con parámetros');

//Una función clásica
const funcionParametrosClasica = function( mensaje ){
    console.log( mensaje );
}

funcionParametrosClasica('Saludos desde la función clásica');

//Se pueden omitir los paréntesis en la función flecha de la siguiente manera
const funcionConParametros = mensaje => console.log( mensaje );

funcionConParametros('Otras forma de trabajar con función flecha');

//Ahora vemos funciones flecha con varios parámetros
//Podemos abrir la función y tener más cosas dentro de ella
const funcionConParametros2 = (op1, op2) => {
    let resultado = op1 + op2;
    return resultado;
}

console.log(funcionConParametros2(3, 5)); 