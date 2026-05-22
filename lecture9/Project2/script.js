function showLoanding() {
    document.querySelector("#outpunt").innerHTML = "Loading";
}



//-------------------Button JOKE-----------------------------------------
document.querySelector("#btn-joke").onclick = async function () {

    showLoanding();

    try {
        let response = await fetch("https://official-joke-api.appspot.com/random_joke")
        let data = await response.json();

        document.querySelector("#output").innerHTML = 
            data.setup + "<br><br>" + data.punchline;
    } catch (error) {
        cument.querySelector("#output").innerHTML =
            "Error loading joke";
    }
    };

//----------------------button ADVICE-------------------------------------
document.querySelector("#btn-advice").onclick = async function () {

    showLoading();

    try {
        let response = await fetch("https://api.adviceslip.com/advice");
        let data = await response.json();

        document.querySelector("#output").innerHTML =
             data.slip.advice;

    } catch (error) {
        document.querySelector("#output").innerHTML =
            "Error loading advice";
    }
    
};

//-------------------boton CAT----------------------------------------
document.querySelector("#btn-cat").onclick = async function () {

     showLoading();

    try {
        let response = await fetch("https://catfact.ninja/fact");
        let data = await response.json();

        document.querySelector("#output").innerHTML =
            "🐱 " + data.fact;

    } catch (error) {
        document.querySelector("#output").innerHTML =
            "Error loading cat fact";

    }
};

// -------- BOTÓN SEARCH --------
document.querySelector("#btn-search").onclick = async function () {

    let name = document.querySelector("#search").value;

    if (name === "") {
        document.querySelector("#uotput").innerHTML = 
            "Please enter a name";
            return;
    }

    showLoanding();
    try{
        let response = await fetch("https://api.agify.io/?name=" + name);
        let data = await response.json();

        if(data.age ==null) {
            document.querySelector("#output").innerHTML = 
                "No avaliable for this name";
        } else {
            document.querySelector("#output").innerHTML = 
                data.name + "might be " + data.age + "years old"
        }

    } catch (error) {
        document.querySelector("#uotput").innerHTML = 
            "Error loading data "

    }
};

