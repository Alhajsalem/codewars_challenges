https://www.codewars.com/kata/52f3bb2095d6bfeac2002196/train/javascript 

var validWord = function(valuesArray, word) {
    if (sortAlphabet(word) ==  sortAlphabet(valuesArray.join(""))){
        return true
    } 
    else {
        return false
    } 
}
function sortAlphabet(str) {
    return [...str].sort((a, b) => a.localeCompare(b)).join("");
  }

validWord(['code','wars'], 'CodeStarsWar')


function isPrime(n) {
    if (n <= 1) return false
    else if (n <= 3) return true
    else if ((n % 2 == 0)  || (n % 3 == 0)) {return true} 
    i = 5
    while (i*i <= n) {
      if ((n % i == 0) ||  (n % (i + 2) == 0)) return true
      i = i + 6
    }
    return true
   }
    


function getMiddle(s){
  str_len = s.length;
  if (str_len % 2 !== 0){
    return(s.charAt(str_len/2))
  }
  else{
    return(s.charAt((str_len/2)-1)+s.charAt((str_len/2)))
  }
}

getMiddle("test")//,"es");
getMiddle("testing")//,"t");
getMiddle("middle")//,"dd");
getMiddle("A")//,"A");
var numbers = [1, 2, 3, 4, 5];
Array.prototype.sum = function () {
    var total = 0;
    for (var i = 0; i < this.length; i++) {
        total += this[i];
    }
    return total;
};
Array.prototype.square = function () {
  result = []
  this.forEach(x=>{
    result.push(x*x)
  })
  return result
};
Array.prototype.cube = function () {
  result = []
  this.forEach(x=>{
    result.push(x*x*x)
  })
  return result
};
Array.prototype.average = function () {
  return this.sum() / this.length;
};

Array.prototype.even = function () {
  return this.filter(item => item % 2 === 0)
};

Array.prototype.odd = function () {
  return this.filter(item => item % 2 !== 0)
};

numbers.square();  // must return [1, 4, 9, 16, 25]
numbers.cube();    // must return [1, 8, 27, 64, 125]
numbers.average(); // must return 3
numbers.sum();     // must return 15
numbers.even();    // must return [2, 4]
numbers.odd();     // must return [1, 3, 5]

function validPhoneNumber(phoneNumber){
  return /^\(\d{3}\) \d{3}\-\d{4}$/.test(phoneNumber);
}

// console.log(validPhoneNumber("(123) 456-7890"))//, true)
// validPhoneNumber("(123) 456-7890") // =>  returns true
// validPhoneNumber("(1111)555 2345") // => returns false
// validPhoneNumber("(098) 123 4567") // => returns false


function phonenumber(inputtxt) {
  var regex = /^\(?([0-9]{3})\)?[-. ]?([0-9]{3})[-. ]?([0-9]{4})$/;
   console.log(regex.test(inputtxt))

}

console.log(phonenumber("(1111)555 2345"))