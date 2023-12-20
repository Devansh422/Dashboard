function digitalclock()
{
  var time=document.getElementById("time");
  var amorpm=document.getElementById("amorpm");
  var eday=document.getElementById("eday");
  var emonth=document.getElementById("emonth");
  var timenow=new Date();

  const months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
  let month = months[timenow.getMonth()];

  const days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
  let day = days[timenow.getDay()];


  time.innerHTML=timenow.toLocaleTimeString();
  eday.innerHTML=day;
  emonth.innerHTML=month;

  var seconds = timenow.getSeconds();
  var svg = document.getElementById("svg-clock");
  svg.style.transform = 'rotate(' + (seconds * 6) + 'deg)'; 


}

window.onload=function()
{
  setInterval(digitalclock,1)
};






