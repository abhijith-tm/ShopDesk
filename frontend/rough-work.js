//variables

let age=22
age =24
//reassignable
const height =172
//non reasignable

//functions
function sayHello(){
    console.log("hello")
}

sayHello//reference
sayHello()

//hoisting: calling before declaring
sayHi()
function sayHi(){
    console.log("hi.. iam hoisted")
}

//storing function 
const greet = function(){ //using const is good practice so it wont change
    console.log("hellooo. iam stored ftn")
}
greet()

const welcome = greet //welcome also now points to same ftn
welcome()

//passing function to another ftn -- callback
function doSomething(callback) {
    console.log("Doing something...");

    callback();
}

function finished() {
    console.log("Finished!");
}

doSomething(finished);//call this later

//exercises
function execute(callback) {
    console.log("A");
    callback();
    console.log("C");
}

function hello() {
    console.log("B");
}

execute(hello);