var updateTimer = null;
var cards = [];
var currentCard = {};
var turn = "";

async function getInfo() {
    let infoString = "";
    infoString += "cards,";
    infoString += "turn,";
    infoString += "currentCard"

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
    let cardsUpdated = false;
    let turnUpdated = false;
    let currentCardUpdated = false;

    let responseCards = data[0].cards;
    let responseTurn = data[1].turn;
    let responseCurrentCard = data[2].currentCard;

    let responseCardsString = JSON.stringify(responseCards);
    let responseCurrentCardString = JSON.stringify(responseCurrentCard);
    let currentCardString = JSON.stringify(currentCard);
    let cardsString = JSON.stringify(cards);
    
    if (cardsString !== responseCardsString) {
        console.log("Cards update!");
        cardsUpdated = true;
        console.log(cardsString + " -> " + responseCardsString);
        cards = responseCards;
    }

    if (turn !== responseTurn) {
        console.log("Turn update!");
        turnUpdated = true;
        console.log(turn + " -> " + responseTurn);
        turn = responseTurn;
    }

    if (currentCardString !== responseCurrentCardString) {
        console.log("Current card update!");
        currentCardUpdated = true;
        console.log(currentCardString + " -> " + responseCurrentCardString);
        currentCard = responseCurrentCard;
    }

    if (turnUpdated === true)
        document.getElementById("turnLabel").innerHTML = "It's " + turn + "'s turn";

    if (currentCardUpdated)
        document.getElementById("currentCardLabel").innerHTML = "Current Card: " + currentCard.value + " " + currentCard.color;

    if (cardsUpdated === true) {    
        const cardTable = document.getElementById("cards_table");
        for (let i = 0; i < cards.length; i++) {
            currentCard = cards[i];
            let row = cardTable.insertRow(i);
            let colorCell = row.insertCell(0);
            let valueCell = row.insertCell(1);
            colorCell.innerHTML = currentCard.color;
            valueCell.innerHTML = currentCard.value;
        }
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