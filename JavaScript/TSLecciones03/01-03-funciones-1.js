miFuncion(8,2);




//Llamando a la función
miFuncion(5,4);

let resultado = miFuncion(6,7)
console.log(resultado)

//Declaramos una fx de tipo expresión
let x = function(a,b){return a+b}; // necesita cierre y punto coma
resultado = x(5,6)
console.log(resultado);


//Funciones de tipo self

(function(a,b){
    console.log('Ejecutando la función: '+ (a+b));
})(9,6);

function miFuncion(a, b) {
    return a + b;
}

console.log(typeof miFuncion);

function miFuncionDos(a, b) {
    console.log(arguments.length);
}

miFuncionDos(5, 7, 3, 6);
// tostring
var miFuncionTexto = miFuncionDos.toString();
console.log(miFuncionTexto);

//Funciones flecha
const sumarFuncionFlecha = (a,b) => a+b;
resultado= sumarFuncionFlecha(3,7);
console.log(resultado)

let sumar=  function(a,b){
    console.log(arguments[0]);  // Muetsra el parámetro de a
    console.log(arguments[1])
    a+b+arguments[2];
    return a+ b;
}
resultado =  sumar(3,2,9);
console.log(resultado)

let respuesta = sumarTodo(5,4,13,10,9);
console.log(respuesta);
function sumarTodo(){
    let suma = 0;
    for(let i = 0; i<arguments.length; i++){
        suma += arguments[i] //arguments es para arrAYS
    }
    return suma;
}
