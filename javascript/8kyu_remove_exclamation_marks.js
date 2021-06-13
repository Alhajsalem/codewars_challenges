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