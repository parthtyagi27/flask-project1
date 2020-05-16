var updateTimer = null;
var cards = []
var turn = null

async function getInfo() {
    let infoString = "";
    if (cards.length === 0)
        infoString += "cards,";
    if (turn === null)
        infoString += "turn";

    console.log("info query = " + infoString);
    if (infoString === "")
        return null;
    console.log("Sending request");
    fetch("/updateGame?info=" + infoString, { method: 'GET',}).then(function(response) {
        return response.json();
    }).then(function(json) {
        updateUI(json);
        setTimeout(getInfo, 1500);
    });
}

function updateUI(data) {
    console.log(data);
    responseCards = data[0];
    responseTurn = data[1];
    if (cards != responseCards)
        cards = responseCards;
    console.log(cards);
    if (turn === null || turn != responseTurn)
        turn = responseTurn.turn;
    console.log(turn);
    document.getElementById("turnLabel").innerHTML = "It's " + turn + "'s turn";

    const cardTable = document.getElementById("cards_table");
    cards = cards.cards;
    for (let i = 0; i < cards.length; i++) {
        currentCard = cards[i];
        let row = cardTable.insertRow(i);
        let colorCell = row.insertCell(0);
        let valueCell = row.insertCell(1);
        colorCell.innerHTML = currentCard.color;
        valueCell.innerHTML = currentCard.value;
    }
}

window.onload = function() {

};

getInfo();

// async function getInfo(queryString) {
//     console.log("info query = " + queryString);
//     if (queryString === "")
//         return null;
//     const response = await fetch("/updateGame?info=" + queryString, { method: 'GET',});
//     const response_1 = response.json;
//     // console.log("Recieved response from getInfo...");
//     // console.log(response_1);
//     // responseObj = response;
//     // return response;
//     return response_1;
// }

// function updateGame() {
//     // let queries = [];
//     let infoQueries = [];
//     let updateQueries = [];

//     if (cards.length === 0)
//         infoQueries.push("cards");
//     if (turn == null)
//         infoQueries.push("turn");

//     // if (JSON.stringify(cards) === "{}") {
//     //     fetch('/updateGame?info=cards', {
//     //         method: 'GET',
//     //     }).then(function (response) {
//     //         return response.json();
//     //     }).then(function (response) {
//     //         cards = response;
//     //         console.log(cards);
//     //     });
//     // } else if (turn === null) {

//     // }
//     let infoString = "";
//     for (let i = 0; i < infoQueries.length; i++) {
//         infoString += infoQueries[i];
//         // console.log("Info Query[" + i + "] = " + infoQueries[i]);
//         if (i < infoQueries.length - 1)
//             infoString += ","
//     }
//     // console.log(infoString);
//     // if (infoString !== "") {
//     //     console.log(getInfo(infoString));
//     // }
//     let infoResponse = getInfo(infoString);
//     console.log(infoResponse);
//     if (infoResponse != null) {
//         if (cards.length === 0) {
//             // fetch cards from response object
//             // let cardResponse = JSON.parse(infoResponse);
//             // infoResponse = JSON.parse(infoResponse);
//             // console.log(infoResponse);
//             // console.log(infoResponse);
//         }
//     }
// }
// updateTimer = setInterval(updateGame, 1000)