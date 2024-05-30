//let persona3 = new Persona('Carla', 'Ponce'); esto no se debe hacer: persona in not defined

class Persona {
    constructor(nombre, apellido) {
        this.nombre = nombre;
        this.apellido = apellido;
    }

    get nombre() {
        return this._nombre;
    }
    get apellido() {
        return this._apellido;
    }
    set nombre(nombre) {
        this._nombre = nombre;
    }
    set apellido(apellido) {
        this._apellido = apellido;
    }
    // clase 7 parte2
    nombreCompleto(){
        return this._nombre+' '+this._apellido;
    }
    //sobreescribiendo el método de la clase padre
    toString(){ //regresa un string
        //se aplica el polimorfismos que significa = multiples formas en tiempo de ejecucion
        //el méthodo que se ejecuta depende si es una referencia de tipo padre o hija 
        return this.nombreCompleto();
    }
}

class Empleado extends Persona{
    constructor(nombre, apellido, departamento){
        super(nombre, apellido);
        this._departamento = departamento;
    }
    get departamento(){
        return this._departamento;
    }
    set departamento(departamento){
        this._departamento = departamento;
    }
    //sobreescritucara clase 7 parte 2
    nombreCompleto(){
        return super.nombreCompleto()+' '+this._departamento
    }

}

let persona1 = new Persona('Julieta', 'Aguilera');
console.log(persona1.nombre);
persona1.nombre = 'Juan Carlos';
console.log(persona1.nombre);
console.log(persona1.apellido);

let persona2 = new Persona('Lucia', 'Guajardo');
console.log(persona2.nombre);
persona2.nombre = 'Maria Laura';
console.log(persona2.nombre);
console.log(persona2.apellido);


let empleado1 = new Empleado('Maria', 'Gimenez', 'Sistemas');
console.log(empleado1);
console.log(empleado1.nombreCompleto())

//Object.prototype.toString esta es la manera de accceder a a tributos y métodos de manera dinamica
console.log(empleado1.toString())
console.log(persona1.toString())