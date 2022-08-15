/*
  CREDIT FOR TUTORIAL:
  https://www.youtube.com/watch?v=3PZAlID3T78
*/
$(document).ready(function(){
  $('.toggle').click(function() {
    $('.sidebar-contact').toggleClass('active')
    $('.toggle').toggleClass('active')
  })
})