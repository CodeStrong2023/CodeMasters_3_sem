let x = 10; //varible tipo primitivo
console.log(x.lenght);
console.log("tipos primitivos");

// Objeto
let persona ={
    nombre: "Romina",
    apellido: "Rodriguez",
    email: "romi@gmail.com",
    edad: 36,
    idioma: 'es', 
    get lang(){
        return this.idioma.toUpperCase(); //Convierte las minusculas en mayusculas
    },
    set lang(lang){
        return this.idioma = lang.toUpperCase();
    },
    nombreCompleto: function(){//Método o función
        return this.nombre+" "+this.apellido;
    },
    get nombreEdad(){
        return 'El nombre es: '+this.nombre+', Edad: '+this.edad;
    }
    
}
console.log(persona.nombre);
console.log(persona.apellido);
console.log(persona.edad);
console.log(persona.email);
console.log(persona);
console.log(persona.nombreCompleto());
console.log("Ejecutando con un objeto");

let persona2 = new Object();//debe crear un nuevo objeto en memoria
persona2.nombre = "Juan";
persona2.direccion = "Salada 14";
persona2.telefono = "2613458790";
console.log(persona2.telefono);
console.log("Creamos un nuevo objeto");
console.log(persona["apellido"]);//accedemos como si fuera un arreglo
console.log("Usamos un ciclo for");

//For in y accedemos al objeto como un arreglo
for(propiedad in persona){
    console.log(propiedad);
    console.log(persona[propiedad]);
}
console.log("comabiamos y eliminamos un error");

persona.apellido = "Betancud";//cambiamos dinamicamente un valor del objeto
delete persona.apellido;//borramos el error que teniamos
console.log(persona);

//Distinta formas de imprimir un objeto
//Numero 1: la más sencilla: concatenar cada valor de cada propiedad
console.log("//Distinta formas de imprimir un objeto: forma1");
console.log(persona.nombre+" "+persona.apellido);

//Número 2: a traves del ciclo for
console.log("//Distinta formas de imprimir un objeto: forma 2");
for(nombrePropiedad in persona){
    console.log(persona[nombrePropiedad]);
}

//Número 3: La función objet.value()
console.log("Distinatas formas de imprimir un objeto: forma 3");
let personaArray = Object.values(persona);
console.log(personaArray);

// Número 4: Utilizamos el método JSON.srtingify
console.log("//Distinta formas de imprimir un objeto: forma 4");
let personaString = JSON.stringify(persona);
console.log(personaString);

console.log('Comenzamos a usar el metodo get');
console.log(persona.nombreEdad);

console.log('Comenzamos el metodo get y set para idiomas');
persona.lang = 'en'
console.log(persona.lang);

function Persona3(nombre, apellido, email){
    this.nombre = nombre;
    this.apellido = apellido;
    this.email = email;
    this.nombreCompleto = function(){
        return this.nombre+' '+this.apellido;
    }
}
let padre = new Persona3('Leo', 'lopez', 'lopez@gmail.com');
padre.nombre = 'Luis' // Modificamos el nombre
padre.telefono = '46374857384' //Propiedad exclusiva del objeto padre
console.log(padre);
console.log(padre.nombreCompleto()); //Utilizamos la funcion

let madre = new Persona3('Laura', 'Contrera', 'contrera@gmail.com');
console.log(madre);
console.log(madre.telefono); //La propiedad no esta definida
console.log(madre.nombreCompleto());

//Diferentes formas de crear objetos
//Caso objeto 1
let miObjeto = new Object(); //Formal
//Caso objeto 2
let miObjeto2 ={}; //Sintaxis Recomendada

//Caso String 1
let miCadena1 = new String('Hola'); //Formal
//Caso String 2
let miCadena2 = 'Hola'; //Sintaxis recomendada
 
//Caso con números 1
let miNumero = new Number(1); //Formal
//Caso con números 2
let miNumero2 = 1; //Sintaxis recomendada

//Caso boolean 1
let miBoolean = new Boolean(false); //Formal
//Caso boolean 2
let miBoolean2 = false; //Sintaxis recomendada

//Caso Arreglos 1
let miArreglo = new Array(); //Formal
//Caso Arreglos 2
let miArreglo2 = []; //Sintaxis recomendada

//Caso function 1
let miFuncion = new function(){}; //Formal
//Caso function 2
let miFuncion2 = function(){}; //Sintaxis recomendada

//Uso de prototype
Persona3.prototype.telefono = '2435267890';
console.log(padre);
console.log(madre.telefono);
madre.telefono = '46374857384';
console.log(madre.telefono);

//Uso de call
let persona4 ={
    nombre: 'Juan',
    apellido: 'Perez',
    nombreCompleto2: function(titulo, telefono){
        return titulo+': '+this.nombre+' '+this.apellido+' '+telefono;
        //return this.nombre+' '+this.apellido;
    }
}

let persona5 = {
    nombre: 'Carlos',
    apellido: 'Lara'
}

console.log(persona4.nombreCompleto2('Lic.', '5492618484845'));
console.log(persona4.nombreCompleto2.call(persona5, 'Ing.', '5492618484845'));

//Método Apply
let arreglo = ['Ing.', '5492618484845'];
console.log(persona4.nombreCompleto2.apply(persona5, arreglo));
