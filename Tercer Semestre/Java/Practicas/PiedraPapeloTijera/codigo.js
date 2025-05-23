let opc = "";

do {
  function numAleatorio(max, min) {
    return Math.floor(Math.random() * (max - min + 1) + min);
  }

  // 1 Piedra
  // 2 Papel
  // 3 Tijera
  let jugador = 0;
//   let max = parseInt(prompt("Ingrese el valor máximo del rango:"));
//   let min = parseInt(prompt("Ingrese el valor mínimo del rango:"));

  //Valido que sean número los ingresados como max y min. Además verifico que min < max
//   if (isNaN(max) || isNaN(min) || min >= max) {
//     alert(
//       "Ha ingresado valores incorrectos. Solo se puede ingresar números y el mínimo debe ser menor al máximo"
//     );
//   } else {
    let triunfos = 0;
    let perdidas = 0;
    let pc = 0;

    while (triunfos < 3 && perdidas < 3) {
      pc = numAleatorio(1, 3);
      jugador = prompt("Elige: 1 Piedra, 2 Papel, 3 Tijera");
      //Elección jugador
      if (jugador == 1) {
        alert("Elegiste Piedra");
      } else if (jugador == 2) {
        alert("Elegiste Papel");
      } else if (jugador == 3) {
        alert("Elegiste Tijera");
      } else {
        alert("Elegiste Perder");
      }

      //Elección PC
      if (pc == 1) {
        alert("PC eligió Piedra");
      } else if (pc == 2) {
        alert("PC eligió Papel");
      } else if (pc == 3) {
        alert("PC eligió Tijera");
      }

      //Combate
      if (pc == jugador) {
        alert("Empate");
      } else if (jugador == 1 && pc == 3) {
        alert("El Jugador ha ganado");
        triunfos++;
      } else if (jugador == 2 && pc == 1) {
        alert("El Jugador ha ganado");
        triunfos++;
      } else if (jugador == 3 && pc == 2) {
        alert("El Jugador ha ganado");
        triunfos++;
      } else {
        alert("Perdiste");
        perdidas++;
      }
    // }
    }
  alert("Ganaste " + triunfos + " veces. Perdiste " + perdidas + " veces.");

  //Elección de seguir jugando
  opc = prompt("Desea seguir jugando? S/N");
} while (opc.toLocaleUpperCase() === "S");
