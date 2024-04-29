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