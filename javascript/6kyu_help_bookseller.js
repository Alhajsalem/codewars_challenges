function f(x, cc) { 
    const keys = Object.keys(cc);
    for (let i = 0; i < keys.length; i++) {
      const key = keys[i];  
      if (cc[key] == x){
        return(cc[keys[(i+1) % keys.length]]);
      }
    }
  }
f( 3, { a:3, b:4, c:5 } )//, 4 

// better solution
function f(x, obj) { 
    const arr = Object.values(obj)
    let ind = arr.indexOf(x)
    ind++
    return arr[ind % 3]
  }