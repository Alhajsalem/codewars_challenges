
function longest(s1, s2) {
    return [...new Set([...s1 + s2])].sort().join('')
  }


  longest("aretheyhere", "yestheyarehere")//, "aehrsty")

function check(a, x) {
  console.log(a.includes(x))
}
check([66, 101], 100)//, true)

function toWeirdCase(string){
  return string.split(' ').map(function(word){
    return word.split('').map(function(letter, index){
      return index % 2 == 0 ? letter.toUpperCase() : letter.toLowerCase()
    }).join('');
  }).join(' ');
}

toWeirdCase( "Weird string case" );//=> returns "WeIrD StRiNg CaSe"


  //   if (index % 2 == 0){
  //           result.push(ch.toUpperCase())
  //         }
  //         else{
  //           result.push(ch.toLowerCase())
  //         }});
  //  console.log(result)

//   [...string].forEach((ch,index) =>{
//     if (index % 2 == 0){
//       result.push(ch.toUpperCase())
//     }
//     else{
//       result.push(ch.toLowerCase())
//     }
//   })
//   console.log(result.join(""))
// }