function launchAll(launchMissile) {
    for(let i = 0; i < 5; i++) {
      setTimeout(function() {
        launchMissile(i);
      }, i * 1000);
    }
  }

function incrementer(nums) { 
  return nums.map((currElement, index) => {
    return ((index+1+currElement))%10
  });  
}
console.log(incrementer([3, 6, 9, 8, 9]))//, [4, 8, 2, 2, 4])

function duplicateElements(m, n) {
  for(var i =0;i < m.length; i++){
    if (n.includes(m[i])){
      console.log(m[i])
      return true;
    } 
  }
  return false
}
m = [ -818821,
  210211,
  362081,
  -921546,
  816536,
  328776,
  890529,
  661866,
  -11561,
  683240,
  -848875,
  -951486,
  -248358,
  -526092,
  -605340,
  -804723,
  26220,
  -972271,
  663945,
  -895230,
  -277635,
  -607823,
  113327,
  -224579,
  700657,
  145393,
  -809229,
  -761722,
  482606,
  605742,
  -938521,
  -150395,
  109030,
  -854922,
  264881,
  -285887,
  844666,
  -400699,
  735944,
  -798910,
  101296,
  624475,
  -944289,
  -669136,
  -825130,
  -721758,
  880130,
  816871,
  -777109,
  -689051,
  998843,
  290054,
  840365,
  -231982,
  -371850,
  -919852,
  -923694,
  -468233,
  874151,
  -526232,
  -781482,
  867826,
  675563,
  -64610,
  -361822,
  728867,
  922650,
  599537,
  368492,
  395213,
  -95147,
  885776 ] 
n = [ 624475,
  -770300,
  -99776,
  -370960,
  -131284,
  -109209,
  775193,
  432567,
  -261565,
  -132478,
  -163377,
  -484310,
  -812942,
  -609872,
  702573,
  996026,
  -914409,
  744631,
  575242,
  622843,
  488830,
  749327,
  -965220,
  -582848,
  -515386,
  -379267,
  -823812,
  -51614,
  -29000,
  -749373,
  826038 ]
console.log(duplicateElements(m,n))