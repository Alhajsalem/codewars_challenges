// https://www.codewars.com/kata/54edbc7200b811e956000556/train/javascript

// FUNDAMENTALS ARRAYS
var assert = require('assert');

function countSheeps(arrayOfSheep) {
    count = 0
    arrayOfSheep.forEach(element => {
        if (element) {count += 1}
    });
    return count
  }

  var array1 = [true,  true,  true,  false,
    true,  true,  true,  true ,
    true,  false, true,  false,
    true,  false, false, true ,
    true,  true,  true,  true ,
    false, false, true,  true ];
    
assert.equal(countSheeps(array1),17)