// Buscamos el botón en el HTML
document.querySelector("#btn-joke").onclick = function () {

    // Usamos fetch para pedir datos a una API (internet)
    fetch("https://official-joke-api.appspot.com/random_joke")

        // Cuando llega la respuesta...
        .then(function (response) {

            // Convertimos la respuesta a JSON
            return response.json();
        })

        // Cuando ya tenemos el JSON...
        .then(function (data) {

            // data contiene el chiste
            // Tiene dos partes: setup (inicio) y punchline (remate)

            // Mostramos el chiste en el <p>
            document.querySelector("#joke").innerHTML =
                data.setup + " 😂 " + data.punchline;
        });
};
