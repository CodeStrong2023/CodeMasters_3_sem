"use strict";

function _typeof(obj) { if (typeof Symbol === "function" && typeof Symbol.iterator === "symbol") { _typeof = function _typeof(obj) { return typeof obj; }; } else { _typeof = function _typeof(obj) { return obj && typeof Symbol === "function" && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj; }; } return _typeof(obj); }

miFuncion(8, 2); //Llamando a la función

miFuncion(5, 4);
var resultado = miFuncion(6, 7);
console.log(resultado); //Declaramos una fx de tipo expresión

var x = function x(a, b) {
  return a + b;
}; // necesita cierre y punto coma


resultado = x(5, 6);
console.log(resultado); //Funciones de tipo self

(function (a, b) {
  console.log('Ejecutando la función: ' + (a + b));
})(9, 6);

function miFuncion(a, b) {
  return a + b;
}

console.log(_typeof(miFuncion));

function miFuncionDos(a, b) {
  console.log(arguments.length);
}

miFuncionDos(5, 7, 3, 6); // tostring

var miFuncionTexto = miFuncionDos.toString();
console.log(miFuncionTexto); //Funciones flecha

var sumarFuncionFlecha = function sumarFuncionFlecha(a, b) {
  return a + b;
};

resultado = sumarFuncionFlecha(3, 7);
console.log(resultado);

var sumar = function sumar(a, b) {
  console.log(arguments[0]); // Muetsra el parámetro de a

  console.log(arguments[1]);
  a + b + arguments[2];
  return a + b;
};

resultado = sumar(3, 2, 9);
console.log(resultado);
var respuesta = sumarTodo(5, 4, 13, 10, 9);
console.log(respuesta);

function sumarTodo() {
  var suma = 0;

  for (var i = 0; i < arguments.length; i++) {
    suma += arguments[i]; //arguments es para arrAYS
  }

  return suma;
}