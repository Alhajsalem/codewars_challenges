function animal(obj){
    return `This ${obj.color} ${obj.name} has ${obj.legs} legs.`
  }

// const animal = (obj) => `This ${obj.color} ${obj.name} has ${obj.legs} legs.`;
// animal({name:"dog",legs:4,color:"white"})


function validateHello(greetings) {
    return /(hello|ciao|salut|hallo|hola|ahoj|czesc)/i.test(greetings)
  }

  const hellos = {
    hello: 'english',
    ciao: 'italian',
    salut: 'french',
    hallo: 'german',
    hola: 'spanish',
    ahoj: 'czech republic',
    czesc: 'polish',
    }
    
    // const validateHello = greetings => {
    //   for (key in hellos) {
    //    if (greetings.toLowerCase().includes(key)) {
    //      return true
    //    }
    //   }
    //   return false
    // }
  

function points(games) {
 let result = 0
 games.forEach(element => {
   x = parseInt(element.split(":")[0])
   y = parseInt(element.split(":")[1])
   if (x > y){
     result +=3
   }
   else{
     result += 1
   }
 });
 return(result)
}

points(["1:0","2:0","3:0","4:0","2:1","3:1","4:1","3:2","4:2","4:3"])

function evenNumbers(array, number) {
  return (array.filter(item => item % 2 == 0)).slice(-number); 
}
evenNumbers([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)

function sortByLength (array) {
   return array.sort((a, b) =>  a.length - b.length);
};

console.log(sortByLength(["Beg", "Life", "I", "To"]))//,["I", "To", "Beg", "Life"])

// https://www.codewars.com/kata/5f3afc40b24f090028233490/train/javascript


function getEvenNumbers(numbersArray){
  return numbersArray.filter(no => no % 2 == 0);
}

console.log(getEvenNumbers([1,2,3,6,8,10]))

function gooseFilter (birds) {
  var geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"];
  result = []
  birds.forEach((item)=>{
    if (!geese.includes(item)) result.push(item)
  });
  return result
};
gooseFilter(["Mallard", "Barbary", "Hook Bill", "Blue Swedish", "Crested"])//,["Mallard", "Barbary", "Hook Bill", "Blue Swedish", "Crested"]