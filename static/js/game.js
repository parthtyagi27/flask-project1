var updateTimer = null;
var cards = [];
var currentCard = {};
var turn = "";
var name = sessionStorage.getItem("session_name");
var colorOptions = document.getElementById("colorOptionsDiv");
colorOptions.style.display = "none";
var colorButton = null;
let playingCard = {}

console.log("Session name = " + name);

async function getInfo() {
    let infoString = "";
    infoString += "cards,";
    infoString += "turn,";
    infoString += "currentCard,";
    infoString += "winner";

    console.log("info query = " + infoString);
    if (infoString === "")
        return null;
    console.log("Sending request");
    fetch("/updateGame?info=" + infoString, { method: 'GET',}).then(function(response) {
        return response.json();
    }).then(function(json) {
        if (updateUI(json) == true)
            setTimeout(getInfo, 250); 
    });
}

function updateUI(data) {

    if (data[3].winner !== "none") {
        alert(data[3].winner + " has won!");
        return false;
    }

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

    if (cardsUpdated === true || currentCardUpdated === true || turnUpdated === true) {    

        const cardTable = document.getElementById("cards_table");
        cardTable.innerHTML = "";

        for (let i = 0; i < cards.length; i++) {
            let card = cards[i];
            let row = cardTable.insertRow(i);
            let colorCell = row.insertCell(0);
            let valueCell = row.insertCell(1);
            colorCell.innerHTML = card.color;
            valueCell.innerHTML = card.value;
            
            if (name === turn) {
                let buttonCell = row.insertCell(2);
                if (card.color === currentCard.color || card.value === currentCard.value || card.color === "wild") {
                    let playButton = document.createElement("button");
                    playButton.id = "useButton";
                    playButton.textContent = "Use";
                    playButton.addEventListener("click", function click() {
                       console.log("Playing " + JSON.stringify(card));
                       if (card.value === "color" || card.value === "+4") {
                            playingCard = card;
                            colorOptions.style.display = "inline";                    
                        } else {
                            playCard(card); 
                        }
                    });
                    buttonCell.appendChild(playButton);
                }
            }
        }
    }

    if (turn === name) {
        document.getElementById("pickupButton").style.display = "block";
    } else {
        document.getElementById("pickupButton").style.display = "none";
    }

    return true;
}

window.onload = function() {
    
};

document.getElementById("redBtn").addEventListener("click", function click() {
    if (JSON.stringify(playCard) === "")
        return;

    colorButton = "red";
    playSpecialCard(playingCard, colorButton);
    playingCard = {};
    colorOptions.style.display = "none"
});

document.getElementById("greenBtn").addEventListener("click", function click() {
    if (JSON.stringify(playCard) === "")
        return;

    colorButton = "green";
    playSpecialCard(playingCard, colorButton);
    playingCard = {};
    colorOptions.style.display = "none"
});

document.getElementById("blueBtn").addEventListener("click", function click() {
    if (JSON.stringify(playCard) === "")
        return;

    colorButton = "blue";
    playSpecialCard(playingCard, colorButton);
    playingCard = {};
    colorOptions.style.display = "none"
});

document.getElementById("yellowBtn").addEventListener("click", function click() {
    if (JSON.stringify(playCard) === "")
        return;

    colorButton = "yellow";
    playSpecialCard(playingCard, colorButton);
    playingCard = {};
    colorOptions.style.display = "none"
});

function playSpecialCard(card_to_play, color) {
    let data = {
        "action": "playCard",
        "card": card_to_play,
        "color": color
    }

    // Send current card to the server
    console.log('Data = ' + JSON.stringify(data));

    fetch('/updateGame', {
        // Specify the method
        method: 'POST',
        // A JSON payload
        // redirect: 'follow',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(data)
        })
    .then(function (response) { 
         // At this point, Flask has printed our JSON
        return response.text();
    }).then(function (text) {
        // Should be 'OK' if everything was successful
        console.log(text);
        });
    colorOptions.style.display = "none";
}

function playCard(card_to_play) {
    let data = {
        "action": "playCard",
        "card": card_to_play
    }

    // Send current card to the server
    console.log('Data = ' + JSON.stringify(data));

    fetch('/updateGame', {
        // Specify the method
        method: 'POST',
        // A JSON payload
        // redirect: 'follow',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(data)
        })
    .then(function (response) { 
         // At this point, Flask has printed our JSON
        return response.text();
    }).then(function (text) {
        // Should be 'OK' if everything was successful
        console.log(text);
        });
}

document.getElementById("pickupButton").addEventListener("click", function click() {
    let data = {
        "action": "pickCard"
    }

    let dataString = JSON.stringify(data);

    console.log('Data = ' + dataString);

    fetch('/updateGame', {
        // Specify the method
        method: 'POST',
        // A JSON payload
        // redirect: 'follow',
        headers: {'Content-Type': 'application/json'},
        body: dataString
        })
    .then(function (response) { 
         // At this point, Flask has printed our JSON
        return response.text();
    }).then(function (text) {
        // Should be 'OK' if everything was successful
        console.log(text);
        });
});

getInfo();
