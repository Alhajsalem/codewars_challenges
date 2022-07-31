function countTheAnimals(animals) {
    var result = 0;
    Object.values(animals).map(a =>{
        result += parseInt(a, 2 )    
    })
    return result;
    //Object.keys(animals).reduce((p,c) => p+parseInt(a[c], 2),0);
/*     var result = 0;
    for (var key in animals) {
        result += parseInt( animals[key], 2 )
        }
    return result; */
    }


countTheAnimals({aardvark: '1101', tiger: '1100', donkey: '1100', emu: '1010'});

var orderedCount = function (text) {
  /*   var result = [];
    [...new Set(text)].forEach(item =>{
        result.push([item,(text.match(new RegExp(item, "g"))||[]).length])
    })
    return result; */
    return [...new Set(text)].map(char => {
        return [char, text.split(char).length - 1]
    })

  }
/*   const orderedCount = str => [...new Set([...str])].map(char => [char, str.split(char).length - 1])
 */
// orderedCount("abracadabra")//, [['a', 5], ['b', 2], ['r', 2], ['c', 1], ['d', 1]]],)
console.log(orderedCount("abracadabra"))