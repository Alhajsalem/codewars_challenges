// https://www.codewars.com/kata/55c45be3b2079eccff00010f/train/javascript
// FUNDAMENTALS STRINGS
var assert = require('assert');

function order(words){
    if (words === ""){return ""}
    const words_arr = words.split(" ")
    var re = new RegExp("[0-90]");
    var arr = []
    words_arr.forEach(element => {
        var myArray = element.match(re);
        arr[myArray[0]] = element
    });
    return ((arr.filter(Boolean)).join(" "))
  }

assert(order("is2 Thi1s T4est 3a") === "Thi1s is2 3a T4est");

// better solution 
function order(words){
  
    return words.split(' ').sort(function(a, b){
        return a.match(/\d/) - b.match(/\d/);
     }).join(' ');
  }    


  var items = [
    { name: 'Edward', value: 21 },
    { name: 'Sharpe', value: 37 },
    { name: 'And', value: 45 },
    { name: 'The', value: -12 },
    { name: 'Magnetic', value: 13 },
    { name: 'Zeros', value: 37 }
  ];
  

  items.sort(function (a, b) {
    return a.value - b.value;
  });

  console.log(items)