let counter = localStorage.getItem("counter");
    if(counter == null) {
        counter = 0;
    } else {
        counter = parseInt(counter);
    }

document.querySelector("#message").innerHTML = counter;



//--------------------Boton Sumar------------------------

document.querySelector("#btn-add").onclick = function() {
    counter++;

    localStorage.setItem("counter", counter);
    document.querySelector("#message").innerHTML = counter;


    }

//-------------------boton Restar-----------------------
document.querySelector("#btn-sub").onclick = function() {
    if (counter > 0){
        counter--;
    } else{
        document.querySelector("#info").innerHTML = "the count cannot be negative";
    }
    
   
    localStorage.setItem("counter", counter);
    document.querySelector("#message").innerHTML = counter;
}


//------------------boton resetear----------------------
document.querySelector("#btn-reset").onclick = function() {
    counter = 0;

    localStorage.setItem("counter", counter);
    document.querySelector("#message").innerHTML = counter;
}

