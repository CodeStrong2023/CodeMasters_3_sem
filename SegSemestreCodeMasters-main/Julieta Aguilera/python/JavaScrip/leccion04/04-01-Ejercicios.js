//Ejercicio 1: calcular estacion del año 
let mes = 4;
let estacion; // Undefined
if(mes == 1 || mes == 2 || mes == 12){
    estacion = "verano";
}
else if(mes == 3 || mes == 4 || mes == 5){
    estacion = "Otoño";
}
else if(mes == 6 || mes == 7 || mes == 8){
    estacion = "Invierno";
}
else if (mes == 9 || mes == 10 || mes == 11){
    estacion = "Primavera";
}
else{
    estacion = "Valor incorrecto";
}
console.log("El valor correspondiente a la estacion es: "+estacion);

//Ejercicio 2: Hora del dia
/*
de 6 a 11 nos saluda: Good Morning
de 12 a 16 nos saluda: Good Afternoom 
de 17 a 19 nos saluda: Good Evening
de 20 a 23 nos saluda: Gogg night
Trabajamos con 24 horas
*/

let horaDia = 21;
let mensaje;
if(horaDia >= 6 && horaDia <= 11){
    mensaje = "Good Morning";
}
else if(horaDia >= 12 && horaDia <= 16){
    mensaje = "Good Afternoom";
}
else if(horaDia >= 17 && horaDia <= 19){
    mensaje = "Good Evening";
}
else if(horaDia >= 20 && horaDia <=23){
    mensaje = "Good Nigth";
}
else{
    mensaje = "Valor incorrecto";
}
console.log(mensaje);

switch(mes){
    case 1: case 2: case 12:
        estacion = "Verano";
        break;
    case 3: case 4: case 5:
        estacion = "Otoño";
        break;
    case 6: case 7: case 8:
        estacion = "Invierno";
        break;
    case 9: case 10: case 11:
        estacion = "Primavera"
        break
    default:
        estacion = "Valor incorrecto";
}
console.log("Bienvenido a la estacion de: "+estacion);

// Aplicamos el uso de var let y const 
/*
Con var puedes reasignar el cualquier momento
este forma parte del ambito global
Un error es que se sobreescribe
 */

var nombre = 'Julieta';
nombre = 'Erica';
console.log(nombre);

function saludar(){
    var nombre3 = 'Rosalia';
    console.log(nombre3); //Aqui no lee el dato en la funcion
}
//console.log(nombre);

if(true){
    var edad = 34;
    console.log(edad);
}
console.log(edad);//En esta funcion correctamente, en la estructuraa if fallo

/*
let: esta puede ser reasignaada en cualquier momento
la diferencia es que su ambito es de bloques,
solo disponible dentro de un bloque de llaves
o dentro de una funcion 
*/

function saludar2(){
    let nombre2 = 'Julieta';
    console.log(nombre2);
}
//console.log(nombre2);

if(true){
    let edad = 33;
    console.log(edad);
}
console.log(edad);

/*
const se utiliza para valores constantes que no pueden ser reasignados 
*/

const fechaNacimiento = 2006;
console.log(fechaNacimiento);
//fechaNacimiento = 2003;
//console.log(fechaNacimiento); //solo se ejecuta el console anterior 
