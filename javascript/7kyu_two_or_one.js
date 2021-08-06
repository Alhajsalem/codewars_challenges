
function longest(s1, s2) {
    return [...new Set([...s1 + s2])].sort().join('')
  }


  longest("aretheyhere", "yestheyarehere")//, "aehrsty")

function check(a, x) {
  console.log(a.includes(x))
}
check([66, 101], 100)//, true)

function toWeirdCase(string){
  return string.split(' ').map(function(word){
    return word.split('').map(function(letter, index){
      return index % 2 == 0 ? letter.toUpperCase() : letter.toLowerCase()
    }).join('');
  }).join(' ');
}

toWeirdCase( "Weird string case" );//=> returns "WeIrD StRiNg CaSe"

function removeEveryOther(arr){
   return arr.filter((item,index) => index %2 == 0)
}
removeEveryOther(['Hello', 'Goodbye', 'Hello Again'])//,['Hello', 'Hello Again']);

function solution(nums){
  return (nums || []).sort((a,b)=> a-b)
}
solution([1,2,3,10,5])//, [1,2,3,5,10])
solution(null)//, []))

function nameShuffler(str){
  return str.split(" ").reverse().join(" ")
}
nameShuffler('john McClane')//; => "McClane john"

// Sum Numbers
function sum (numbers) {
  return numbers.reduce((a, b) => a + b, 0)
};

console.log(sum([]))//, 0;
console.log(sum([1, 5.2, 4, 0, -1]))//, 9.2;

var breakChocolate = function(n, m) {
  return (n*m === 0) ? 0 : n * m - 1;
 };

 function removeUrlAnchor(url){
  
  return url.split("#")[0]
}

removeUrlAnchor('www.codewars.com#about')//, 'www.codewars.com')
