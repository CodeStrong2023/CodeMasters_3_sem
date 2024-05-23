function aleatorio(min, max){
    return Math.floor(Math.random() * (max -min+1) + min)
}
function eleccion(jugada){
    let resultado = ""
    if(jugada == 1){
        resultado = "Piedra "
    }else if(jugada == 2){
        resultado = "Papel"
    }else if(jugada == 3){
        resultado = "Tijera"
    }else{
        resultado = "Mala Elección"
    }
    return resultado
}    


let jugador = 0
let pc = 0
let triunfos = 0
let perdidas = 0

while(triunfos < 3 || perdidas  > 3){
    pc = aleatorio(1, 3)
    jugador = prompt("Elige : 1 piedra, 2 papel, 3 tijera")

    alert("Pc elige: "+eleccion(pc))
    alert("Tu eliges: "+eleccion(jugador))

//combate
    if(pc == jugador){
        alert("Empate")
    }else if(jugador == 1 && pc ==3){
        alert("Ganaste")
        triunfos += 1
    }else if(jugador == 2 && pc == 1){
        alert("Ganaste")
        triunfos += 1
    }else if(jugador == 3 && pc == 2){
        alert("Ganaste")
        triunfos += 1
    }else{
        alert("PERDISTE")
        perdidas += 1
    }
    alert("Ganaste "+triunfos+" veces. Perdiste "+perdidas+" veces.")

    //Preguntamos si quiere jugar de nuevo
    let continuar = prompt("¿Deseas continuar? (Sí/No)").toLowerCase();
    if (continuar !== "si") {
        break; // Sale del bucle
    }
}
