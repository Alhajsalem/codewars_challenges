// https://www.codewars.com/kata/5a00e05cc374cb34d100000d/train/javascript

// FUNDAMENTALS
const reverseSeq = n => {
    var arr = []
    for (i = 1; i < n+1; i++) { 
        arr.push(i)
      }
    return arr.reverse();
  };


 // better solution 
const reverseSeq_1 = n => {
let arr = [];
    for (let i=n; i>0; i--) {
    arr.push(i);
    } return arr;
};
reverseSeq_1(5)//, [5, 4, 3, 2, 1]

const flip = (d, a)=>{
  if (d === "R") return a.sort((x,y) => x-y);
  if (d === "L") return a.sort((x,y) => y-x);
  }
var x = flip('R', [3, 2, 1, 2])    // =>  [1, 2, 2, 3]


function smallEnough(a, limit){
    var x = []
    a.forEach(element => {
    if (element > limit){
      x.push(element)
    }
  });
  return x.length == 0 ? true :false
}
//better solution 

function smallEnough_1(a, limit){
  return a.every(x => x <= limit);
}


function countBy(x, n) {
  var z = [];
  for(var i = x; i <= x*n; i+=x){
    z.push(i)
  }
  return z;
}
console.log(countBy(2,5))

function getCount(str) {
  var vowelsCount = 0;
  str_vowels = "aeiou";
  [...str].forEach(element => {
    if (str_vowels.includes(element)){
      vowelsCount+=1
    }
  });
  return vowelsCount;
}
console.log(getCount("abracadabra"))