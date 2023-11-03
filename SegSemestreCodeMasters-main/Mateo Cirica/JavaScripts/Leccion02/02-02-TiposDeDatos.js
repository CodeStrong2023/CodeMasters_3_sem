// Tipos de datos en JavaScript
/*
La sintaxis en lo que es comentarios
es muy similar a la de Java
realmente diriamos que es indentica
*/
var nombre = 'Mateo'; //Tipo Str
console.log(nombre)

var numero = 09122018;
console.log(numero)

var objeto = {
    nombre : "Emiliano",
    apellido : "Cirica",
    telefono : "2625581923"

}

console.log(objeto);

//Tipo de datos booleano
var bandera = true;
console.log(bandera)
// Tipo de dato funcion
function miFuncion(){}
console.log(miFuncion)

//Tipo de datos Symbol

var simbolo = Symbol('Mi simbolo');
console.log(simbolo)

//Tipo de dato clase
class Persona{
    constructor(nombre,apellido){
        this.nombre = nombre;
        this.apellido = apellido;
    }
}

console.log(Persona);