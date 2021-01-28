let calcDisplay = document.getElementById('display') 

// calcDisplay.html is my div
console.log(calcDisplay)
let calstr = ""

// instert numbers and symbols

function my_f(button) {
    calstr = calstr + button
    calcDisplay.innerHTML = calstr
    console.log(calstr);
}

function result(button) {
    let calcResult = eval(calstr);
    calcDisplay.innerHTML = calcResult;
    calstr = calcResult;
    console.log(calcResult);

}

function clear1() {
    calstr = "";
    calcDisplay.innerHTML = 0;
    
}

function back() {
    if (calcDisplay.innerHTML.length > 1) {
        calcstr = calstr.slice(0, -1);
        console.log(calstr);
calcDisplay.innerHTML = calcDisplay.innerHTML.slice(0, -1)
    }

    else {
        calcDisplay.innerHTML = 0;
       }
}