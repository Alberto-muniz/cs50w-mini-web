let counter = localStorage.getItem("counter");
if (counter === null) {
    counter = 0;
} else {
    counter = parseInt(counter);
}

document.querySelector("#message").innerHTML = counter;


// ---------- BOTÓN SUMAR ----------

document.querySelector("#btn-add").onclick = function () {
    counter++;
    localStorage.setItem("counter", counter);
    document.querySelector("#message").innerHTML = counter;
};


// ---------- BOTÓN RESTAR ----------

document.querySelector("#btn-sub").onclick = function () {
    if (counter > 0) {
        counter--;
    }
    localStorage.setItem("counter", counter);
    document.querySelector("#message").innerHTML = counter;
};


// ---------- BOTÓN RESET ----------

document.querySelector("#btn-reset").onclick = function () {
    counter = 0
    localStorage.setItem("counter", counter);
    document.querySelector("#message").innerHTML = counter;
};