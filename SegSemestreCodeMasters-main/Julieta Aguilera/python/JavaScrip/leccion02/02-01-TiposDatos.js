//Tipos de datos en javascript
/*
La sintaxis en los comentarios 
es muy similar a la de java
 */
var nombre = 'Julieta'; //Tipo Str
console.log(typeof nombre);
nombre = 7;
console.log(nombre);

var numero = 3000; //Tipo numerico
console.log(typeof numero);
nombre = 11.3;
console.log(typeof nombre)
var objeto = {
    nombre: "Julieta",
    apellido: "Aguilera",
    telefono: 2604341029

}
console.log(typeof objeto);

//Tipo de dato boolean
var bandera = true;
console.log(typeof bandera);

//Tipo de dato funcion
function miFuncion(){}
console.log(typeof miFuncion);

//Tipo de dato symbol
var simbolo = Symbol("Mi simbolo");
console.log(simbolo);

//Tipo de dato Clase
class Persona{
    constructor(nombre, apellido){
        this.nombre = nombre;
        this.apellido = apellido;

    }
}

console.log(typeof Persona);
//Tipo de dato undefined 
var x;
console.log(typeof x);

//null: significa ausencia de valor
var y = null; //null no es un tipo de dato pero su origen es objet
console.log(typeof y);

//Tipo de dato array y Empery string
//para definir array(arreglos) se debe usar corchetes
var autos = ['Citroen', 'Audi', 'BMW', 'Ford'];
console.log(autos);
console.log(typeof autos)

var z= '';
console.log(z); //esto se refiere a que es una cadena vacia:
console.log(typeof z)
