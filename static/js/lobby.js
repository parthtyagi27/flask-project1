var ready = false;

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
    alert("Called entergame");
    fetch('/enter', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(jsonObj)
    }).then(function (response) {
        return response.json();
    }).then(function (response) {
        console.log(response);
        return response;
    });
}

var infoTimer = null;

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
        var table = document.getElementById("playerTable");

        for (var i = 1; i < table.rows.length; i++) {
            table.deleteRow(i);
        }

        for (var i = 0; i < jsonData.players.length; i++) {
            
            row = table.insertRow(i + 1);
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

        if (allReady === true) {
            clearInterval(infoTimer);
            enterGame(jsonData);
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

infoTimer = setInterval(getInfo, 3000);
const readyBtn = document.getElementById("readyBtn");
readyBtn.addEventListener("click", setReady, false);