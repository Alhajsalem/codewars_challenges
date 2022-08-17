// https://www.codewars.com/kata/5f8341f6d030dc002a69d7e4/train/javascript

function leastLarger(a,i) {
    let s = Infinity;
    let result = -1;
    for (let index = 0; index < a.length; index++) { 
        if (a[index] > a[i] && a[index] <s ){
            s = a[index];
            result = index      
        }
      }
    return result;
  }

/*   function leastLarger(a, i) {
    const targetVal = a[i]
    const largerVals = a.filter(num => num > targetVal)
    const leastLargeVal = Math.min(...largerVals)
    
    return a.findIndex(num => num === leastLargeVal)
}
 */
  console.log(leastLarger( [1, 3, 5, 2, 4], 0 ))//, 3 )//, 3 )