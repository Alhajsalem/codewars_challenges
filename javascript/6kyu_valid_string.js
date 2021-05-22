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


function even_or_odd(number) {
    return (number % 2 == 0) ? "Even": "Odd"
  }
