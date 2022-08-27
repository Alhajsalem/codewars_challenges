String.prototype.check = function () {
    var a = this.toString();
    //return String.fromCharCode(this.toString().charCodeAt(0) - 32)
    return String.fromCharCode(a.charCodeAt(0)>96 && a.charCodeAt(0)<123 ? a.charCodeAt(0)-32: a.charCodeAt(0))
  }

String.prototype.capitalize = function() {
    return this.toString().charAt(0).check()+this.toString().slice(1)
  }
  
console.log("an apple a day keeps the doctor away".capitalize())


function century(year) {
  return Math.ceil(year/100);
}
century(1705)

function generateShape(integer){
  
  var result = "";
  for(var i = 2 ; i <= integer; i++){
    result += "\n"+"+".repeat(integer);
  }
  return "+".repeat(integer) + result;

}
console.log(generateShape(8));