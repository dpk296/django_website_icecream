// challenge1: your age in days
function ageindays(){
    var age=prompt("Enter Your birth Year");
    var days=2021-age;
    // console.log(days);
    // create element is used to create one variable here h1 is a variable
    var h1=document.createElement("p");
    // here p is the tag that what sige shoud be the answer
    // creating text inside the created element 
    var answer=document.createTextNode("You Are "+days+" Years Old");
    // creating age
    h1.setAttribute('id', 'ageindays');
    h1.appendChild(answer);
    document.getElementById('innerage1').appendChild(h1);
  
}

function reset(){
    document.getElementById('ageindays').remove();
}
   
