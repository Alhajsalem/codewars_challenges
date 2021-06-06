// https://www.codewars.com/kata/54edbc7200b811e956000556/train/javascript

// FUNDAMENTALS ARRAYS
var assert = require('assert');
const { start } = require('repl');
const { get } = require('https');

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
  return result
}

deleteNth([20,37,20,21],1)

// https://www.codewars.com/kata/585d7d5adb20cf33cb000235/train/javascript

function findUniq(arr) {
  uniqueArray = arr.filter(function(item, pos, self) {
    return self.indexOf(item) == pos;
  })
  var count = 0;
  for(var i = 0; i < arr.length; ++i){
    if(arr[i] == uniqueArray[0])
        count++;
}
 return count == 1 ? uniqueArray[0]: uniqueArray[1]
}

console.log(findUniq([ 0, 1, 1, 1, 1, 1, 1, 1 ]))

function findUniq(arr) {
  arr.sort((a,b)=>a-b);
  return arr[0]==arr[1]?arr.pop():arr[0]
}

function noSpace(x){
  return(x.replace(/ /g,""))
}

noSpace('8 j 8   mBliB8g  imjB8B8  jl  B')


var number=function(array){
  result =[]
  array.forEach((x,y)=>{
    result.push(`${y+1}: ${x}`)
  })
  return(result)
}

number(["a", "b", "c"])//, ["1: a", "2: b", "3: c"]

// Factory function 
function Router(){
  return {
    "FirstName":"Yousef",
    "LastName": "Alhajsalem", 
    "MyLastCent" : function(){
      console.log(`${this.FirstName}: ${this.LastName}`)
      return ""

    }
  }
}

var x = new Router()
console.log(x.MyLastCent())
// Constuctor function
function CirucleCalulation(radius){
  this.radius = radius
  this.draw = function(){
    console.log(this.radius)
  }

}

function SubstitutionCipher(abc1, abc2) {
  this.abc1 = abc1
  this.abc2 = abc2
  
  this.encode = function (str) {
    result = []
    for (var i = 0; i < str.length; i++) {
      if (this.abc1.indexOf(str[i]) != -1) result.push(this.abc2[this.abc1.indexOf(str[i])])
      else result.push(str[i]) 
    }
    return result.join("")
  }
  this.decode = function (str) {
    result = []
    for (var i = 0; i < str.length; i++) {
      if (this.abc1.indexOf(str[i]) != -1) result.push(this.abc1[this.abc2.indexOf(str[i])])
      else result.push(str[i]) 
    }
    return result.join("")  
  }
}

var abc1 = "abcdefghijklmnopqrstuvwxyz";
var abc2 = "etaoinshrdlucmfwypvbgkjqxz";
   
var sub = new SubstitutionCipher(abc1, abc2);
sub.encode("a_bc&*83") // => "eta"



function reverse(array) {
  var left = null;
  var right = null;
  var length = array.length;
  for (left = 0, right = length - 1; left < right; left += 1, right -= 1){
    var temporary = array[left];
      array[left] = array[right];
      array[right] = temporary;
  }
  return array
}

reverse(['hello','world','how','are','you','?'])

function getCommonDirectoryPath(pathes) {
  let split = pathes.map(path => path.split('/')), arr = [], i = 0;
   while (true) {
     let t = split[0][i];
     if (split.every(splitPath => splitPath[i] === t)) {
       arr.push(t);
       i += 1;
     } else break;
   }
   return arr.length === 0 ? '' : arr.join('/') + '/';
}

getCommonDirectoryPath(['/web/images/image1.png', '/web/images/image2.png'])


var uniqueInOrder=function(iterable){
  if (!Array.isArray(iterable)){
    x = iterable.split("")
  }
  else x = iterable
 
  for (var i = 0; i < x.length-1; i++){
    if (x[i+1] == x[i]){
      x.splice(i,1)
      i-=1
    } 
  }
  return x
}

uniqueInOrder('ABBCcAD')// == ['A', 'B', 'C', 'D', 'A', 'B']

var uniqueInOrder=function(iterable){
  return [...iterable].filter((a, i) => a !== iterable[i-1])
}

function fakeBin(x){
   arr = [];
   [...x].forEach(x=>{
    if(x < 5){
      arr.push(0)
    }
    else arr.push(1)
  })
  console.log(arr.join(""))
}

fakeBin('45385593107843568')