'use strict'
// Veamos como evitar este error
try {
    let x = 10; //Lo traemos con alt + flecha hacia arriba o hacia abajo
    // miFuncion(); //Capturamos el error de la función
    throw'Mi Error';
} catch (error) { //Catchamos el error
    console.log(typeof(error)); 
} finally {
    console.log('Termina la revisión de errores')
}

//La ejecucion ahora continua...
console.log('Continuamos...') //Esto no se llega a ver porque esta bloqueado

let resultado = 'hola';

try {
    // y = 5;
    if(isNaN(resultado)) throw 'No es un número';
    else if (resultado === '')throw 'Es una cadena vacia';
    else if (resultado >= 0)throw 'Valor positivo';
    else if (resultado <= 0)throw 'Valor positivo';
} catch(error) {
    console.log(error);
    console.log(error.name);
    console.log(error.message);
} finally {
    console.log('Termina la revision de errores 2')
}