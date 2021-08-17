//  var x = 0;

// document.getElementById('output-area').innerHTML = x;
// var btn1=document.querySelector('button1')

// function button1() {
//   document.getElementById('output-area').innerHTML = ++x;
//   console.log('inside bttn 1',x)
// }

// function button2() {
  
//   document.getElementById('output-area').innerHTML = --x;
//   console.log('inside bttn 2',x)
// }

//like and dislike toggle
function myFunction(x) {
  x.classList.toggle("fa-thumbs-down");
}
// function validateForm1() {
//   // const date1 = document.forms["myForm"]["date1"].value;
//   // const date2 = document.forms["myForm"]["date2"].value;
//   var date1=document.forms["myForm"]["date1"].value
//   // console.log('inside fun',date1.getDate())
//   // if (date2.getDate() < date1.getDate()) 
//   // {
//   //   alert("Enter the no of rooms");
//   //   return false;
//   // }
//   alert("Enter the no of rooms",date1);
//     return false;
// } 

//axios
// console.log('Hello ')
// const cancelbtn = document.querySelector('#cancel')
// console.log(cancelbtn)
// cancelbtn.addEventListener('click', cancelbooking)
// function cancelbooking()
// {
//     const id =document.querySelector('#booking_id')
//     console.log('Inside function ')
//     axios.delete('booking_view',{id:id})
//     console.log(id)
// }

const orderbtn=document.querySelector('#order')
const total=document.querySelector('#total')

orderbtn.addEventListener('click',order)
// console.log(p1.value)
function order()
{ 
const p1=document.querySelector('#inp1')
const p2=document.querySelector('#inp2')
const p3=document.querySelector('#inp3')
const a=p1.value*200
const b=p2.value*300
const c=p3.value*250
// console.log(b)
var amount=(a+b+c)
  // alert( document.getElementById('total').innerHTML);
  alert('Total Bill is '+ amount )
}