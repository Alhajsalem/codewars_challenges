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
const reverseSeq = n => {
let arr = [];
    for (let i=n; i>0; i--) {
    arr.push(i);
    } return arr;
};
reverseSeq(5)//, [5, 4, 3, 2, 1]