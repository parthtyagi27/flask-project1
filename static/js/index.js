const textBox = document.getElementById("nameInput");
function click() {
    let name = textBox.value;
    fetch('/login', {
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
        console.log(text);
        sessionStorage.setItem("session_name", name);
        window.location = "/lobby";
        });
}
const button2 = document.getElementById("enterBtn");
button2.addEventListener("click", click, false);
