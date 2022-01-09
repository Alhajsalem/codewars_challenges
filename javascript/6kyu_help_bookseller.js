function f(x, cc) {
  const keys = Object.keys(cc);
  for (let i = 0; i < keys.length; i++) {
    const key = keys[i];
    if (cc[key] == x) {
      return cc[keys[(i + 1) % keys.length]];
    }
  }
}
f(3, { a: 3, b: 4, c: 5 }); //, 4

// better solution
function f(x, obj) {
  const arr = Object.values(obj);
  let ind = arr.indexOf(x);
  ind++;
  return arr[ind % 3];
}

function singleDigit(n) {
  if (n < 10) return n;
  sum = n
    .toString(2)
    .toString()
    .split("")
    .map(Number)
    .reduce(function (a, b) {
      return a + b;
    }, 0);
  console.log(sum);
  if (sum >= 10) {
    return singleDigit(sum);
  } else {
    return sum;
  }
}
// better solution
function singleDigit(n) {
  while (n >= 10) {
    n = (n.toString(2).match(/1/g) || []).length;
  }
  return n;
}
console.log(singleDigit(443566));
