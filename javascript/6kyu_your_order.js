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


String.prototype.camelCase=function(){
    x =  this.split(" ")
    arr = []
    for (var i = 0; i < x.length; i++) {
      arr.push(x[i].charAt(0).toUpperCase() + x[i].slice(1));
    }
    return(arr.join(""))
  }

console.log("test case".camelCase())

// better solution 
String.prototype.camelCase=function(){
  return this.split(' ').map(function(word){
   return word.charAt(0).toUpperCase() + word.slice(1);
 }).join('');
}

multiplicationTable = function(size) {
  arr = []
  for (var i = 1; i< size+1; i++){
    x = []
    for (var j= 1; j < size +1; j++){
        x.push(j*i)
    }
    arr.push(x)
  }
  return arr
}
console.log(multiplicationTable(3))
  


function playPass(s, n) {
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  console.log(alphabet)
}

playPass("I LOVE YOU!!!", 1)


function generateColor() {
  return `#${(0 | Math.random() * 0xEEEEEE + 0x111111).toString(16)}`
}

console.log(generateColor())