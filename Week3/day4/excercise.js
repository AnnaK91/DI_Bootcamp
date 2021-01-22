//1.Excercise


// Create 2 variables, x and y. Each of them has a different numeric value.
// Write an if/else statement that checks the biggest number.
// If x equals 5 and y equals 2, the program should display:

// x is the biggest number


// let x = 5 
// let y = 2 

// if ( x > y) {
//     alert("X is bigger")
// }

// Exercise 2: Chihuahua

// Create a variable newDog that is equal to the string “Chihuahua”.
// Check and display how many letters are in newDog.
// Display the newDog variable in uppercase and then in lowercase (no need to create new variables, just use 2 console.log).
// Check if the variable newDog equals to “Chihuahua”
// if it does, display ‘I love Chihuahua, it’s my favorite dog breed’
// else, console.log ‘I dont care, I prefer cats’

// a + b

//var newDog = "Chiahuahua"
// var newDog = newDog.length;
// console.log(newDog)

// c.
// var newDog = "Chiahuahua"
// newDog = newDog.toLowerCase();
// console.log(newDog)

// newDog = newDog.toUpperCase();
// console.log(newDog)

// d.
// var newDog = "Chiahuahua"
// if(typeof(newDog) === 'string') {
//     alert('I love Chihuahua, it’s my favorite dog breed')
//   } else if(typeof(newDog) === 'number') {
//     alert('I dont care, I prefer cats')
// }

// Exercise 3: Even Or Not Even




// Ask a number to the user, and save it to a variable.
// Check if the variable is an even number
// If it is, display: “x is an even number’. Where x is the actual number of the user.
// If it isn’t, display “x is not an even number’. Where x is the actual number of the user

// var number = prompt("Give me a number");
// console.log(number);

// var answer = prompt('Give me a number', 10);
// if(answer % 2 == 0) {
//     console.log("x is an even number");
// }

// // if the number is odd
// else {
//     console.log("The number is odd.");
// }


// Exercise 4: Group Chat
// let users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"]
// Using the array above, console.log the number of users in a group conversation based on the following rules:
// If there is no one, display “no one is online”.
// If there is 1 person, display “<name_user> is online”.
// If there are 2 people, display “<name_user1> and <name_user2> are online”.
// If there are n>2 people, display the first two names and add “and n-2 more are online”.
// For example, if there are 5 users, it should display:

// name_user1, name_user2 and 3 more are online


let users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"];

// console.log(users.length)

if (users.length == 0) {
    console.log("No one is online")
}

// if (users.length == -1) {
//     console.log("No one is online");
// }

//Note to Chaim - don't understand :( Please help!)