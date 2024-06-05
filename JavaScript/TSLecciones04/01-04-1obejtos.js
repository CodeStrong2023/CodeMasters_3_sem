let x = 10;
console.log(x.length);

let persona = {
    nombre: "Carlos",
    apellido: "Gil",
    email: "zuloagabalacom",
    edad: 30,    
    nombreCompleto: function(){
        return this.nombre+' '+this.apellido;
    }
}
console.log(persona.nombre); 
console.log(persona.apellido)
console.log(persona.email)
console.log(persona.edad)
console.log(persona.nombreCompleto());

let persona2 = new Object()
persona2.nombre = 'Juan';
persona2.direccion = 'Xelada';
persona2.telefono = '2613352502';
console.log(persona2.telefono);

console.log(persona['apellido']);  //ACCEDEMOS COMO SI FUERA ARREGLO

for(propiedad in persona ){
    console.log(propiedad);
    console.log(persona[propiedad])
}

persona.apellido = "Ignacio Bala";
console.log(persona);