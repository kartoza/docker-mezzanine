window.addEventListener("DOMContentLoaded", function (e) {

    var stage = document.getElementById("stage");
    var fadeComplete = function (e) {
        stage.appendChild(arr[0]);
    };
    var arr = stage.getElementsByTagName("img");
    for (var i = 0; i < arr.length; i++) {
        arr[i].addEventListener("animationend", fadeComplete, false);
    }

}, false);
