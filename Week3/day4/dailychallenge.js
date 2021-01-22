// Instructions
// Create a variable called sentence. Assign to this variable, a string that has the word “not” and “bad” inside. For example, “The movie is not that bad really, I like it”
// Create a variable called wordNot that retrieves the first appearance of the substring “not” (from the sentence)
// Create a variable called wordBad that retrieves the first appearance of the substring “bad” (from the sentence)
// If the word “bad” follows the word “not”, you should replace the whole “not…bad” substring with “good”, then console.log the result.
// For example, the result here should be : “The movie is good really, I like it”
// If the words “not” and “bad” are not in the right sequence (or are not in the sentence), just console.log the original sentence.

//let str = "This dinner is not that bad!";
let str = "This dinner is not that bad ! You cook well!";
// //split into chars
let array = str.split("");
console.log(array);

// //find index where not starts

let wordNot = str.indexOf("not");
console.log(wordNot);

// //find index where bad starts
let wordBad = str.indexOf("bad");
console.log(wordBad);

let deleteCount = (wordBad - wordNot-2);
// //if not is before bad, and not and bad exist in the string (-1 is out of range)
if (wordNot < wordBad && wordNot != -1 && wordBad != -1) {

//take out not and bad, replace it with good
array.splice(wordNot, deleteCount, "good");
array.splice(wordNot, wordBad-wordNot-2, "good");

console.log(array)

// 	//join the chars back
str = array.join("");
}

console.log(str);