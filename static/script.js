let menuBtn = document.querySelector('#m'); 
let navbar = document.querySelector('.header .top-bar .navbar'); 

/*when the "menuBtn" element is clicked, the code will toggle the "fa-times" class on and off, which could trigger a visual change in the appearance of the button or other related elements.*/
menuBtn.onclick = () =>{
    menuBtn.classList.toggle('fa-times');
    navbar.classList.toggle('active');
}

/*leftOrRightLetter*/
  function redirectLetter() {
    var message = "Note:\n\nIf you're wearing a wrist compression strap or Medic Elastic wrist hand sprain, it’s recommended to remove it before using the hand gesture recognition system.\n\nSimilarly, if you’re wearing rings, it’s advisable to remove them as well.\n\nPlease keep in mind that switching between gestures may take a few seconds for the system to recognize and respond to the new gestures. During this time, it’s recommended to keep both hands outside the frame to avoid any unwanted interference.\n\nThank you for your cooperation and enjoy using our hand gesture recognition system!";

    if (document.getElementById('left-handed').checked) {
      window.location.href = 'LeftLetterLesson';
    } else if (document.getElementById('right-handed').checked) {
      window.location.href = 'RightLetterLesson';
    } else {
      var errorMessage = "Please select your hand preference.";
      alert(errorMessage);
    }

    // Display the message
    alert(message);
  }

/*leftOrRightNumber */
function redirectDigit() {
    var message = "Note:\n\nIf you're wearing a wrist compression strap or Medic Elastic wrist hand sprain, it’s recommended to remove it before using the hand gesture recognition system.\n\nIf you’re wearing rings, it’s advisable to remove them as well.\n\n Your hand must be fully seen in the frame and not covered by sleeves \n\nPlease keep in mind that switching between gestures may take a few seconds for the system to recognize and respond to the new gestures. During this time, it’s recommended to keep both hands outside the frame to avoid any unwanted interference.\n\nThank you for your cooperation and enjoy using our hand gesture recognition system!";

    if (document.getElementById('left-handed').checked && document.getElementById('wales').checked) {
      alert(message);
      window.location.href = 'LeftNumberW';
    } else if (document.getElementById('left-handed').checked && document.getElementById('england').checked) {
        alert(message);
      window.location.href = 'leftLesson';
    } else if (document.getElementById('right-handed').checked && document.getElementById('wales').checked) {
        alert(message);
      window.location.href = 'RightNumberW';
    } else if (document.getElementById('right-handed').checked && document.getElementById('england').checked) {
        alert(message);

      window.location.href = 'rightLesson';
    }else {
      var errorMessage = "Please select your hand preference.";
      alert(errorMessage);
    }
  }

/*function for stopping the video feed */
function stopVideo() {z
  document.getElementById("video-feed-left").src = "";
  document.getElementById("video-feed-left").style.display = "none";
}
// To set a URL to id element
function startVideoLeft(mode) {
  const urls = {
    "letter_A_left": "/video_feed_left/letter_A_left",
    "letter_B_left": "/video_feed_left/letter_B_left",
    "letter_C_left": "/video_feed_left/letter_C_left",
    "letter_D_left": "/video_feed_left/letter_D_left",
    "letter_P_left": "/video_feed_left/letter_P_left",
    "start": "/video_feed_left/start",
    "number_one_left": "/video_feed_left/number_one_left",
    "number_one_right": "/video_feed_left/number_one_right",
    "number_two_left": "/video_feed_left/number_two_left",
    "number_two_right": "/video_feed_left/number_two_right",
    "number_three_left": "/video_feed_left/number_three_left",
    "number_three_right": "/video_feed_left/number_three_right",
    "number_four_left": "/video_feed_left/number_four_left",
    "number_four_right": "/video_feed_left/number_four_right",
    "number_five_left": "/video_feed_left/number_five_left",
    "number_five_right": "/video_feed_left/number_five_right",
    "number_six_left": "/video_feed_left/number_six_left",
    "number_six_right": "/video_feed_left/number_six_right",
    "number_seven_left": "/video_feed_left/number_seven_left",
    "number_seven_right": "/video_feed_left/number_seven_right",
    "number_eight_left": "/video_feed_left/number_eight_left",
    "number_eight_right": "/video_feed_left/number_eight_right",
    "number_nine_left": "/video_feed_left/number_nine_left",
    "number_nine_right": "/video_feed_left/number_nine_right",
    "letter_A_right": "/video_feed_left/letter_A_right",
    "letter_B_right": "/video_feed_left/letter_B_right",
    "letter_C_right": "/video_feed_left/letter_C_right",
    "letter_D_right": "/video_feed_left/letter_D_right",
    "letter_P_right": "/video_feed_left/letter_P_right",

    "House-sign": "/video_feed_left/House-sign",
    "number_six_right_wales": "/video_feed_left/number_six_right_wales",
    "number_six_left_wales": "/video_feed_left/number_six_left_wales"
  };

  // To see if the mode does actually exists
  if (urls[mode]) {
    document.getElementById("video-feed-left").src = urls[mode];
  } else {
    console.log("Invalid mode");
    return;
  }

  document.getElementById("video-feed-left").style.display = "block";
}

/*function to show the selected image and start the video feed for the selected sign */

function showImageLeft(imageId) {
  var imgAL = document.getElementById("letter-A-sign-left");
  var imgBL = document.getElementById("letter-B-sign-left");
  var imgCL = document.getElementById("letter-C-sign-left");
  var imgDL = document.getElementById("letter-D-sign-left");
  var imgPL = document.getElementById("letter-P-sign-left");
  var imgOne = document.getElementById("one-left-sign");
  var imgOneR = document.getElementById("one-right-sign");
  var imgTwo = document.getElementById("two-left-sign");
  var imgTwoR = document.getElementById("two-right-sign");
  var imgThree = document.getElementById("three-left-sign");
  var imgThreeR = document.getElementById("three-right-sign");
  var imgFour = document.getElementById("four-left-sign");
  var imgFourR = document.getElementById("four-right-sign");
  var imgFive = document.getElementById("five-left-sign");
  var imgFiveR = document.getElementById("five-right-sign");
  var imgSix = document.getElementById("six-left-sign");
  var imgSixR = document.getElementById("six-right-sign");
  var imgSeven = document.getElementById("seven-left-sign");
  var imgSevenR = document.getElementById("seven-right-sign");
  var imgEight = document.getElementById("eight-left-sign");
  var imgEightR = document.getElementById("eight-right-sign");
  var imgNine = document.getElementById("nine-left-sign");
  var imgNineR = document.getElementById("nine-right-sign");
  var imgAR = document.getElementById("letter-A-sign");
  var imgBR = document.getElementById("letter-B-sign");
  var imgCR = document.getElementById("letter-C-sign");
  var imgDR = document.getElementById("letter-D-sign");
  var imgPR = document.getElementById("letter-P-sign");

  var imgH = document.getElementById("House-sign");
  var img6W = document.getElementById("Number-six-sign-wales")
  var img6WL = document.getElementById("Number-six-sign-wales-left")


  if (imageId === "one-left-sign") {
    imgOne.style.display = "block";
    imgTwo.style.display = "none";
    imgThree.style.display = "none";
    imgFour.style.display = "none";
    imgFive.style.display = "none";
    imgSix.style.display = "none";
    imgSeven.style.display = "none";
    imgEight.style.display = "none";
    imgNine.style.display = "none";
    startVideoLeft("number_one_left");  // to start the video feed
  } else if (imageId === "one-right-sign") {
    imgOneR.style.display = "block";
    imgTwoR.style.display = "none";
    imgThreeR.style.display = "none";
    imgFourR.style.display = "none";
    imgFiveR.style.display = "none";
    imgSixR.style.display = "none";
    imgSevenR.style.display = "none";
    imgEightR.style.display = "none";
    imgNineR.style.display = "none";
    startVideoLeft("number_one_right");
  } else if (imageId === "two-left-sign") {
    imgTwo.style.display = "block";
    imgOne.style.display = "none";
    imgThree.style.display = "none";
    imgFour.style.display = "none";
    imgFive.style.display = "none";
    imgSix.style.display = "none";
    imgSeven.style.display = "none";
    imgEight.style.display= "none";
    imgNine.style.display = "none";
    startVideoLeft("number_two_left");
  } else if (imageId === "two-right-sign") {
    imgTwoR.style.display = "block";
    imgOneR.style.display = "none";
    imgThreeR.style.display = "none";
    imgFourR.style.display = "none";
    imgFiveR.style.display = "none";
    imgSixR.style.display = "none";
    imgSevenR.style.display = "none";
    imgEightR.style.display = "none";
    imgNineR.style.display = "none";
    startVideoLeft("number_two_right");
  }else if (imageId === "three-left-sign") {
    imgTwo.style.display = "none";
    imgOne.style.display = "none";
    imgThree.style.display = "block";
    imgFour.style.display = "none";
    imgFive.style.display = "none";
    imgFive.style.display = "none";
    imgSix.style.display = "none";
    imgSeven.style.display = "none";
    imgEight.style.display = "none";
    imgNine.style.display = "none";
    startVideoLeft("number_three_left");
  } else if (imageId === "three-right-sign") {
    imgTwoR.style.display = "none";
    imgOneR.style.display = "none";
    imgThreeR.style.display = "block";
    imgFourR.style.display = "none";
    imgFiveR.style.display = "none";
    imgSixR.style.display = "none";
    imgSevenR.style.display = "none";
    imgEightR.style.display = "none";
    imgNineR.style.display = "none";
    startVideoLeft("number_three_right");
  } else if (imageId === "four-left-sign") {
    imgTwo.style.display = "none";
    imgOne.style.display = "none";
    imgThree.style.display = "none";
    imgFour.style.display = "block";
    imgFive.style.display = "none";
    imgSix.style.display = "none";
    imgSeven.style.display = "none";
    imgEight.style.display = "none";
    imgNine.style.display = "none";
    startVideoLeft("number_four_left");
  } else if (imageId === "four-right-sign") {
    imgTwoR.style.display = "none";
    imgOneR.style.display = "none";
    imgThreeR.style.display = "none";
    imgFourR.style.display = "block";
    imgFiveR.style.display = "none";
    imgSixR.style.display = "none";
    imgSevenR.style.display = "none";
    imgEightR.style.display = "none";
    imgNineR.style.display = "none";
    startVideoLeft("number_four_right");
  } else if (imageId === "five-left-sign") {
    imgTwo.style.display = "none";
    imgOne.style.display = "none";
    imgThree.style.display = "none";
    imgFour.style.display = "none";
    imgFive.style.display = "block";
    imgSix.style.display = "none";
    imgSeven.style.display = "none";
    imgEight.style.display = "none";
    imgNine.style.display = "none";
    startVideoLeft("number_five_left");
  } else if (imageId === "five-right-sign") {
    imgTwoR.style.display = "none";
    imgOneR.style.display = "none";
    imgThreeR.style.display = "none";
    imgFourR.style.display = "none";
    imgFiveR.style.display = "block";
    imgSixR.style.display = "none";
    imgSevenR.style.display = "none";
    imgEightR.style.display = "none";
    imgNineR.style.display = "none";
    startVideoLeft("number_five_right");
  } else if (imageId === "six-left-sign") {
    imgTwo.style.display = "none";
    imgOne.style.display = "none";
    imgThree.style.display = "none";
    imgFour.style.display = "none";
    imgFive.style.display = "none";
    imgSix.style.display = "block";
    imgSeven.style.display = "none";
    imgEight.style.display = "none";
    imgNine.style.display = "none";
    startVideoLeft("number_six_left");
  } else if (imageId === "six-right-sign") {
    imgTwoR.style.display = "none";
    imgOneR.style.display = "none";
    imgThreeR.style.display = "none";
    imgFourR.style.display = "none";
    imgFiveR.style.display = "none";
    imgSixR.style.display = "block";
    imgSevenR.style.display = "none";
    imgEightR.style.display = "none";
    imgNineR.style.display = "none";
    startVideoLeft("number_six_right");
  } else if (imageId === "seven-left-sign") {
    imgTwo.style.display = "none";
    imgOne.style.display = "none";
    imgThree.style.display = "none";
    imgFour.style.display = "none";
    imgFive.style.display = "none";
    imgSix.style.display = "none";
    imgSeven.style.display = "block";
    imgEight.style.display = "none";
    imgNine.style.display = "none";
    startVideoLeft("number_seven_left");
  } else if (imageId === "seven-right-sign") {
    imgTwoR.style.display = "none";
    imgOneR.style.display = "none";
    imgThreeR.style.display = "none";
    imgFourR.style.display = "none";
    imgFiveR.style.display = "none";
    imgSixR.style.display = "none";
    imgSevenR.style.display = "block";
    imgEightR.style.display = "none";
    imgNineR.style.display = "none";
    startVideoLeft("number_seven_right");
  } else if (imageId === "eight-left-sign") {
    imgTwo.style.display = "none";
    imgOne.style.display = "none";
    imgThree.style.display = "none";
    imgFour.style.display = "none";
    imgFive.style.display = "none";
    imgSix.style.display = "none";
    imgSeven.style.display = "none";
    imgEight.style.display = "block";
    imgNine.style.display = "none";
    startVideoLeft("number_eight_left");
  } else if (imageId === "eight-right-sign") {
    imgTwoR.style.display = "none";
    imgOneR.style.display = "none";
    imgThreeR.style.display = "none";
    imgFourR.style.display = "none";
    imgFiveR.style.display = "none";
    imgSixR.style.display = "none";
    imgSevenR.style.display = "none";
    imgEightR.style.display = "block";
    imgNineR.style.display = "none";
    startVideoLeft("number_eight_right");
  } else if (imageId === "nine-left-sign") {
    imgTwo.style.display = "none";
    imgOne.style.display = "none";
    imgThree.style.display = "none";
    imgFour.style.display = "none";
    imgFive.style.display = "none";
    imgSix.style.display = "none";
    imgSeven.style.display = "none";
    imgEight.style.display = "none";
    imgNine.style.display = "block";
    startVideoLeft("number_nine_left");
  } else if (imageId === "nine-right-sign") {
    imgTwoR.style.display = "none";
    imgOneR.style.display = "none";
    imgThreeR.style.display = "none";
    imgFourR.style.display = "none";
    imgFiveR.style.display = "none";
    imgSixR.style.display = "none";
    imgSevenR.style.display = "none";
    imgEightR.style.display = "none";
    imgNineR.style.display = "block";
    startVideoLeft("number_nine_right");
  } else if (imageId === "letter-A-sign") {
    imgAR.style.display = "block";
    imgBR.style.display = "none";
    imgCR.style.display = "none";
    imgDR.style.display = "none";
    imgPR.style.display = "none";
    startVideoLeft("letter_A_right");
  }
  else if (imageId === "letter-B-sign") {
    imgBR.style.display = "block";
    imgAR.style.display = "none";
    imgCR.style.display = "none";
    imgDR.style.display = "none";
    imgPR.style.display = "none";
    startVideoLeft("letter_B_right");
  }

  else if (imageId === "letter-C-sign") {
    imgBR.style.display = "none";
    imgAR.style.display = "none";
    imgCR.style.display = "block";
    imgDR.style.display = "none";
    imgPR.style.display = "none";
    startVideoLeft("letter_C_right");
  }

  else if (imageId === "letter-D-sign") {
    imgBR.style.display = "none";
    imgAR.style.display = "none";
    imgCR.style.display = "none";
    imgDR.style.display = "block";
    imgPR.style.display = "none";
    startVideoLeft("letter_D_right");
  }

  else if (imageId === "letter-P-sign") {
    imgBR.style.display = "none";
    imgAR.style.display = "none";
    imgCR.style.display = "none";
    imgDR.style.display = "none";
    imgPR.style.display = "block";
    startVideoLeft("letter_P_right");
  }

  else if (imageId === "letter-A-sign-left") {
    imgAL.style.display = "block";
    imgBL.style.display = "none";
    imgCL.style.display = "none";
    imgDL.style.display = "none";
    imgPL.style.display = "none";
    startVideoLeft("letter_A_left");
  }

  else if (imageId === "letter-B-sign-left") {
    imgAL.style.display = "none";
    imgBL.style.display = "block";
    imgCL.style.display = "none";
    imgDL.style.display = "none";
    imgPL.style.display = "none";
    startVideoLeft("letter_B_left");
  }
  else if (imageId === "letter-C-sign-left") {
    imgAL.style.display = "none";
    imgBL.style.display = "none";
    imgCL.style.display= "block";
    imgDL.style.display = "none";
    imgPL.style.display = "none";
    startVideoLeft("letter_C_left");
  }
  else if (imageId === "letter-D-sign-left") {
    imgAL.style.display = "none";
    imgBL.style.display = "none";
    imgCL.style.display= "none";
    imgDL.style.display = "block";
    imgPL.style.display = "none";
    startVideoLeft("letter_D_left");
  }

  else if (imageId === "letter-P-sign-left") {
    imgAL.style.display = "none";
    imgBL.style.display = "none";
    imgCL.style.display= "none";
    imgDL.style.display = "none";
    imgPL.style.display = "block";
    startVideoLeft("letter_P_left");
  }

  else if (imageId === "House-sign") {
    imgH.style.display = "block";
    startVideoLeft("House-sign");
  }

  else if (imageId === "Number-six-sign-wales") {
    img6W.style.display = "block";
    startVideoLeft("number_six_right_wales");
  }

  else if (imageId === "Number-six-sign-wales-left") {
    img6WL.style.display = "block";
    startVideoLeft("number_six_left_wales");
  }


}