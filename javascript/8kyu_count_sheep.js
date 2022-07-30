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