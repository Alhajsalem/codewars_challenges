const result =  (x) => x.replace(/\s/g, '');
const sayHello = (name, city, state ) => `Hello, ${name.join(' ')}! Welcome to ${city}, ${state}!`;
const binToDec = (bin) =>  parseInt( bin, 2 );
console.log(sayHello(['John', 'Smith', 'martin'], 'Phoenix', 'Arizona'));
console.log(result('8 j 8   mBliB8g  imjB8B8  jl  B'))
console.log(binToDec("1001001"))


