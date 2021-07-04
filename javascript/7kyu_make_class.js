function makeClass(...params) {
    return class {
      constructor(...args) {
        params.forEach((item, i) => this[params[i]] = args[i])
      }
    }
  }

function makeClass(...properties) {
  return function (...n) {
    properties.forEach((x, y) => (this[x] = n[y]));
  };
}

const Animel = makeClass('name','species','age','health','weight','color')
const dog2 = new Animel("Bob", "Dog", "5", "good", "50lb", "brown");
console.log(dog2)
