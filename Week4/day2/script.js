// Exercise 1 : Keyless Car
// Ask the user for his age, and save the value into a variable
// Create a function called checkDriverAge() that will alert the user if he can drive depending on his age.
// if he is too young, alert “Sorry, you are too young to drive this car. Powering off”
// if he is old enough, alert “You are old enough to drive, Powering On. Enjoy the ride!”
// if he just turned 18, alert “Congratulations on your first year of driving. Enjoy the ride!”
// Instead of using prompt to ask the user for his age, make the checkDriverAge() function accept an argument age, 
// so that if you enter: checkDriverAge(92); it alerts “You are old enough to drive, Powering On. Enjoy the ride!”


// let age = prompt("What is your age?");
// // console.log(age);

// function checkDriverAge(age) {

//     if (age < 18) {
//         alert("Sorry, you are too young to drive this car, Power Off.");
//     }
//     else if (age > 18) {
//         alert("You are old enough to drive, Powering On. Enjoy the ride!");
//     }
//     else (age = 18) 
//         alert("Congratulations on your first year of driving. Enjoy the ride!")
// }
// checkDriverAge(age);



// Exercise 2 : What’s In My Wallet ?
// Given a total due and an array representing the amount of change in your pocket, determine whether or not you are able to pay for the item.
// Change will always be represented in the following order: quarters, dimes, nickels, pennies.
// Quarters  = 0.25
// Dimes = 0.10
// Nickels = 0.05
// Pennies = 0.01
// To illustrate:
// changeEnough([25, 20, 5, 0], 4.25) should return true, since having 25 quarters, 20 dimes, 5 nickels 
// and 0 pennies gives you 6.25 + 2 + .25 + 0 = 8.50 which is bigger than 4.25 (the total amount due)

// Examples

// changeEnough([2, 100, 0, 0], 14.11) ➞ false
// changeEnough([0, 0, 20, 5], 0.75) ➞ true


// Exercise 3: Find The Multiples Of 23
// Write a js function that console.log the multiples of 23 less than 500 and at the end return the sum of all of them.

// Elements : 0 23 46 69 92 115 138 161 184 207 230 253 276 299 322 345 368
// 391 414 437 460 483
// Sum : 5313

// let numbers = [0, 23, 46, 69, 92, 115, 138, 161, 184, 207, 230, 253, 276, 299, 322, 345, 368, 391, 414, 437, 460, 483];

// Multiples function

// var numbers = [500, 75, 0, 23, 46, 69, 92, 115, 138, 161, 184, 207, 230, 253, 276, 299, 322, 345, 368, 391, 414, 437, 460, 483];

// const sumMultiples = (numbers) => {
//     let multiplesOf23 = numbers.filter(element => element%23===0 && element<500);
//     return multiplesOf23.reduce((x,y)=>x+y);
// }

// console.log(sumMultiples(numbers));


// Note to Chaim - It'd be great if you could send me some sources to practise, because I still don't understand a 100%, thanks


// Exercise 4 : Amazon Shopping


// Create a function called checkBasket().
// It should:
// ask the user for the item he wants
// and let him know if it’s in the basket or not
// Hint: Use the in keyword inside the conditional


// let item = prompt("What is in the basket?");

// let amazonBasket = {
//     glasses: 1,
//     books: 2,
//     floss: 100
// }

// function checkBasket(amazonBasket) {
//     if (item in amazonBasket = 0) {
//         return "It is";
//     }
//     else {
//         return "It is not";
//     }

// }

// checkBasket(amazonBasket);



// function checkBasket() {
//     let amazonBasket = {
//         glasses: 1,
//         books: 2,
//         floss: 100
//     }


//     let item = prompt("Is it in the basket");

//     if (item in amazonBasket) {
//         alert("The item is in the basket");
//     } else {
//         alert("item is not in the basket");
//     }
//     return;
// }


// checkBasket();