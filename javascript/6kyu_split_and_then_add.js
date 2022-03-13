//https://www.codewars.com/kata/58da7ae9b340a2440500009c/train/javascript
function pointInCircle(x,y){
    if ((x ** 2 + y **2) <1) return true
    return false
}
  pointInCircle(0,0)

function createSecretHolder(secret) {
       var secret = secret
       return {
        getSecret: function () {
          return secret
        },
        setSecret: function (secret) {
            this.secret = secret
          },
      };    
}
obj = createSecretHolder(5)
console.log(obj.getSecret())


class obj {
    constructor(secret) {
      this.sec = secret;
    }
    
    getSecret(){
      return this.sec;
    }
    
    setSecret(val){
      this.sec = val;
    }
  }
  
  function createSecretHolder(secret) {
    var y = new obj(secret);
    return y;
  }