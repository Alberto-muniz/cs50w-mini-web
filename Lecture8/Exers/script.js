// Creamos una variable llamada counter
// Aquí se guarda el valor del contador
let counter = 0;


// ---------- BOTÓN SUMAR ----------

// Buscamos el botón con id="btn-add"
// Cuando se hace clic, se ejecuta la función
document.querySelector("#btn-add").onclick = function () {

    // Aumentamos el contador en 1
    counter++;

    // Actualizamos el texto del <h1>
    document.querySelector("#message").innerHTML = counter;
};


// ---------- BOTÓN RESTAR ----------

// Buscamos el botón con id="btn-sub"
document.querySelector("#btn-reset").onclick = function () {

    // Disminuimos el contador en 1
    counter--;

    // Actualizamos el texto del <h1>
    document.querySelector("#message").innerHTML = counter;
};


// ---------- BOTÓN RESET ----------

// Buscamos el botón con id="btn-reset"
document.querySelector("#btn-sub").onclick = function () {

    // Reiniciamos el contador a 0
    counter = 0;

    // Actualizamos el texto del <h1>
    document.querySelector("#message").innerHTML = counter;
};


















































































































































