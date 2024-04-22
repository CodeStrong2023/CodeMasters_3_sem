//cración de array
//let autos= new Array('ferrari', 'renaut', 'BMW'); esta es la sintaxis vieja 
const autos =['Ferrari', 'Renault', 'BMW']
console.log(autos);

//recorremos los elementos del arreglo
console.log(autos[0]);
console.log(autos[2]);

for(let i=0; i<autos.length; i++){
console.log(i+' : '+autos[i]);
}

//modificamos los elementos del arreglo
autos[1]= 'volvo';
console.log(autos[1]);

//agrgamos nuevos valores al arreglo
autos.push('Audi');
console.log(autos);

//otras formas de agregar elementos al arreglo
autos[autos.length]= 'Porche';
console.log(autos);

//tercera forma de agregar elementos teniendo CUIDADO
autos[6]= 'Renault';
console.log(autos);

//como preguntar si es un arreglo 
console.log(Array.isArray(autos));//devuelve un booleano

console.log(autos instanceof Array); // pregunta si la variable es una instancia de la clase array