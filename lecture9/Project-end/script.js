function showLoading() {
    document.querySelector("#output").innerHTML = "Loading...";
}

//-------------------BOTON search--------------------------------
document.querySelector("#btn-search").onclick = function () {
    
    let name = document.querySelector("#search").value;


    if (name === "") {
        document.querySelector("#output").innerHTML = 
          "Please enter a name";
          return;
        }


    showLoading();
   
    fetch("https://api.agify.io/?name=" + name)

        .then(function (response) {
             return response.json();
        })

        .then(function (data) {

            if(data.age === null) {
                document.querySelector("#output").innerHTML = 
                    "No data available for this name";


           } else {
                document.querySelector("#output").innerHTML =
                    data.name + " might be " + data.age + " years old";
            }
        });
};
