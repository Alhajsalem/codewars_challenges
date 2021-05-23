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