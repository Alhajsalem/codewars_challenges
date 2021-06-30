function removeExclamationMarks(s) {
    return s.replace(new RegExp("!", 'g'),"");
  }
removeExclamationMarks("Hello World!")


function solution(string) {
   arr = [];
  [...string].forEach((character)=>{
    if (character == character.toUpperCase()) {
      arr.push(" "+character)
     }
     else{
     arr.push(character)
     }
  })
   return(arr.join("")) 
}

solution('camelCasing')

// better soltion 
const solution_1 = string => {
  return [...string].map((char) => {
    return (char === char.toUpperCase()) ? ` ${char}` : char;
  }).join('');
}

function count (string) {  
   result = {}
   for (var i = 0; i < string.length; i++){
    const items = [...string].filter(l => l === string[i]).length;
    result[string[i]] = items
   }
   return result
}

function count (string) {
  var result = {};
  
  for(let i = 0; i < string.length; i++) {
    if(result.hasOwnProperty(string[i])){
      result[string[i]] += 1;
    } else {
      result[string[i]] = 1;
    }
  }
  
  return result;
}

function shiftedDiff(first,second){
  if (first == second) return 0
  var result = ""
  counter = 0
  for (var i=0; i< first.length; i++){
   // const rot = s => s.substring(1) + s.charAt(0);
   result = first.slice(-1) + first.substring(0, first.length-1);
   first = result
   counter+=1
   if (result == second){
    return counter
   }
  }
  return -1
}
console.log(shiftedDiff(" "," "),)//, -1)