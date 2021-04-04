// https://www.codewars.com/kata/550498447451fbbd7600041c/train/javascript
// FUNDAMENTALS
function comp(array1, array2){
        if  (array1 == null || array2 == null) {return false}
        arr = []
        array1.sort().forEach(element => {
            arr.push(element*element)
        });
        if ((array2.sort((a,b)=>a-b)).join("") == (arr.sort((a,b)=>a-b)).join("")){
            return true
        }
        else {return false}
  }
a1 = [8, 6, 10, 0, 2, 10, 6, 3, 7, 8, 3]  ;
a2 = [9, 9, 64, 36, 36, 100, 0, 100, 4, 49, 64];
console.log(comp(a1, a2))


// better solution 
function comp(array1, array2) {
    if(array1 == null || array2 == null) return false;
    array1.sort((a, b) => a - b); array2.sort((a, b) => a - b);
    return array1.map(v => v * v).every((v, i) => v == array2[i]);
  }