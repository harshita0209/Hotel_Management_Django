const nav = document.querySelector('.nav')
window.addEventListener('scroll', fixNav)

// var x = window.scrollY
// console.log(x)

function fixNav(){
    if(window.scrollY > nav.offsetHeight + 150){    //true  //false
        nav.classList.add('active')
    }
     else {
        nav.classList.remove('active')
    }

}
const textEl = document.getElementById('text')
// const speedEl = document.getElementById('speed')
const text = 'Welcome to Hotel The Grand!'
let idx = 1
let speed = 300 / 1

writeText()

function writeText() {
    textEl.innerText = text.slice(0, idx)

    idx++

    if(idx > text.length) {
        idx = 1
    }

    setTimeout(writeText, speed)
}


speedEl.addEventListener('input', (e) => speed = 300 / e.target.value)


// function myfunction(){window.location.href = "register.html";}

// var x = 0;

// document.getElementById('output-area').innerHTML = x;

// function button1() {
    
//   document.getElementById('output-area').innerHTML = ++x;
//   console.log('btn1',x)
// }

// function button2() {
//     console.log('btn2')
//   document.getElementById('output-area').innerHTML = --x;
// }
//  var x1 = 0;
//  console.log('inside bttn 1',x1)

// document.getElementById('output-area').innerHTML = x1;
// // var btn1=document.querySelector('button1')

// function btn1() {
    
//   document.getElementById('output-area').innerHTML = +x1;
//   console.log('inside bttn 1',x1)
// }

// function btn2() {
//   console.log('inside bttn 2')
//   document.getElementById('output-area').innerHTML = -x1;
//   console.log('inside bttn 2',x1)
// }

// function myFunction(x) {
//     x.classList.toggle("fa-thumbs-down");
//   }




