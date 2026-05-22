//-------------------BOTON JOKE--------------------------------
document.querySelector("#btn-joke").onclick = function () {

    document.querySelector("#output").innerHTML = "Loading...";
    fetch("https://official-joke-api.appspot.com/random_joke")

        .then(function (response) {
             return response.json();
        })

        
        .then(function (data) {
             document.querySelector("#output").innerHTML =
                data.setup + "<br><br> " + data.punchline;
        });
};

//--------------BOTON ADVICE------------------------------------------
document.querySelector("#btn-advice").onclick = function () {
    document.querySelector("#output").innerHTML = "Loading...";
    fetch("https://api.adviceslip.com/advice")

        .then(function(response) {
            return response.json();
 
   })
   
        .then(function(data) {

            document.querySelector("#output").innerHTML =
           " 💡" + data.slip.advice;

   });
};

