// 1. Give to all paragraphs inside the <article> tag the class of para_article.
// 2. Remove the last paragraph in the article.
// 3. Add an event listener so that when you click on the h2, it is removed from the DOM.
// 4. Set the font size of the h1 to be a random pixel size from 0 to 100.
// 5. Hide the 1st paragraph, when it’s clicked. (use the display property )
// 6. Get the values from the inputs and append them to the end of the html, inside a table.
// Bonus: Fade out the 2nd paragraph over 2000 milliseconds, when it’s clicked.


// 1.
let paragraphs = document.querySelectorAll('p');

console.log(paragraphs);

// loop through the array to get a class to all the paragraphs

for (p of paragraphs) {
    console.log(p);
    p.classList.add('para_article');
}

// 2. remove the last paragraph

let paratwo = document.getElementsByTagName('p')[3];

paratwo.remove();


// paragraphs.classList.add('para_article');




// 3.

// add event listener


function removeItem() {

    let h2 = document.getElementsByTagName('h2')[0];
    h2.remove();


}


// 5. 

function hideItem() {

    let h1 = document.getElementsByTagName('h1')[0];
    h1.style.display = "none";

} 
