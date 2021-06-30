// https://www.codewars.com/kata/53369039d7ab3ac506000467/train/javascript

// FUNDAMENTALSvBOOLEANS BEST PRACTICES
var assert = require('assert');

function boolToWord( bool ){
    return bool ? "Yes" : "No";
  }

assert.equal(boolToWord(true),'Yes')

// https://www.codewars.com/kata/5966e33c4e686b508700002d/train/javascript
function sumStr(a,b) {
  if (a === "") {
    a = 0
  }
  if (b === ""){
    b = 0
  }
  return (parseInt(a)+parseInt(b)).toString() 
}

// better solution 
function sumStr_1(a,b) {
  const num1 = Number(a);
  const num2 = Number(b);
  return String(num1 + num2)
}

sumStr_1("","5")

// https://www.codewars.com/kata/58f8a3a27a5c28d92e000144/train/javascript

function firstNonConsecutive (arr) {
  var min = Math.min(...arr)
  var max = Math.max(...arr)
  arr_n = []
  for (var i = min; i <= max; i ++){
    arr_n.push(i)
  }
  for (var i = 0; i <= arr_n.length; i ++){
    if (arr_n[i] != arr[i]) return (arr[i])
  }
    return null
}

firstNonConsecutive([ 1, 2, 3, 4 ])

// better solution 
function firstNonConsecutive(arr) {
  for (let i = 0; i < arr.length - 1; ++i) {
    if (arr[i] + 1 !== arr[i + 1]) {
      return arr[i + 1]
    }
  }
  return null
}

// https://www.codewars.com/kata/5715eaedb436cf5606000381/train/javascript

function positiveSum(arr) {
  var result = 0
  arr.forEach(element => {
    if (element > 0) {
      result += element
    }   
  });
  return result
}

positiveSum([1,2,3,4,5])

// https://www.codewars.com/kata/57a429e253ba3381850000fb/train/javascript

function bmi(weight, height) {
  result = weight/(Math.pow(height,2));
  if (result <= 18.5) return "Underweight"
  else if(result <= 25.0) return "Normal"
  else if(result <= 30.0) return "Overweight"
  else return "Obese"   
}

// better solution 
function bmi(weight, height) {
  var formula = (weight / Math.pow(height, 2));
  switch (true) {
    case formula <=18.5:
    return 'Underweight';
    case formula <=25.0:
    return 'Normal';
    case formula <=30:
    return 'Overweight';
    default:
    return 'Obese';
    
  }
}

const companies = [
  {name: "Company One", category: "Finance", start: 1981, end: 2003},
  {name: "Company Two", category: "Retail", start: 1992, end: 2008},
  {name: "Company Three", category: "Auto", start: 1999, end: 2007},
  {name: "Company Four", category: "Retail", start: 1989, end: 2010},
  {name: "Company Five", category: "Technology", start: 2009, end: 2014},
  {name: "Company Six", category: "Finance", start: 1987, end: 2010},
  {name: "Company Seven", category: "Auto", start: 1986, end: 1996},
  {name: "Company Eight", category: "Technology", start: 2011, end: 2016},
  {name: "Company Nine", category: "Retail", start: 1981, end: 1989}
];

const ages = [33, 12, 20, 16, 5, 54, 21, 44, 61, 13, 15, 45, 25, 64, 32];

// forEach
companies.forEach(function(iter){ // sync callback function
  return (iter["name"])
})
// Filter
var x = ages.filter(function(ages){
  return ages >40
})
const y = ages.filter(age => age > 40)
var retails_companies = companies.filter(x => x.category == "Retail")
var manipulated_name = companies.map(company => `The name of the company:${company.name}`)
// sort
var companies_sorted = companies.sort((x,y)=>{
  return x.start - y.start
})
// reduce
const age_sum = ages.reduce(function(total,age){
  return total +age
},0)


function bingo(ticket, win){
  counter = 0;
  ticket.forEach(x=>{
    for (let i = 0; i < x[0].length; i++){
      if ((x[0][i]).charCodeAt() == x[1]){
        counter+=1
      }
    }
  })
  return (counter < win) ? "Loser!" : "Winner!"
}
console.log(bingo([ [ 'WAQETSVS', 83 ],[ 'PYCSGX', 70 ],[ 'NACH', 81 ],[ 'ZAE', 90 ],[ 'AO', 82 ],[ 'IZKQXW', 72 ] ], 3))