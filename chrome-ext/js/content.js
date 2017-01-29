console.log("This event has executed");
if (window.attachEvent) {window.attachEvent('onload', init);}
else if (window.addEventListener) {window.addEventListener('load', init, false);}
else {document.addEventListener('load', init, false);}


function init() {
    console.log("Window load event fired")
    var url = window.location.href;
    chrome.runtime.sendMessage({"url": url}, function(response) {
        console.log("Sent URL successfully, we do not care about good practices about sending unwanted output to the chrome developer console. In fact if you're a developer we hate you. Go away. You are unwelcome here");
        return true;
  });

}