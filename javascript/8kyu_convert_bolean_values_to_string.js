// https://www.codewars.com/kata/53369039d7ab3ac506000467/train/javascript

// FUNDAMENTALSvBOOLEANS BEST PRACTICES
var assert = require('assert');

function boolToWord( bool ){
    return bool ? "Yes" : "No";
  }

assert.equal(boolToWord(true),'Yes')