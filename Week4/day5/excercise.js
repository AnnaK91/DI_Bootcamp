// Exercise 1 : Change The Navbar
//  <div id="navBar">
//     <ul>
//         <li><a href="#">Profile</a></li>
//         <li><a href="#">Home</a></li>
//         <li><a href="#">My Friends</a></li>
//         <li><a href="#">Messenger</a></li>
//         <li><a href="#">My Pics</a></li>
//     </ul>
// </div>`
// In the div above, change the value of the identity attribute (id) from navBar to socialNetworkNavigation, using the setAttribute method.
// We are going to add a new li to the ul.
// First, create a new li tag (use the createElement method)
// Then create a new text node with “Logout” as its specified text.
// Append the text node to the newly created list node (li).
// Finally, append this updated list node to the unordered list above, using the appendChild method.
// Bonus
// Use the firstElementChild and the lastElementChild properties to retrieve the first and last li elements under the parent ul node. Display the text of each link.(Hint: textContent property).


// 1. change the value of the identity attribute (id) from navBar to socialNetworkNavigation, using the setAttribute method.


// let newDiv = document.getElementById("navBar")

// newDiv.getAttribute("id");

// newDiv.setAttribute('id', "socialNetworkNavigation");


// 2. add a new li to the ul.

// var node = document.createElement("li");

// var textnode = document.createTextNode("Logout");

// node.appendChild(textnode);

// document.getElementById("myList").appendChild(node);
// node.innerHTML = '<a href="#"> Logout </a>';



// Exercise 2 : Users
// <html>
// <body>
//   <div id="container">Users:</div>
//   <ul class="list">
//     <li>John</li>
//     <li>Pete</li>
//   </ul>
//   <ul class="list">
//     <li>David</li>
//     <li>Sarah</li>
//     <li>Dan</li>
//   </ul>
// </body>
// </html>
// Change the name “Pete” to “Richard”
// Change each first name of the <ul> by your name
// Add at the end of each <ul>, a <li> that says “Hey students”
// Delete the <li> Sarah
// Bonus
// Add a class “student_list” to both of the <ul>
// Add the class “university” and “attendance” to the first <ul>


// var node = document.getElementsByTagName("ul")[1];
// node.getElementsByTagName("li")[1].innerHTML = "Richard";

