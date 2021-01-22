
//FOR LOOPS

//Syntax

/* for(variable start; length or condition; increment){

	Code we want to repeat

 }
 */
 

// for (isaac = 1; isaac <= 5; isaac++) {

//       console.log("The number is " + isaac);
//   }

//Increment by 2
// for (isaac = 0; isaac < 10; isaac = isaac + 2) {

// 	console.log("The number is " + isaac);
// }


// for(var i = 1; i <= 101; i++){

//  	console.log(i);

//  }


// var week = ['Sunday','Monday','Tuesday','Wednesday','Thursday', 'Friday', 'Saturday']

//  for(var i = 0; i < week.length; i++){

//  	console.log(week[i]);

//  }







// Exercise 1
// Create a stuctured html file linked to a JS file

// 1. Write a JavaScript for loop that will iterate from 0 to 15. For each iteration, it will check if the current number is odd or even, and display a message to the screen.

// Sample Output: //"0 is even" //"1 is odd" //"2 is even"

//Solution:
// for(i = 0; i <= 15; i++){

// 	//console.log(i);

// 	if (i % 2 == 0) {

// 		console.log(i + " is even");

// 	  } else {

// 		console.log(i + " is odd");
// 	  }
// }






//FOR IN

//(its more for objects)

// var person = {
//                fname: "John", 
//                lname: "Doe", 
//                age: 25
//              };

// for (x in person) {

//   console.log(person[x]) // John Doe 25

// }


// var week = ['Sunday','Monday','Tuesday','Wednesday','Thursday', 'Friday', 'Saturday'];

//  for(yitzjak in week){

//  	console.log(week[yitzjak]);
//  }



//FOR OF 

// (its more for arrays than objects)

// var colors = ["blue", "yellow", "red"];

// for ( i in colors) {
//    console.log(i); // logs "0", "1", "2",
// }



// var colors = ["blue", "yellow", "red"];

// for (i of colors) {

//    console.log(i); // logs blue, yellow, red
// }




//WHILE LOOPS


// SYNTAX

// while(condition){
//
// }

// var n = 0;

// while (n < 3) {

//  console.log(n)

//   n++;

// }



// var i = 1;

// while(i < 11){

//   document.write(i + '<br>');

// 	i++;

// }



//DO WHILE

// let i = 1;

// do {
//   console.log(i);

//   i++;
// }

// while (i <= 10);



//Do while loop - Run the code at least 1 time

// var i = 12;

// do{

//   document.write(i + '<br>');

//   i++;

// }while(i < 11);




//Break Statement


// for (i = 0; i < 10; i++) {

//   if (i === 3) { 

//       break;

//     }

//   console.log(i); // 0 1 2
// }


// BREAK - Allows you to stop the cycle

// var week = ['Sunday','Monday','Tuesday','Wednesday','Thursday', 'Friday', 'Saturday'];



// for(var i = 0; i < week.length; i++){


//   //console.log(i);

// 	console.log(week[i]);

// 	if (week[i] == 'Wednesday') {

// 		break;
// 	}

// }




//OTHER WAY OF EXECUTION

// var week = ['Sunday','Monday','Tuesday','Wednesday','Thursday', 'Friday', 'Saturday'];


// for(var i = 0; i < week.length; i++){


// 	if (week[i] == 'Wednesday') {

// 		break;
//   }


//   console.log(week[i]);


// }





//CONTINUE

// for (i = 0; i < 10; i++) {

//   if (i === 3) { 

//     continue;   //skip it , we are skipping number 3

//   }

//   console.log(i); // 0 1 2 4 5 6 7 8 9 
// }



// CONTINUE - Lets you jump to the next execution of the cycle

// var week = ['Sunday','Monday','Tuesday','Wednesday','Thursday', 'Friday', 'Saturday'];

// for(var i = 0; i < week.length; i++){

// 	if (week[i] == 'Tuesday') {

// 		continue;
// 	}

// 	console.log(week[i]);

// }



//INFINTE LOOP (DANGER)


// for (var i = 0; i < Infinity; i++) {

//     //console.log(i);
// }


// for (var i = 1; i > 0 ; i++) {

//     //console.log(i);
// }



// while(true){

//   console.log('VIRUS');

// }




// Exercise 2
// let names= ["john", "sarah", 23, "Rudolf",34]

// 1. Write a JavaScript for loop that will go through the variable names.
// if the item is not a string, pass.
// if the item is a string, check if it's first letter is in uppercase. If not, change it to uppercase and then display the name.

// 2. Write a JavaScript for loop that will go through the variable names
// if the item is not a string, go out of the loop.
// if the item is a string, display it.


//Solution:
let names= ["john", "sarah", 23, "Rudolf",34];

//Step 1:
// for (i of names){
// 	if(typeof(i) === 'string'){

// 		//console.log(i, 'is a string');

// 		if(i[0] == i[0].toUpperCase() ){

// 			console.log(i);

// 		} else {

// 			// concat first letter with the rest 
// 			console.log(i[0].toUpperCase() + i.slice(1, i[i.lenghth -1]));
// 		}

// 	} else {
// 		continue;
// 	}
// }



//Step 2:
// for (i of names){

// 	if(typeof(i) === 'string'){

// 		console.log(i, 'is a string');

// 	} else {

// 		break;

// 	}

// }







// //Example of use:
// // Looping Object With Condition
// function signin() {

// 	let username = document.getElementById('user').value;
// 	let password = document.getElementById('pass').value;
	
// 	//Boolean variable to check if we got a correct user
// 	correct = false;

// 	//console.log(username);
// 	//console.log(password);

// 	for(x of users){

// 		// console.log(x.username);
// 		// console.log(x.password);

// 		if(username == x.username && password == x.password){

// 			alert('correct');
// 			correct = true;
// 			break;

// 		} else if(username !== x.username && password !== x.password){

// 			continue;

// 		}
		
// 	}

// 	if(correct == false){
// 		alert('Please sign up');
// 	}


// }

// let submit = document.querySelector('button');
// //console.log(submit);

// submit.addEventListener('click', signin)


// //Database
// let users = [

// 	{
// 		username: 'johnny5',
// 		password: '12345'
// 	},

// 	{
// 		username: 'jamesB',
// 		password: '007'
// 	}
// ]




//Variable Keywords:

// Local scope
// function sayHello(){
//     var name = "Sarah"
// }
// console.log(name) // undefined


//Global scope
// function sayHello(){
//     var name = "Sarah"
// }
// console.log(name) // undefined


//The Problem Of The Keyword Var
// var age = 20

// if (age > 18) {
//     var canDrive = true 
//     console.log(canDrive); // true
// } 
// console.log(canDrive);  // true


//Redeclaration
// var name = "Sarah"
// var name = "Dan"
// console.log(name);  // "Dan"  



// The Solution With Of The Keyword Let
// Support Block Scope
// let age = 20

// if (age > 18) {
//     console.log(age) // 20
//     let canDrive = true 
//     console.log(canDrive); // true
// } 
// console.log(canDrive); //ReferenceError: canDrive is not defined


//Doesn’t Allow Redeclaration But The Variable Can Be Changed
// let name = "Sarah"
// let name = "Dan" // SyntaxError: Identifier 'name' has already been declared

// name = "David"
// console.log(name)


// The Solution With Of The Keyword Const
// Support Block Scope
// let age = 20

// if (age > 18) {
//     const canDrive = true 
//     console.log(canDrive); // true
// } 
// console.log(canDrive);  // ReferenceError: canDrive is not defined


//Doesn’t Allow Redeclaration And The Variable Can’t Be Changed
// const name = "Sarah"
// name = "David" // TypeError: Assignment to constant variable.


//Play
//What's the Difference Between var, let and const in JavaScript?
//https://alligator.io/js/var-let-const/




//String And Variable Concatenation (Template Strings):

//1st Way
// let name = "Lea"
// let greetings = "Hello "+ name
// console.log(greetings)

//2nd Way
// let name = "Lea"
// let greetings = `Hello ${name}`;
// console.log(greetings)