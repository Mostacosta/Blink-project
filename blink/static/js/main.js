$(document).ready(function(){

  //delay href action
  $(".btnAction").click(function() {
    var href = $(this).attr('href');
    //$("body").css('pointer-events','none');
    $(".center").children().not(this).css('opacity', '.5');

    // Delay setting the location for one second
    setTimeout(function() {window.location = href}, 1500);
    return false;

});


const buttons = Array.from(document.querySelectorAll(".button"));
const count = buttons.length;
const increase = Math.PI * 2 / buttons.length;
const radius = 250;
let angle = 0;

buttons.forEach((button, i) => {
  button.style.top = Math.sin(-Math.PI / 2 + i * increase) * radius + "px";
  button.style.left = Math.cos(-Math.PI / 2 + i * increase) * radius + "px";
  button.addEventListener("click", move);
});

function move(e) {
  const n = buttons.indexOf(e.target);
  const endAngle = (n % count) * increase;
  (function turn() {
    if (Math.abs(endAngle - angle) > 1 / 8) {
      const sign = endAngle > angle ? 1 : -1;
      angle = angle + sign / 8;
      setTimeout(turn, 20);
    } else {
      angle = endAngle;
    }

    /* Rotation *//*
    buttons.forEach((button, i) => {
      button.style.top =
        Math.sin(-Math.PI / 2 + i * increase - angle) * radius + "px";
      button.style.left =
        Math.cos(-Math.PI / 2 + i * increase - angle) * radius + "px";
    });*/
    
  })();
}

if (window.matchMedia('(max-width: 600px)').matches)
{
  const buttons = Array.from(document.querySelectorAll(".button"));
  const count = buttons.length;
  const increase = Math.PI * 2 / buttons.length;
  const radius = 130;
  let angle = 0;

  buttons.forEach((button, i) => {
  button.style.top = Math.sin(-Math.PI / 2 + i * increase) * radius + "px";
  button.style.left = Math.cos(-Math.PI / 2 + i * increase) * radius + "px";
  button.addEventListener("click", move);
  });

  function move(e) {
  const n = buttons.indexOf(e.target);
  const endAngle = (n % count) * increase;
  (function turn() {
    if (Math.abs(endAngle - angle) > 1 / 8) {
      const sign = endAngle > angle ? 1 : -1;
      angle = angle + sign / 8;
      setTimeout(turn, 20);
    } else {
      angle = endAngle;
    }

    /* Rotation *//*
    buttons.forEach((button, i) => {
      button.style.top =
        Math.sin(-Math.PI / 2 + i * increase - angle) * radius + "px";
      button.style.left =
        Math.cos(-Math.PI / 2 + i * increase - angle) * radius + "px";
    });*/
    
  })();
  }
}






/** Videos of achievements **/ 
$(".box-video").click(function(){
  str = $('iframe',this)[0].src;
  res = str.replace('autoplay=0','autoplay=1');
  $('iframe',this)[0].src = res;
  $(this).addClass('open');
});


document.addEventListener('play', function(e){
  var audios = document.getElementsByTagName('audio');
  for(var i = 0, len = audios.length; i < len;i++){
      if(audios[i] != e.target){
          audios[i].pause();
      }
  }
}, true);

});