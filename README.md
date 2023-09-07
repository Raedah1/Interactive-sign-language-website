# Interactive-sign-language-website
A web application platform for learning and practicing British sign language through incorporating sign gesture detection. The purpose of the website is to provide instant and real-time feedback on their hand signing and to give the users the opportunity to actively practice their signing skills in a more fun and engaging way without relying on others. This project aims to increase the accessibility of sign language learning to a border audience. 

# 1.1 Project Scope 
The web application will offer three lessons for learners, namely "Numbers", "Fingerspelling for Alphabet" and "Basic Vocabulary". It will only cover the static signs not the dynamic signs for instance, the letter "J" will not be included in the "Fingerselling for Alphabet" as it is a dynamic sign. Additionally, it supports both right-handed and left-handed learners, as it is important to specify the dominant hand. 
# 1.2 Use Cases UML Diagram 
The use cases diagram shows the different actions and use cases the user can do in the system. It helps to visualize the flow of interaction between the user and the system. Please refer to Figure 1.

<img width="417" alt="UML" src="https://github.com/Raedah1/Interactive-sign-language-website/assets/92187909/738a8dac-220f-4c6d-9026-0f38c863d6e1">

# 1.3 Hand Signing Recognition Model Design 
The design of the hand sign recognition models consists of  a set of interconnected steps and functions that work together to achieve a specific task, which is to accurately recognize the signs and return correct and reliable feedback to the users. For a graphical illustration, please refer to Figure 2.

<img width="382" alt="Model" src="https://github.com/Raedah1/Interactive-sign-language-website/assets/92187909/cb846ef7-f55e-487d-bef3-8d13784baed9">


The model begins when the user performs a sign, and the camera captures the video feed with the help of the “OpenCV'' library. Then it pre-processes the image frame to ensure that data inputs are in their correct format, by converting the frame from the default BGR to RGB. This is an important step as it is the required format for the “Mediapipe” framework that is used for hand tracking and detection.

Another important step in image pre-processing is flipping the camera feed to mirror 
the user's hand, to prevent confusion and frustration for the users, as the signs for right-handed and left-handed learners are different from each other. To ensure security “Writeflag” is set to “False” to prevent the data from being modified and avoid the unexpected change that might occur during the image processing and once the image processing is complete the “Writeflag” is set back to “True” .
For hand detection, “Mediapipe” library framework is used to track and detect the hands from the video feed. Additionally, it is used for hand landmark extraction, which is essential for customising the sign recognition function.

The sign recognition functions is based on utilising the mathematical logic with the 
extracted landmarks to recognize the different signs, there are several factors that 
have been considered when designing the recognition functions, which are as follows: 
- Number of hands in the frame.
- Handness(Left or Right). 
- Orientation of the hand. 
- Orientation of specific fingers in the hand. 
- The palm or the back of the hand. 
- Fingers are closed or open. 
- Distance between fingers of the same or opposite hand. 

All of these factors have an impact on developing an accurate sign recognition function, they will be defined as a condition, and if the recognised sign met the condition a feedback will be displayed. It is worth noting not all the factors will be utilized in every recognition function. Therefore, some signs might only need two to three conditions for them to be recognized. 

The last step, after the sign gesture recognition step, is providing feedback to the user based on their signing performance. For example, if the user did the signing for “Letter A” correctly it will display “Letter A” and “Correct”, which indicates a correct gesture has been performed. In addition, if the user is doing the sign with the wrong hand a “Wrong hand X” feedback will be displayed on the screen. 

Integrating the hand signing recognition model into the web application is what will 
distinguish it from other BSL teaching websites. Hence, the successful development for 
this model is a high priority for the success of the web application.

# 1.4 Hand Signing Recognition Model Implementation 

Two main libraries are used for developing the recognition algorithm, which is "OpenCV" and "Mediapip". OpenCV is used for capturing webcam video and image pre-processing, while the latter is used for tracking, detecting, and drawing the landmarks of the hand. Then the math logic is used on the extracted hand landmarks to customise a recognition function for each sign. 

The Mediapipe framework helps detect 21 landmarks in the hand, as it is shown in Figure 3. The landmarks are going to be used to detect the orientation of the hand, back, and palm of the hand. Additionally, the distance between two fingers of the same hand or for the opposite hand. 

<img width="487" alt="HandLandmarks" src="https://github.com/Raedah1/Interactive-sign-language-website/assets/92187909/6af73817-131a-45da-910a-77ea50fdd7f4">


# 2.1 The Digits signs recognition Function for the Left-handed 
To accurately recognize the digits signs it is important to consider that they are formed using one hand only as illustrated in Figure 18.0 .Consequently, when initialising the hand tracking module, it is necessary to indicate that only one hand should be tracked. This is achieved by setting the max_num_hands attribute to one “mp_hands.Hands(max_num_hands = 1)”. Moreover, as previously stated the system supports both left-right-handed users. Therefore, it is crucial to specify which 
hand should be detected, based on the user choice. Achieving this task is through specifying the “hand.classification [0].label != “Left” “ this ensure only the 
landmarks of the left hand are detecting and if it was the right hand landmark , a “continue” statement is executed and it will skips the current detection and will move on the next hand.To see the full code refer to GitHub repository in the Exhibition H of 
the appendix refer file path “Application /NumberLesson/Number_left.py”. 

Once the hand was successfully detected and classified in the video frame. The next step is landmark extraction and storing it in a new variable to be used in signs 
recognition functions.It is done through the ".landmark” attribute of “hand_landmarks“ object, where it has a list of the (x,y,z) coordinates for each 
landmark that were detected. As the project will focus on the static signs , only the (x,y) coordinates will be used for further processing and analysing and the (z) will be ignored.The extracted landmark can be used to determine the orientation of the hand, as well as the position of the fingers, whether they are open or closed , and whether the palm of or back of the hand is facing the camera. These critical features will be 
stated into the sign recognition functions.

# 2.2 Orientation of the Hand 
Detecting the orientation of the hand is an essential step for recognizing the digits signs,as it will make the process of recognising the signs more accurate. The idea of the orientation function “def detect_orientation(hand_landmarks_value)” is based on the work of Mudgal(2021), as described in their tutorial on real-time gesture recognition using Google’s MediaPipe Hands.By taking a list of hand landmarks , for either the right or the left hand and return the orientation based on the position of the wrist[0] and the base of middle finger [9] landmarks. 

The function extracts the x and y coordinate of the wrist[0] and the base of the middle finger landmarks[9].Then it calculates the slope between these two landmarks [0] and [9]. If the result of the calculation is between 0 and 1, and the [9] landmark is greater than [0] landmark , the hand is pointing to the “Right” orientation. In contrast, if the [9] landmark is less than [0] landmark, the hand is pointed to the “Left” .For butter 
visualisation refer to Figure 4. 

<img width="512" alt="Left_or_right" src="https://github.com/Raedah1/Interactive-sign-language-website/assets/92187909/f610530c-c70e-4b23-91fb-cbf26bbc484f">

On other hand, if the calculation results of the slope is greater than 1 and the [9] landmark is less than [0] landmark the hand is pointing to the “Up” direction. While if the [9] is greater than [0] landmark the orientation of the hand is “Down”, for a graphical representation, please see Figure 20.0. To view the full code , please refer to “Application/Number Lesson/Number_Left” or (Section B) in the Appendix If the slope is very close to zero , the function returns “Undefined”.

<img width="492" alt="Up_or_down" src="https://github.com/Raedah1/Interactive-sign-language-website/assets/92187909/b961ec5c-465a-4e9d-9858-b7d7f5f02736">

# 2.3 The finger is open or closed 
This determination is based on the comparison between the landmark for the tip of the finger, referred to as “landmark[tip]” with the second and third position 
of the tip in the same finger ”landmark[tip -1]” and “landmarks[tip - 2]”. In some cases, specifically for the thumb finger the comparison is between “landmark[tip]”with “[landmark[tip -3]”. For the signs that point “Up” the difference between the landmarks is observed along the Y-axis. In contrast, for signs pointing in the “Right” and “Left” direction, the difference occurs in the X-axis. The idea of this code was adapted from 
the work of datamagic2020s GitHub . 
As an example to detect “Number one” for left handed learner’s, first the orientation of the hand is “Up” and the index finger must be open while the rest of the fingers should be closed, please refer to Figure 21.0 for a visual illustration of the sign.To ensure that middle[12], ring[16], and pinky[20] are recognised as closed, the tip of these fingers in the Y-axis should be greater than the [tip - 3]see the snippet of the code in Figure 5.For the index finger if this condition “landmarks [index_tip].< landmarks[index_tip - 2]” is met , it indicates that the finger is extended(open).Then for the thumb finger this condition should be met “landmarks[thumb].x >landmarks[thumb-3].x”, to recognize it as closed.

<img width="235" alt="Up" src="https://github.com/Raedah1/Interactive-sign-language-website/assets/92187909/bc3dfe6f-3de8-4459-8ea0-9d1635598c7a">
