var nombre = 'Beto';
var apellido = 'Aguilera';
var nombrecompleto = nombre+' '+apellido;
console.log(nombrecompleto); //primera concatencaion

var nombrecompleto2 = 'Antonia'+' '+'Murie';
console.log(nombrecompleto2)//segunda concatenacion

var juntos = nombre + 219; //lee de izq a der siguiendo la cadena lee el numero como strg
console.log(juntos);

juntos = nombre +(78 + 17); //aqui se puede diferenciar a travez de los parentesis
console.log(juntos)

juntos =  78 + 19 + nombre;
console.log(juntos)

nombre += apellido;//Tercera concatenacion usando el operador simplificado
console.log(nombre);

// Hoy ya no se usa var , se utiliza let y const 
let nombre2 = "Pedro";
console.log( nombre2);

const apellido2 = "Lopez";
console.log(apellido2);

let x, y; //se pueden crear varias variables dentro de una misma linea 
x = 17, y = 21; //se puede hacer asignacion de varias variables dentro de la misma linea
let z = x + y; // se asigna el valor de la operacion
console.log(z);

let _1num = 31;//no utilizar numeros para iniciar ek nombre de una variable
let rompiendo = "rompe"; // no utilizar palabras reservadas para variables

console.log(_1num);
console.log(rompiendo);

l