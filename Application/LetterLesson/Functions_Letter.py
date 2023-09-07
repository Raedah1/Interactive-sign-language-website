import cv2
import mediapipe as mp
import math

# Initialize the MediaPipe hands object
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# Initialize the MediaPipe drawing object
mp_drawing = mp.solutions.drawing_utils

# Define a function to calculate the distance between two landmarks


def findDistance(lm1, lm2):
    x1, y1 = lm1.x, lm1.y
    x2, y2 = lm2.x, lm2.y
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance


# Define a function to detect hands and return the frame and handedness label
def detect_hand(frame):
    # Convert the frame to RGB for processing with MediaPipe
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame with MediaPipe to detect hands
    results = hands.process(frame)

    # Convert the frame back to BGR for displaying
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    left_hand_landmarks = None
    right_hand_landmarks = None

    # If hands are detected, get the landmarks and draw them on the frame
    if results.multi_hand_landmarks:
        for hand_landmarks, hand in zip(results.multi_hand_landmarks, results.multi_handedness):
            # Get the handedness label (left or right)
            handedness_label = hand.classification[0].label
            # Store the landmarks for the left or right hand
            if handedness_label == "Left":
                left_hand_landmarks = hand_landmarks
            else:
                right_hand_landmarks = hand_landmarks

    return frame, left_hand_landmarks, right_hand_landmarks


finger_up = [mp_hands.HandLandmark.INDEX_FINGER_TIP, mp_hands.HandLandmark.MIDDLE_FINGER_TIP,
             mp_hands.HandLandmark.RING_FINGER_TIP, mp_hands.HandLandmark.PINKY_TIP]
finger_down = [mp_hands.HandLandmark.MIDDLE_FINGER_TIP,
             mp_hands.HandLandmark.RING_FINGER_TIP, mp_hands.HandLandmark.PINKY_TIP]


def recognising_letter(letter):
    global cap
    # Initialize the camera capture
    cap = cv2.VideoCapture(0)

    while True:
        # Read a frame from the camera
        if cap is not None:
            ret, frame = cap.read()
            if not ret:
                print("Error: Could not read frame")
                continue

        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame")
            continue
        frame = cv2.flip(frame, 1)

        # Set flags
        frame.flags.writeable = False

        # Convert the frame to RGB for processing with MediaPipe
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = hands.process(frame)


        # Convert the frame back to BGR for displaying
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        # Detect the hand landmarks
        frame, left_hand_landmarks, right_hand_landmarks = detect_hand(frame)

        # Detect the letter
        letter_detected = letter(frame, left_hand_landmarks, right_hand_landmarks)


        # Display the letter on the frame
        if letter_detected is not None:
            box_width = 200
            box_height = 50
            box_pos_x = 20
            box_pos_y = 10
            cv2.rectangle(frame, (box_pos_x, box_pos_y), (box_pos_x + box_width, box_pos_y + box_height),
                          (255, 255, 255), cv2.FILLED)
            cv2.putText(frame, letter_detected, (30, 45), cv2.FONT_HERSHEY_SIMPLEX, 1,
                        (0, 0, 0), 2)
            box_width = 200
            box_height = 50
            box_pos_x2 = 20
            box_pos_y2 = 80
            cv2.rectangle(frame, (box_pos_x2, box_pos_y2), (box_pos_x2 + box_width, box_pos_y2 + box_height),
                          (255, 255, 255), cv2.FILLED)
            cv2.putText(frame, "Correct !", (30, 115), cv2.FONT_HERSHEY_SIMPLEX, 1,
                        (0, 255, 0), 2)

            frame.flags.writeable = True

        frame = cv2.imencode('.jpg', frame)[1].tobytes()
        yield b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n'
