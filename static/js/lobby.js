var ready = false;
var infoTimer = undefined;

function getPlayers() {
    fetch('/enter', {
        // Specify the method
        method: 'POST',
        // A JSON payload
        // redirect: 'follow',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({'name': name})
        })
    .then(function (response) { 
         // At this point, Flask has printed our JSON
        return response.text();
    }).then(function (text) {
        // Should be 'OK' if everything was successful
        console.log(text)
        window.location = "/lobby";
        });
}

function enterGame(jsonObj) {
    console.log("Trying to enter game");
    let canEnter = false;
    fetch('/enter', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: jsonObj
    }).then(function (response) {
        return response;
    }).then(function (response) {
        console.log(response.status);
        if (response.status == 500) {
           canEnter = false;
        } else {
            console.log("Im gonna send you to the game page");
            canEnter = true;
            window.location = "/game";
        }
    });
    return canEnter;
}

function getInfo() {
    fetch('/gameInfo', {
        // Specify the method
        method: 'GET',
        // A JSON payload
        // redirect: 'follow',
        
        })
    .then(function (response) { 
         // At this point, Flask has printed our JSON
        return response.json()
    }).then(function (jsonData) {
        // Should be 'OK' if everything was successful

        var allReady = true;

        console.log(jsonData);
        console.log("Json = " + jsonData);
        var table = document.getElementById("nameTable");

        table.innerHTML = "";

        for (var i = 0; i < jsonData.players.length; i++) {
            
            row = table.insertRow(i);
            var name = jsonData.players[i].name;
            var cell1 = row.insertCell(0);
            var cell2 = row.insertCell(1);
            cell1.innerHTML = name;
            if (jsonData.players[i].ready === false) {
                cell2.innerHTML = "Not Ready";
                allReady = false;
            } else {
                cell2.innerHTML = "Ready";
            }
            
        }

        if (allReady === true && jsonData.players.length > 1) {
            let result = enterGame(jsonData);
            console.log("Enter Game result = " + result);
            if (result === true) {
                clearInterval(infoTimer);
                console.log("setting location to game")
               
            } else {
                // setInterval(infoTimer);
                alert(console.log("cant join game yet"));
            }
        }
    });
}

function setReady() {
    if (ready === true) {
        return;
    }
    ready = true;
    fetch('/ready', {
        // Specify the method
        method: 'GET',
        // A JSON payload
        // redirect: 'follow',
        })
    .then(function (response) { 
         // At this point, Flask has printed our JSON
        return response.text();
    }).then(function (text) {
        // Should be 'OK' if everything was successful
        console.log(text)
        // window.location = "/lobby";
        });
}

const readyBtn = document.getElementById("readyBtn");
readyBtn.addEventListener("click", setReady, false);
infoTimer = setInterval(getInfo, 3000);