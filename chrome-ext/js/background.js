console.log("This is executing - loaded background script");

chrome.runtime.onMessage.addListener(
    function (request, sender, sendResponse) {
        console.log("This is executing - background req");
        if (request) {
            var http = new XMLHttpRequest();
            var url = "http://127.0.0.1:8136";
            var params = "url=" + request["url"];
            http.open("POST", url, true);

            //Send the proper header information along with the request
            http.setRequestHeader("Content-type", "application/x-www-form-urlencoded");

            http.onreadystatechange = function () {//Call a function when the state changes.
                if (http.readyState == 4 && http.status == 200) {
                    console.log("It just works");
                }
            }
            http.send(params);


            // Returns true so that the rating ajax can be sent off asynchronously
            return true;
        }

    }
);
