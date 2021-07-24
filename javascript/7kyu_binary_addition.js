function addBinary(a,b) {
    return Number(a+b).toString(2)
}
addBinary(1, 1) //== "10"

var number = function(busStops){
    
    return busStops.map(subarray => subarray[0]-subarray[1]).reduce((a, b) => a + b)
  }
number([[10,0],[3,5],[5,8]])


// 1 + 1/4 + 1/7 + 1/10 + 1/13 = "1.57"
function SeriesSum(n){
   num = 0
  for(var i = 0; i < n;i++){
    num = i+num
    console.log(num)

  }
}
SeriesSum(5)