function sumTwoSmallestNumbers(numbers) {  
    numbers.sort((a,b)=> a -b)
    return numbers[0]+numbers[1]
}
sumTwoSmallestNumbers([5, 8, 12, 19, 22])//, 13 , "Sum should be 13");


function openOrSenior(data){
    result = []
    data.forEach(element => {
        if (element[0] >= 55 & element[1] > 7){
            result.push("Senior")
        }
        else{
            result.push("Open")
        }   
    });
    return result
  }
console.log(openOrSenior([[45, 12],[55,21],[19, -2],[104, 20]]))//,['Open', 'Senior', 'Open', 'Senior']

// better solution
function openOrSenior(data){
    return data.map(function(d){
      return d[0] >= 55 && d[1] > 7 ? 'Senior' : 'Open';
    });
  }