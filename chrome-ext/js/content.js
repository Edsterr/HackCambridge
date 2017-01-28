window.addEventListener ("load", init, true);

function init() {

    var url = window.location.href;
    chrome.runtime.sendMessage({"url": url}, function(response) {
        console.log("Sent URL successfully, we do not care about good practices about sending unwanted output to the chrome developer console. In fact if you're a developer we hate you. Go away. You are unwelcome here");
    });
}