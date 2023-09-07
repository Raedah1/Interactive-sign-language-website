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

