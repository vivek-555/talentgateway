/**
 * Created by vivek on 24/4/17.
 */

function showLoader(text) {
    if (text) {
        changeLoaderText(text);
    }
    document.getElementById("loader_overlay").style.width = "100%";
}


function hideLoader() {
    document.getElementById("loader_overlay").style.width = "0%";
}

function changeLoaderText(text) {
    $(".progress-message").text(text);
}