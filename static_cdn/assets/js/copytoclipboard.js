function copy(copyId){
    let inputElement = document.createElement("input");
    inputElement.type = "text";
    let copyText = document.getElementById(copyId).innerHTML;
    inputElement.value = copyText;
    document.body.appendChild(inputElement);
    inputElement.select();
    document.execCommand('copy');
    document.body.removeChild(inputElement);

    document.getElementById("alert1").style.display = "block";
    setTimeout(function(){
        document.getElementById("alert1").style.display = "none";
    }, 1000);
    document.getElementById("alert2").style.display = "block";
    setTimeout(function(){
        document.getElementById("alert2").style.display = "none";
    }, 1000);
    document.getElementById("alert3").style.display = "block";
    setTimeout(function(){
        document.getElementById("alert3").style.display = "none";
    }, 1000);
}