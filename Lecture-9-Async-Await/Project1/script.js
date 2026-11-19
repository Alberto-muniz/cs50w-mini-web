function showLoading() {
    document.querySelector("#output").innerHTML = "Loading...";
}

//-------------------BOTON JOKE--------------------------------
document.querySelector("#btn-joke").onclick = function () {

    showLoading();
   
    fetch("https://official-joke-api.appspot.com/random_joke")

        .then(function (response) {
             return response.json();
        })

        .then(function (data) {
             document.querySelector("#output").innerHTML =
                data.setup + "<br><br> " + data.punchline;
        })

        .catch(function () {
            document.querySelector("#output").innerHTML = 
            "Error loading joke";
        });
};

//--------------BOTON ADVICE------------------------------------------
document.querySelector("#btn-advice").onclick = function () {
    
    showLoading();

    fetch("https://api.adviceslip.com/advice")

        .then(function(response) {
            return response.json();
 
   })
   
        .then(function(data) {

            document.querySelector("#output").innerHTML =
           " 💡" + data.slip.advice;
        })

        .catch(function () {
            document.querySelector("#output").innerHTML =
                "Error loading advice ";
        });

};
//--------------------BOTON CAT FACT------------------------------------
document.querySelector("#btn-cat").onclick = function() {

    showLoading()

    fetch("https://catfact.ninja/fact")

        .then(function(response) {
            return response.json();
        })

        .then(function (data) {
            document.querySelector("#output").innerHTML = 
            "miau " + data.fact;
        })

        .catch(function (){
            document.querySelector("#output").innerHTML =
                "Error loading cat fact"
        })

    
}