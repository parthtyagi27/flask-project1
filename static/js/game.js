var updateTimer = null;
var cards = {}
var turn = null

window.onload = function() {

};

function updateGame() {
    if (JSON.stringify(cards) === "{}") {
        fetch('/updateGame?info=cards', {
            method: 'GET',
        }).then(function (response) {
            return response.json();
        }).then(function (response) {
            cards = response;
            console.log(cards);
        });
    } else if (turn === null) {

    }
}

updateTimer = setInterval(updateGame, 1000);