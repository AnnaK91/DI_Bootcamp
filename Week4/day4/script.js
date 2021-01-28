// Instructions
// You know the infamous song “99 Bottles of Beer?”

// You need to generate in JavaScript the lyrics to the song 99 Bottles of Beer as an output.

// Ask the user to input a starting number of bottles of beer, and start the bottles falling.
// But instead of 1 falling each time, the number falling goes up by one each time.

// ==============================

// 99 bottles of beer on the wall
// 99 bottles of beer
// Take 1 down, pass it around
// 98 bottles of beer on the wall
// 98 bottles of beer on the wall
// 98 bottles of beer
// Take 2 down, pass them around
// 96 bottles of beer on the wall
// 96 bottles of beer on the wall
// 96 bottles of beer
// Take 3 down, pass them around
// 93 bottles of beer on the wall

// ==============================

// How will you choose to make the song end?
// Make sure you get the grammer right…
// For 1 bottle, you pass “it” around.
// For more than one bottle, you pass “them” around
var number = prompt("Give me a number")
var word = "bottles";
// console.log(number);
var count = number;
while (count > 0) {
        var bottle = count == 1 ? "bottle" : "bottles";
console.log(count + " " + word + " of beer on the wall");
console.log(count + " " + word + " of beer on the wall");
console.log(count + " " + word + " of beer,");
console.log("Take one down, pass it around,");
--count;
}

// // Note to Chaim - I understand that I need to make a general variable that I can increment. But I don't know how :( This is as far as I could go.
