import cv2
import mediapipe as mp
import math

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# Initialize the hand tracking module
hands = mp_hands.Hands(
    max_num_hands=1,  # Only track one hand
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)


# Adapted from: "Real-time Gesture Recognition using Google's MediaPipe Hands: Add your own gestures tutorial"
# Author: Vaibhav Mudgal
# Medium article: https://mudgalvaibhav.medium.com/real-time-gesture-recognition-using-googles-mediapipe-hands-add-your-own-gestures-tutorial-1-dd7f14169c19

# Code: Is for detecting the orientation of the hand by calculating the slop
# I used this code as function, to call it in the recognition function as condition


def detect_orientation(hand_landmarks_value):

    # Get the x and y coordinates of Landmark 0 and Landmark 9
    x0, y0 = hand_landmarks_value[0].x, hand_landmarks_value[0].y
    x9, y9 = hand_landmarks_value[9].x, hand_landmarks_value[9].y

    # Calculate the slope of the line joining Landmark 0 and Landmark 9
    if abs(x9 - x0) < 0.05:  # avoid division by zero
        m = 1000000000
    else:
        m = abs((y9 - y0) / (x9 - x0))

    # Determine the orientation based on the slope and the relative positions of the landmarks
    if 0 <= m <= 1:
        if x9 > x0:
            return "Right"
        else:
            return "Left"
    elif m > 1:
        if y9 < y0:
            return "Up"
        else:
            return "Down"
    else:
        return "Undefined"


#I used the same concept to calculate ,however here to calculate the orientation of specific finger

def detect_orientation_of_the_index(hand_landmarks):
    # Get the x and y coordinates of Landmark 0 and Landmark 9
    x5, y5 = hand_landmarks[5].x, hand_landmarks[5].y
    x8, y8 = hand_landmarks[8].x, hand_landmarks[8].y

    # Calculate the slope of the line joining Landmark 0 and Landmark 9
    if abs(x8 - x5) < 0.05:  # avoid division by zero
        m = 1000000000
    else:
        m = abs((y8 - y5) / (x8 - x5))

    # Determine the orientation based on the slope and the relative positions of the landmarks
    if 0<= m <= 1:
        if x8 > x5:
            return "Right"
        else:
            return "Left"
    elif m > 1:
        if y8 < y5:
            return "Up"
        else:
            return "Down"
    else:
        return "Undefined"


def detect_orientation_of_the_middle(hand_landmarks):
    # Get the x and y coordinates of Landmark 0 and Landmark 9
    x9, y9 = hand_landmarks[9].x, hand_landmarks[9].y
    x12, y12 = hand_landmarks[12].x, hand_landmarks[12].y

    # Calculate the slope of the line joining Landmark 0 and Landmark 9
    if abs(x12 - x9) < 0.05:  # avoid division by zero
        m = 1000000000
    else:
        m = abs((y12 - y9) / (x12 - x9))
    # Determine the orientation based on the slope and the relative positions of the landmarks
    if 0<= m <= 1:
        if x12 > x9:
            return "Right"
        else:
            return "Left"
    elif m > 1:
        if y12 < y9:
            return "Up"
        else:
            return "Down"
    else:
        return "Undefined"


def detect_orientation_of_the_pinky(hand_landmarks):
    # Get the x and y coordinates of Landmark 0 and Landmark 9
    x17, y17 = hand_landmarks[17].x, hand_landmarks[17].y
    x20, y20 = hand_landmarks[20].x, hand_landmarks[20].y

    # Calculate the slope of the line joining Landmark 0 and Landmark 9
    if abs(x20 - x17) < 0.05:  # avoid division by zero
        m = 1000000000
    else:
        m = abs((y20 - y17) / (x20 - x17))

    # Determine the orientation based on the slope and the relative positions of the landmarks
    if 0<= m <= 1:
        if x20 > x17:
            return "Right"
        else:
            return "Left"
    elif m > 1:
        if y20 < y17:
            return "Up"
        else:
            return "Down"
    else:
        return "Undefined"


def findDistance(lm1, lm2):
    x1, y1 = lm1.x, lm1.y
    x2, y2 = lm2.x, lm2.y
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance