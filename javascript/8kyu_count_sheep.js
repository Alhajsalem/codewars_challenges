var countSheep = function (num){
    var result = "";
    for (let i = 1; i <= num; i++) { 
        result += i + " sheep...";
      }
      return result;
  }

/*   var countSheep = function (num){
    let str = "";
    for(let i = 1; i <= num; i++) { str+= `${i} sheep...`; }
    return str;
  } */
countSheep(3)

const zeroFuel = (distanceToPump, mpg, fuelLeft) => {
  return mpg * fuelLeft >= distanceToPump;
};

function factorial(n){
  var i = 0;
  var result = 1;
  while (i < n) {
    result *= (n-i)
    i++;
  }
  return result
}

factorial(7)//, 5040);


function solution(a) {
  let counter = 0;
  let newIndex = 0;
  function theFunction (oldIndex){
  counter++;
  newIndex = oldIndex + a[oldIndex];
  console.log(newIndex)
  if (typeof a[newIndex] === 'undefined'){
  return counter;
  }
  else {
      theFunction(newIndex);
  };
  };
  let theCounter = theFunction(a[0]);
  return theCounter;
}
console.log(solution([1, 1, 1, 1]))//, 4);