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
    


consisPrime(0)
