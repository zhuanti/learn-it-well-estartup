//計時器
$(document).ready(function(){
  // Values
  var isPaused = true;
  var isSession = true;
  var breakTime = 300;
  var breakTimer = breakTime;
  var sessionTime = 1500;
  var sessionTimer = sessionTime;

  // The timer
  var t = window.setInterval(function() {
    if(!isPaused) {
      if (isSession) {
        sessionTimer -= 1;
        setTimer(sessionTimer);
        if (sessionTimer == 0) {
          toggleMode();
          sessionTimer = sessionTime;
        }
      } else if (!isSession) {
        breakTimer -= 1;
        setTimer(breakTimer)
        if (breakTimer == 0) {
          toggleMode();
          breakTimer = breakTime;
        }
      }
    }
  }, 1000);

  // Refresh v
  function refreshValues() {
    $(".break-time").text(breakTime / 60);
    $(".session-time").text(sessionTime / 60);
    // Set clock time
    setTimer(sessionTimer);
  }

  function increaseBreak() {
    if (breakTime !== 3600) {
      breakTime += 60;
      breakTimer = breakTime;
      setTimer(breakTimer);
      refreshValues();
    }
  }

  function decreaseBreak() {
    if (breakTime !== 60) {
      breakTime -= 60;
      breakTimer = breakTime;
      setTimer(breakTimer);
      refreshValues();
    }
  }

  function increaseSession() {
    if (sessionTime !== 3600) {
      sessionTime += 60;
      sessionTimer = sessionTime;
      setTimer(sessionTimer);
      refreshValues();
    }
  }

  function decreaseSession() {
    if (sessionTime !== 60) {
      sessionTime -= 60;
      sessionTimer = sessionTime;
      setTimer(sessionTimer);
      refreshValues();
    }
  }

  function toggleButton() {
    if (!isPaused) {
      $(".pause").text("開始計時");
      isPaused = true;
    } else {
      $(".pause").text("暫停計時");
      isPaused = false;
    }
  }

  function toggleMode() {
    isSession = !isSession;
    if (isSession) {
      $("body").css("background-color", "#e55");
      $(".mode").text("讀書倒數計時:");
      $(".pause").css("color", "#e55");
    } else {
      $("body").css("background-color", "#5b5");
      $(".mode").text("休息倒數計時:");
      $(".pause").css("color", "rgb(246, 252, 245)");
    }
  }



  function setTimer(seconds) {
    var mins = Math.floor(seconds / 60);
    var secs = seconds % 60;
    if (Math.max(Math.floor(Math.log10(Math.abs(secs)), 0) + 1) == 1) {
      $(".clock").text(mins + ":" + "0" + secs);
    } else if (secs == 0) {
      $(".clock").text(mins + ":" + "00");
    } else {
      $(".clock").text(mins + ":" + secs);
    }
  }

  $(".break-up").click(function() { increaseBreak(); })
  $(".break-down").click(function() { decreaseBreak(); })
  $(".session-up").click(function() { increaseSession(); })
  $(".session-down").click(function() { decreaseSession(); })
  $(".pause").click(function() { toggleButton(); })

  refreshValues();
})

////時鐘
"use strict";

var clock = {

	clocktime: {},

  dots: document.querySelectorAll('#lcd-clock .dots'),

  dotsState: false,

  updateClock: function (){

		var time = new Date();
		clock.clocktime.hour   = time.getHours();
		clock.clocktime.minute = time.getMinutes();
		clock.clocktime.second = time.getSeconds();

		for (var timeUnit in clock.clocktime) {
			// convert all to values to string,
			// pad single values, ie 8 to 08
	 		// split the values into an array of single characters
			clock.clocktime[timeUnit] = clock.clocktime[timeUnit].toString();
			if (clock.clocktime[timeUnit].length == 1) {
				clock.clocktime[timeUnit] = '0'+clock.clocktime[timeUnit];
			}
			clock.clocktime[timeUnit] = clock.clocktime[timeUnit].split('');

			// update each digit for this time unit
			for (var i=0; i<2; i++) {
				var selector = '#lcd-clock .'+timeUnit+'.digit-'+(i+1);
				var className = 'number-is-'+clock.clocktime[timeUnit][i];
				// remove any pre-existing classname
				for (var j=0; j<10; j++) {
					var oldClass = 'number-is-'+j;
					document.querySelector(selector).classList.remove(oldClass);
				}
				// add the relevant classname to the appropriate clock digit
				document.querySelector(selector).classList.add(className);
			}

		}

		clock.toggleDots();
	},

	toggleDots: function(){

		var num_dots = clock.dots.length;

		for (var i=0; i < num_dots; i++) {
			if (clock.dotsState === false) {
				clock.dots[i].classList.add('lcd-element-active');
				continue;
			} else {
				clock.dots[i].classList.remove('lcd-element-active');
			}
		}

		clock.dotsState = !clock.dotsState;

	},

	init: function(){

		clock.toggleDots();
		clock.updateClock();
		// update every half second to make dots flash at that rate :)
		setInterval(clock.updateClock, 500);

	}

};



clock.init();


//
//$(function(){
//
//    // Cache some selectors
//
//    var clock = $('#clock'),
//        alarm = clock.find('.alarm'),
//        ampm = clock.find('.ampm');
//
//    // Map digits to their names (this will be an array)
//    var digit_to_name = 'zero one two three four five six seven eight nine'.split(' ');
//
//    // This object will hold the digit elements
//    var digits = {};
//
//    // Positions for the hours, minutes, and seconds
//    var positions = [
//        'h1', 'h2', ':', 'm1', 'm2', ':', 's1', 's2'
//    ];
//
//    // Generate the digits with the needed markup,
//    // and add them to the clock
//
//    var digit_holder = clock.find('.digits');
//
//    $.each(positions, function(){
//
//        if(this == ':'){
//            digit_holder.append('<div class="dots">');
//        }
//        else{
//
//            var pos = $('<div>');
//
//            for(var i=1; i<8; i++){
//                pos.append('<span class="d' + i + '">');
//            }
//
//            // Set the digits as key:value pairs in the digits object
//            digits[this] = pos;
//
//            // Add the digit elements to the page
//            digit_holder.append(pos);
//        }
//
//    });
//
//    // Add the weekday names
//
//    var weekday_names = 'MON TUE WED THU FRI SAT SUN'.split(' '),
//        weekday_holder = clock.find('.weekdays');
//
//    $.each(weekday_names, function(){
//        weekday_holder.append('<span>' + this + '</span>');
//    });
//
//    var weekdays = clock.find('.weekdays span');
//
//    // Run a timer every second and update the clock
//
//    (function update_time(){
//
//        // Use moment.js to output the current time as a string
//        // hh is for the hours in 12-hour format,
//        // mm - minutes, ss-seconds (all with leading zeroes),
//        // d is for day of week and A is for AM/PM
//
//        var now = moment().format("hhmmssdA");
//
//        digits.h1.attr('class', digit_to_name[now[0]]);
//        digits.h2.attr('class', digit_to_name[now[1]]);
//        digits.m1.attr('class', digit_to_name[now[2]]);
//        digits.m2.attr('class', digit_to_name[now[3]]);
//        digits.s1.attr('class', digit_to_name[now[4]]);
//        digits.s2.attr('class', digit_to_name[now[5]]);
//
//        // The library returns Sunday as the first day of the week.
//        // Stupid, I know. Lets shift all the days one position down,
//        // and make Sunday last
//
//        var dow = now[6];
//        dow--;
//
//        // Sunday!
//        if(dow < 0){
//            // Make it last
//            dow = 6;
//        }
//
//        // Mark the active day of the week
//        weekdays.removeClass('active').eq(dow).addClass('active');
//
//        // Set the am/pm text:
//        ampm.text(now[7]+now[8]);
//
//        // Schedule this function to be run again in 1 sec
//        setTimeout(update_time, 1000);
//
//    })();
//
//    // Switch the theme
//
//    $('a.button').click(function(){
//        clock.toggleClass('light dark');
//    });
//
//});