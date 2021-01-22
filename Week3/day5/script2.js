// class excercise 2


// let names= ["john", "sarah", 23, "Rudolf",34]


// 1. Write a JavaScript for loop that will go through the variable names.

// if the item is not a string, pass.
// if the item is a string, check if it's first letter is in uppercase. If not, change it to uppercase and then display the name.
// 2. Write a JavaScript for loop that will go through the variable names

// if the item is not a string, go out of the loop.
// if the item is a string, display it.

//Solution:
let names = ["john", "sarah", 23, "Rudolf", 34];

//Step 1:
for (i of names) {
    if (typeof (i) === 'string') {

        //console.log(i, 'is a string');

        if (i[0] == i[0].toUpperCase()) {

            console.log(i);

        } else {

            // concat first letter with the rest 
            console.log(i[0].toUpperCase() + i.slice(1, i[i.lenghth - 1]));
        }

    } else {
        continue;
    }
}
for (i of names) {

    if (typeof (i) === 'string') {

        console.log(i, "is a string");
    } else {
        break;
    }
}
