// Tipos de Datos en JavaScript
/*
La sintaxis en lo que es comentarios
es muy similar a la de Java
realmente diriamos que es identica
*/
//Tipo String
var nombre = 'Ariel'; 
console.log(nombre);

//Tipo Numérico
var numero = 3000; 
console.log(numero);

//Tipo Object
var objeto = {
    nombre : "Ariel",
    apellido : "Betancud",
    telefono : "2614567893"
}
console.log(objeto);

//Tipo de dato boolean
var bandera = true;
console.log(bandera);

//Tipo de dato funcion
function miFuncion(){}
console.log(miFuncion);

//Tipo de dato symbol
var simbolo = Symbol("Mi simbolo")
console.log(simbolo);

//Tipo de dato clase
class Persona{
    constructor(nombre,apellido){
        this.nombre = nombre;
        this.apellido = apellido;
    }
}

console.log(Persona);

//Tipo de dato undefined
var x;
console.log(x);

x = undefined;
console.log(typeof x);

// null: significa ausencia de valor
var y = null; //null no es un tipo de dato, pero su origen es de tipo object
console.log(typeof y);

//Tipo de dato array y Empty String
var autos = ['Citroen','Audi','BMW','Ford'];
console.log(autos);
console.log(typeof autos); //Preguntamos que tipo de dato es:

var z = '';
console.log(z); //Esto se refiere a que es una cadena vacía:
console.log(typeof z);