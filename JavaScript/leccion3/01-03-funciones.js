miFuncion(3, 5); // esto es Hosting

function miFuncion(a, b){
    // console.log("Sumamos: " + (a + b));
    return a + b;
}

// Llamar la funcion
miFuncion(5, 4);

let resultado = miFuncion(6,7);
console.log(resultado); 

// Funcion de tipo Expresion

let x = function(a,b){return a+b};
resultado = x(5,6);
console.log(resultado);

// Funcion de tipo Self e Invoking
// Es una funcion anonima y NO se puede reutilizar

(function(a,b){
    console.log("Ejecutando la funcion: "+ (a+b));  
})(3, 1);

console.log(typeof miFuncion);
function miFuncion2(a, b){
    // console.log(arguments);
    console.log(arguments.length);
}

miFuncion2(1,2,3,4,5);

// ToString

var miFuncion3 = miFuncion2.toString();
console.log(miFuncion3);

// Funciones flecha
const sumarFuncionFlecha = (a, b) => a + b;
resultado = sumarFuncionFlecha(3,7) // Asignamos el valor de la variable 
console.log(resultado)

//Funcion tipo expresion
let sumar = function(a, b){
    console.log(arguments[0]) // Muestra el parametro de: a 
    console.log(arguments[1]) // Muestra el parametro de: b

    return a + b+ arguments[2]
}
resultado = sumar(3,2,9) 
console.log(resultado)

//Sumar todos los argumentos
let respuesta = sumarTodo(5, 4, 13, 10, 9)
console.log(respuesta)
function sumarTodo(){
    let suma = 0
    for(let i = 0; i < arguments.length; i++){
        suma += arguments[i]
    }
    return suma
}

//Tipos primitivos
let k = 10
function cambiarValor(a){
    a = 20
}

cambiarValor(k);
console.log(k)

//Paso por referencia
const persona ={
    nombre: 'juan',
    apellido: 'Lopez'
}

function cambiarValorObjeto(p1){
    p1.nombre = 'Ignacio',
    p1.apellido ='Perez'
}

cambiarValorObjeto(persona)
console.log(persona)