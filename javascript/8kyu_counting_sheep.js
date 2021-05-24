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

// better solution 

function countSheeps(arrayOfSheeps) {
    return arrayOfSheeps.filter(Boolean).length;
  }

function find_average(array) {
  var sum = array.reduce(function(total, item){
  return total +item
  },0)
  return array.length > 0 ? sum/array.length : 0
}

// better solution 
function find_average(array) {
  var sum = array.reduce((a, b) => a + b, 0);
  return sum/array.length;
}