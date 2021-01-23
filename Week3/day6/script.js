// Excercise1

// Create an array to hold your top colors.
// For each choice, console.log a string like: “My #1 choice is blue”, “My #2 choice is red” ect…
// Bonus: Change it to console.log “My 1st choice”, “My 2nd choice”, “My 3rd choice”, picking the right suffix for the number.
// Hint : create an array of suffix to do the Bonus


// let colors = ["blue", "red", "yellow"];

// for (let i in colors) {

//     if (i == 0) {
//         console.log("My favorite color is blue")
//     }
//     if (i == 1) {
//         console.log("My favorite color is red")
//     }

//     if (i == 2) {
//         console.log("My favorite color is yellow")
//     }
// }


// Exercise 2 : List Of People

// let people = ["Greg", "Mary", "Devon", "James"]
// 1. Write the command to remove “Greg” from the array.
// 2. Write the command to replace “James” by “Jason” in the array.
// 3. Write the command to add your name to the end of the array.
// 4. Using a loop, iterate through this array and console.log all of the people.
// 5. Using a loop, iterate through this array and after console.log-ing “Jason”, exit from the loop.
// 6.  the command to make a copy of the array using slice. The copy should NOT include “Mary” or your name.
// 7. Write the command that gives the indexOf where “Mary” is located. Look on google what indexOf is
// 8. Write the command that gives the indexOf where “Foo” is located (this should return -1). Why does it return -1
// 9. Write a variable called last which value is the last element of the array.
// Hint: What is the relationship between the index of the last element in the array and the length of the array?


// let people = ["Greg", "Mary", "Devon", "James"]

//1. remove Greg

// people.shift();

// console.log(people);


//2. Replace James by Jason

// let replacedItems = people.splice(people.indexOf("James"), 1, "Jason")

// console.log(people)

// 3. Write the command to add your name to the end of the array.

// people.push("Anna");
// console.log(people);

// 4.

// let people = ["Greg", "Mary", "Devon", "James", "Anna"]

// let arrayLength = people.length;

// for (let i = 0; i < arrayLength; i++) {
//     console.log(people[i]);
// }

// 6.

// let people = ["Greg", "Mary", "Devon", "Jason", "Anna"]

// let arrayLength = people.length;

// for (let i = 0; i < arrayLength; i++) {

//     if (i === 4) {
//         break;
//     }
//     console.log(people[i]);
// }

// 7.

// let people = ["Greg", "Mary", "Devon", "Jason", "Anna"]

// console.log(people.indexOf("Mary"));

// 8.

// let people = ["Greg", "Mary", "Devon", "Jason", "Anna"]

// console.log(people.indexOf("Foo"));

// It came back as -1 because it doesn't exist.

// // 9. Write a variable called last which value is the last element of the array.



// Exercise 3 : Repeat The Question
// Ask a number to the user, while the number is smaller than 10, ask him for a new number.
// Tip : Which while loop is more relevant for this situation?


// prompt("Give me a number");

// let i = 0;

// do {
//     alert("Give me an other number")
//     i++;
// }

// while (i < 10);


// for (let i = 0; i < 10; i++) {

// alert("Give me an other number") 

//     if (i > 10) {
//         break;
//     }
//     alert("Too big")
// }
