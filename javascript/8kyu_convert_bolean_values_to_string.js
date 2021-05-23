// https://www.codewars.com/kata/53369039d7ab3ac506000467/train/javascript

// FUNDAMENTALSvBOOLEANS BEST PRACTICES
var assert = require('assert');

function boolToWord( bool ){
    return bool ? "Yes" : "No";
  }

assert.equal(boolToWord(true),'Yes')

// https://www.codewars.com/kata/5966e33c4e686b508700002d/train/javascript
function sumStr(a,b) {
  if (a === "") {
    a = 0
  }
  if (b === ""){
    b = 0
  }
  return (parseInt(a)+parseInt(b)).toString() 
}

// better solution 
function sumStr_1(a,b) {
  const num1 = Number(a);
  const num2 = Number(b);
  return String(num1 + num2)
}

sumStr_1("","5")

// https://www.codewars.com/kata/58f8a3a27a5c28d92e000144/train/javascript

function firstNonConsecutive (arr) {
  var min = Math.min(...arr)
  var max = Math.max(...arr)
  arr_n = []
  for (var i = min; i <= max; i ++){
    arr_n.push(i)
  }
  for (var i = 0; i <= arr_n.length; i ++){
    if (arr_n[i] != arr[i]) return (arr[i])
  }
    return null
}

console.log(firstNonConsecutive([ 1, 2, 3, 4 ]))

// better solution 
function firstNonConsecutive(arr) {
  for (let i = 0; i < arr.length - 1; ++i) {
    if (arr[i] + 1 !== arr[i + 1]) {
      return arr[i + 1]
    }
  }
  return null
}