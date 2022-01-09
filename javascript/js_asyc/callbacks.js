function printString(){
    console.log("Tom"); 
    setTimeout(function()  { console.log("Jacob"); }, 3000); 
   console.log("Mark")
 }
 
 printString();

 const myFirstPromise = new Promise((resolve, reject) => { 
    const condition = true;   
    if(condition) {
         setTimeout(function(){
             resolve("Promise is resolved!"); // fulfilled
        }, 3000);
    } else {    
        reject('Promise is rejected!');  
    }
})

myFirstPromise.then((x)=>{
    console.log(x)
})