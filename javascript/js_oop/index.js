let circle = {
  radius: 1,
  location: {
    x: 1,
    y: 1,
  },
  draw: function () {
    console.log("draw");
  },
};

//Factory Function
function createCircule(radius) {
  return {
    radius,
    draw: function () {
      console.log("draw");
    },
  };
}
// Constrocutor Function

console.log(this);
function Circle(radius) {
  let age = function () {
    console.log("called from age");
  };
  this.radius = radius;
  this.draw = function () {
    age();
    console.log("draw");
  };
  Object.definePropertry(this, "defaultLocation", {
    get: function () {
      return age;
    },
    set: function () {},
  });
}
const another = new Circle(1);
console.log((another.age = 199));

// for (let key in another){
//     console.log(key,circle[key])
// }
// const keys = Object.keys(another)
// console.log(keys)
