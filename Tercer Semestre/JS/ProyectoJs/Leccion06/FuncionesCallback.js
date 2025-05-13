
miFuncion1()
miFuncion2()

function miFuncion1(){
    console.log('Función 1');
}

function miFuncion2(){
    console.log('Función 2');
}

//Funcion de tipo callback
let imp = function imprimir( mensaje ){
    console.log( mensaje );
}

function sumar(op1, op2, funcionCallBack) {
    let res = op1 + op2;
    funcionCallBack(`Resultado: ${res}`);
}

sumar(5, 3, imp);

//Llamadas asincronicas con uso setTimeout
function miFuncionCallBack(){
    console.log('Saludo asincronico despues de 3 segundos')
}

setTimeout(miFuncionCallBack, 3000);

setTimeout(function() {console.log('Saludo asincronico 2')}, 4000);

setTimeout(() => console.log('Saludos Asincronico 3'), 5000)

let reloj = () => {
    let fecha = new Date();
    console.log(`${fecha.getHours()}:${fecha.getMinutes()}:${fecha.getSeconds()}`);
}

setInterval(reloj, 1000); //Cada 1 segundo se ejecuta
