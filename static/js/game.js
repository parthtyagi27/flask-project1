var updateTimer = null;
var cards = {}
var turn = null

window.onload = function() {

};

async function getInfo(queryString) {
    console.log("info query = " + queryString);
    const response = await fetch("/updateGame?info=" + queryString, { method: 'GET', });
    const response_1 = await response.json();
    console.log("Recieved response from getInfo...");
    console.log(response_1);
    // responseObj = response;
    return response_1;
    // return responseObj
}

function updateGame() {
    // let queries = [];
    let infoQueries = [];
    let updateQueries = [];

    if (JSON.stringify(cards) === "{}")
        infoQueries.push("cards");
    if (turn == null)
        infoQueries.push("turn");

    // if (JSON.stringify(cards) === "{}") {
    //     fetch('/updateGame?info=cards', {
    //         method: 'GET',
    //     }).then(function (response) {
    //         return response.json();
    //     }).then(function (response) {
    //         cards = response;
    //         console.log(cards);
    //     });
    // } else if (turn === null) {

    // }
    let infoString = "";
    for (let i = 0; i < infoQueries.length; i++) {
        infoString += infoQueries[i];
        // console.log("Info Query[" + i + "] = " + infoQueries[i]);
        if (i < infoQueries.length - 1)
            infoString += ","
    }
    console.log(infoString);
    if (infoString !== "") {
        console.log(getInfo(infoString));
    }
    
}

updateTimer = setInterval(updateGame, 1000);