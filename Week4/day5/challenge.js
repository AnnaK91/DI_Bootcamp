
// update

// var planetNode = document.createElement('div');
// var textNode = document.createTextNode("Test");
// planetNode.appendChild(textNode);
// document.getElementsByTagName('body')[0].appendChild(planetNode);
// planetNode.classList.add("planets");

let Planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"];
planetLength = Planets.length;
let newDiv;
for (i = 0; i < planetLength; i++) {
        newDiv = document.createElement('div');
        newDiv.className = "planets";
        newDiv.innerHTML = Planets[i];
        document.getElementsByTagName('body')[0].appendChild(newDiv);
    }