function insert_Row() {
  var table = document.getElementById("sampleTable");
  var newRow = document.createElement('tr');
  newRow.innerHTML = "<td>Row</td><td>Row</td>"
  table.appendChild(newRow);
}