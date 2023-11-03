var nombre = "Romina";
var apellido = "Rodriguez";
var nombreCompleto = nombre+" "+apellido;//Primera concatenación
console.log(nombreCompleto);
var nombreCompleto2 = "Ariel"+" "+"Betancud";//Segunda concatenación
console.log(nombreCompleto2);
var juntos = nombre + 219;
console.log(juntos)
juntos + 78 + 17;
console.log(juntos);
juntos = 78 + 17 + nombre;
console.log(juntos);

nombre += apellido;//Tercera concatenación usando el operador simplificado
console.log(nombre);

// Hoy ya no se usa var, se utiliza let y const
let nombre2 = "Pedro";
console.log(nombre2);

const apellido2 = "Lepes";
//apellido2 = "Peres";una costante no puede ser modificada
console.log(apellido2);

let x, y; //Se pueden crear varias variables dentro de una misma línea
x = 17, y = 21; //Se puede hacer asignación de varias variables dentro de la misma
let z = x +y;//Se le asigna el valor de la operación
console.log(z);

let _1num = 31;//No utilizar numeros para el inicio de una variable
let rompiendo = "rompe";//No se pueden utilizar palabras reservadas para inicializar una variable
console.log(_1num);
console.log(rompiendo);