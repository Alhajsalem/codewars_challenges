
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

function generateRange(min, max, step){
  result = [] 
  for (min; min < max+1; min += step){
    result.push(min)
  }
  return result
}
console.log(generateRange(2, 10, 2))//, [2,4,6,8,10]

function multipleOfIndex(array) {
  return array.filter((number,index)=>number%index==0)
}
console.log(multipleOfIndex([22, -6, 32, 82, 9, 25]))//, [-6, 32, 25]);

function Song(title, artist){
  this.title = title
  this.artist = artist
  this.result = []
  this.counter = 0
  this.howMany = function(names){
    names.map(name => name.toLowerCase()).forEach(name => { 
      if (!this.result.includes(name)){
        this.result.push(name)
      }   
    });
    re = this.result.length - this.counter
    this.counter = this.result.length
    return re
  }
}

const mountMoose = new Song('Mount Moose', 'The Snazzy Moose');
console.log(mountMoose.howMany(['John', 'Fred', 'BOb', 'carl', 'RyAn']))//; => 5
console.log(mountMoose.howMany(['JoHn', 'Luke', 'AmAndA']))//; => 2


function Person(name){
  this.name = name
  this.greet = function(name){
    return `Hello ${name}, my name is ${this.name}`
  }
}
var joe = new Person('Joe');
console.log(joe.greet('Kate')); // should return 'Hello Kate, my name is Joe'
console.log(joe.name)          // should == 'Joe'




Array.prototype.sortReloaded = function(ord){
  a = this.slice() 
  if (ord == undefined || ord == 'asc') {
    return a.sort((a,b) => a-b)
  }
  else if (ord == 'desc'){
    return a.sort((a,b) => b-a)
  }
  return false 
}
console.log([1, 3, 3, 4, 1].sortReloaded('desc'))

String.prototype.isUpperCase = function() {
  return !/[a-z]/.test(this);
}
console.log(' DONALD'.isUpperCase())