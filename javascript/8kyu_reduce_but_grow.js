//https://www.codewars.com/kata/57f780909f7e8e3183000078/train/javascript

function grow(x){
    return x.reduce((a, b)=> a*b, 1)
}



function bump(x){
    if (((x.match(/_/g) || []).length) <= 15) return "Woohoo!"
    return "Car Dead"
}
console.log(bump("n"))//, "Car Dead"

var min = function min(list){
    var min = list[0];
    for(var i= 1; i< list.length; i++) {
       if(list[i] < min){
        min = list[i]
       }
    }
    return min
}

var max = function(list){
    var max = list[0];
    for(var i= 1; i< list.length; i++) {
       if(list[i] > max){
        max = list[i]
       }
    }
    return max
}
min([-52, 56, 30, 29, -54, 0, -110])

function isIntArray(arr) {
    if (!Array.isArray(arr)) {
        return false;
      }
    for(var i = 0; i< arr.length; i++){
        if (typeof arr[i] === "string" || arr[i] === null || isNaN(arr[i]) || (Math.round(Number(arr[i]))) !== Number(arr[i])) return false
    }
    return true
  }

isIntArray([''])



function determineTime(durations){
    hours = []
    mins = []
    secs = []
    durations.forEach(element => {
        hours.push(Number(element.split(":")[0]))
        mins.push(Number(element.split(":")[1]))
        secs.push(Number(element.split(":")[2]))
        
    });

    totalMinutes = ( eval(secs.join("+")) / 60) + eval(mins.join("+"))
    console.log((totalMinutes / 60))
    var hours_total = (totalMinutes / 60) + eval(hours.join("+"))
    if (hours_total> 24){
        return false
    }
    return true
  }

determineTime(["06:00:00","12:00:00","06:30:00"])

function sumDigits(number) {
    var myArr = String(Math.abs(number)).split("").map((num)=>{
        return Number(num)
      })
    return myArr.reduce((pv, cv) => pv + cv, 0);
}

sumDigits(-32)//, 5


function mineLocation(field){
    var mine;
    field.forEach(function(row, x) {
      row.forEach(function(cell, y) {
        if (cell === 1) {
          mine = [x, y]; 
        }
      });
    });
    
    return mine;
  }

console.log(mineLocation([ [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0] ]))