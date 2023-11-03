//Ejercicio para encontrar numeros pares 
let parImpar = 10;
if(parImpar % 2 == 0){
    console.log("Es un numero Par");
}
else{
    console.log("Es un numero Impar");
}

//Ejercicio es mayor de edad 
let edad = 20, adulto = 18;
if(edad >= adulto){
    console.log("Eres mayor de edad");
}
else{
    console.log("Eres menor de edad");
}

//Dentro de unrango
let dentroRnago = 5; //Aqui vamos a ir cambiando el valor
let valMin = 0, valMax = 10;
if (dentroRnago >= valMax && dentroRnago <= valMax){
    console.log('Está dentro del rango establecido');
} 
else {
    console.log('Esta fuera del rango establecido');
}

//Ejercicio: si el padre puede asistir al juego de su hijo
let vacaciones = true, diaDescanso = false;
if(vacaciones || diaDescanso){
    console.log("El padre puede asistir al juego de su hijo")
}
else{
    console.log("El padre No puede asistir al juego de su hijo")
}

//Operador ternario
let resultado2 = 3 > 2? "Verdadero" : "Falso";
console.log(resultado2);
let numero = 9;
resultado2 = numero % 2 ==0? "Es un numero Par" : "Es un numero impar";
console.log(resultado2)

//Convertir String a Number 
let miNumero = "21";
console.log(typeof miNumero);
let edad2 = Number(miNumero); //esta es una funcion
console.log(typeof edad2);
//Funcion isNAN
if(isNaN(edad2)){ //No es un numero = os Not a Number(devuelve un resultado booleano)
    console.log("La variable no contiene solo numeros")
}
else{
    if(edad2 >= 18){
        console.log("Pede votar");
    }
    else{
        console.log("Muy joven para votar");
   }    
}


let resultado3 = edad2 >= 18? "Puede votar" : "Muy joven para votar";
console.log(resultado3);
