// https://www.codewars.com/kata/54edbc7200b811e956000556/train/javascript

// FUNDAMENTALS ARRAYS
var assert = require('assert');
const { start } = require('repl');

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

// https://www.codewars.com/kata/54da539698b8a2ad76000228/train/javascript

function isValidWalk(walk) {
  array_n = []
  array_s = []
  array_w = []
  array_e = []
  walk.forEach(function(item){
    if (item == 'n') array_n.push(item)
    if (item == 's') array_s.push(item)
    if (item == 'e') array_e.push(item)
    if (item == 'w') array_w.push(item)
  })
  return (array_n.length == array_s.length)  && (array_w.length == array_e.length) && ((array_n.length+array_s.length+array_w.length+array_e.length)==10) ? true : false
}

// better solution 
function isValidWalk(walk) {
  const north = walk.filter(item => { return item === "n" }).length;
  const south = walk.filter(item => { return item === "s" }).length;
  const east = walk.filter(item => { return item === "e" }).length;
  const west = walk.filter(item => { return item === "w" }).length;
  
  return walk.length === 10 && north === south && east === west;
}

function findMissingLetter(array){
  start_ = 'abcdefghijklmnopqrstuvwxyz'.indexOf(array[0].toLowerCase())
  end_ = 'abcdefghijklmnopqrstuvwxyz'.indexOf(array[array.length-1].toLowerCase())
  alphabet = 'abcdefghijklmnopqrstuvwxyz'.slice(start_,end_+1).split("")
  str = ""
  for(var i = 0; i<= array.length; i++){
    if(alphabet[i] !== array[i].toLowerCase()){
      str = alphabet[i]
      break
    }
  }
  if (array[0] == array[0] .toUpperCase()) return str.toUpperCase()
  if (array[0] == array[0] .toLowerCase()) return str.toLowerCase()

}

findMissingLetter(['O','Q','R','S'])//, 'e'

// https://www.codewars.com/kata/554ca54ffa7d91b236000023/train/javascript
function deleteNth(arr,n){
  var y = {}
  result = arr.filter(x =>{
    y[x] =  y[x] ? y[x] + 1 : 1;
    return y[x] <= n
  })
  console.log(result)
}

deleteNth([20,37,20,21],1)