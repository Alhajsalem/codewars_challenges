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

// https://www.codewars.com/kata/5526fc09a1bbd946250002dc/train/javascript
function findOutlier(integers){
  odd_array = []
  even_array = []
  integers.forEach(function(item){
    if (item % 2 == 0){
      even_array.push(item)
    }
    else if (item % 2 != 0){
      odd_array.push(item)
    }
  })
  return odd_array.length == 1 ? odd_array[0] : even_array[0]
}

// better solution
function findOutlier(int){
  var even = int.filter(a=>a%2==0);
  var odd = int.filter(a=>a%2!==0);
  return even.length==1? even[0] : odd[0];
}