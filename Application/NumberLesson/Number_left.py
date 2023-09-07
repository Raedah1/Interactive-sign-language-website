from Application.NumberLesson.Functions import *
finger_tips = [8, 12, 16, 20]
thumb_tip = 4
index_tip = 8
two_finger_down = [16, 20]
middle_tip = 12
three_finger = [8, 12, 16]
pinky_tip = 20

# The implementation  was inspired from MediaPipe Hand Landmark Detection
# Documentation: https://developers.google.com/mediapipe/solutions/vision/hand_landmarker


def recognise_number_generator(detect_number_func, message):
    global cap
    cap = cv2.VideoCapture(0)
    while True:
        if cap is not None:
            ret, frame = cap.read()
            if not ret:
                print("Error: Could not read frame")
                continue
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame")
            continue
        # Flip on horizontal
        frame = cv2.flip(frame, 1)
        #set Flags
        frame.flags.writeable = False
        # convert the
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        #Detection of the hand
        results = hands.process(frame)
        frame.flags.writeable = True
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        if results.multi_hand_landmarks:
            for hand_landmarks, hand in zip(results.multi_hand_landmarks, results.multi_handedness):
                if hand.classification[0].label != "Left":
                    box_width = 250
                    box_height = 50
                    box_pos_x = 350
                    box_pos_y = 10
                    cv2.rectangle(frame, (box_pos_x, box_pos_y), (box_pos_x + box_width, box_pos_y + box_height),
                                  (255, 255, 255), cv2.FILLED)
                    cv2.putText(frame, "Wrong hand X", (360, 45), cv2.FONT_HERSHEY_SIMPLEX, 1,
                                (0, 0, 255), 2)
                    continue
                landmarks = hand_landmarks.landmark
                orientation = detect_orientation(hand_landmarks.landmark)
                gesture = detect_number_func(frame, landmarks, orientation)
                if gesture is not None:
                    box_width = 200
                    box_height = 50
                    box_pos_x = 20
                    box_pos_y = 10
                    cv2.rectangle(frame, (box_pos_x, box_pos_y), (box_pos_x + box_width, box_pos_y + box_height),
                                  (255, 255, 255), cv2.FILLED)
                    cv2.putText(frame, message, (30, 45), cv2.FONT_HERSHEY_SIMPLEX, 1,
                                (0, 0, 0), 2)
                    box_width = 200
                    box_height = 50
                    box_pos_x2 = 20
                    box_pos_y2 = 80
                    cv2.rectangle(frame, (box_pos_x2, box_pos_y2), (box_pos_x2 + box_width, box_pos_y2 + box_height),
                                  (255, 255, 255), cv2.FILLED)
                    cv2.putText(frame, "Correct !", (30, 115), cv2.FONT_HERSHEY_SIMPLEX, 1,
                                (0, 255, 0), 2)



        frame = cv2.imencode('.jpg', frame)[1].tobytes()
        yield b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n'


def recognise_gesture_index_orientation(gesture, message):
    global cap
    # Initialize the camera capture
    cap = cv2.VideoCapture(0)

    while True:
        # Read a frame from the camera
        if cap is not None:
            # Read a frame from the camera
            ret, frame = cap.read()
            if not ret:
                print("Error: Could not read frame")
                continue

        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame")
            continue
        frame = cv2.flip(frame, 1)

        # set Flags
        frame.flags.writeable = False

        # Convert the frame to RGB for processing with MediaPipe
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process the frame with MediaPipe to detect hands
        results = hands.process(frame)
        # Convert the frame back to BGR for displaying
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        frame.flags.writeable = True

        # If hands are detected, get the landmarks and draw them on the frame
        if results.multi_hand_landmarks:
            for hand_landmarks, hand in zip(results.multi_hand_landmarks, results.multi_handedness):
                # Only process the left hand
                if hand.classification[0].label != "Left":
                    box_width = 250
                    box_height = 50
                    box_pos_x = 350
                    box_pos_y = 10
                    cv2.rectangle(frame, (box_pos_x, box_pos_y), (box_pos_x + box_width, box_pos_y + box_height),
                                  (255, 255, 255), cv2.FILLED)
                    cv2.putText(frame, "Wrong hand X", (360, 45), cv2.FONT_HERSHEY_SIMPLEX, 1,
                                (0, 0, 255), 2)
                    continue

                landmarks = hand_landmarks.landmark

                # Detect the orientation of the hand
                orientation = detect_orientation(hand_landmarks.landmark)
                index_orientation = detect_orientation_of_the_index(hand_landmarks.landmark)

                if gesture(frame, landmarks, orientation, index_orientation):
                    box_width = 200
                    box_height = 50
                    box_pos_x = 20
                    box_pos_y = 10
                    cv2.rectangle(frame, (box_pos_x, box_pos_y), (box_pos_x + box_width, box_pos_y + box_height),
                                  (255, 255, 255), cv2.FILLED)
                    cv2.putText(frame, message, (box_pos_x + 10, box_pos_y + 35), cv2.FONT_HERSHEY_SIMPLEX, 1,
                                (0, 0, 0), 2)
                    box_width = 200
                    box_height = 50
                    box_pos_x2 = 20
                    box_pos_y2 = 80
                    cv2.rectangle(frame, (box_pos_x2, box_pos_y2), (box_pos_x2 + box_width, box_pos_y2 + box_height),
                                  (255, 255, 255), cv2.FILLED)
                    cv2.putText(frame, "Correct !", (box_pos_x2 + 10, box_pos_y2 + 35), cv2.FONT_HERSHEY_SIMPLEX, 1,
                                (0, 255, 0), 2)

        frame = cv2.imencode('.jpg', frame)[1].tobytes()
        #send frame to browswer template template
        yield b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n'


def recognise_gesture_middle_orientation(gesture, message):
    global cap
    # Initialize the camera capture
    cap = cv2.VideoCapture(0)

    while True:
        # Read a frame from the camera
        if cap is not None:
            # Read a frame from the camera
            ret, frame = cap.read()
            if not ret:
                print("Error: Could not read frame")
                continue

        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame")
            continue
        frame = cv2.flip(frame, 1)

        # set Flags
        frame.flags.writeable = False

        # Convert the frame to RGB for processing with MediaPipe
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process the frame with MediaPipe to detect hands
        results = hands.process(frame)
        frame.flags.writeable = True
        # Convert the frame back to BGR for displaying
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        # If hands are detected, get the landmarks and draw them on the frame
        if results.multi_hand_landmarks:
            for hand_landmarks, hand in zip(results.multi_hand_landmarks, results.multi_handedness):
                # Only process the left hand
                if hand.classification[0].label != "Left":
                    box_width = 250
                    box_height = 50
                    box_pos_x = 350
                    box_pos_y = 10
                    cv2.rectangle(frame, (box_pos_x, box_pos_y), (box_pos_x + box_width, box_pos_y + box_height),
                                  (255, 255, 255), cv2.FILLED)
                    cv2.putText(frame, "Wrong hand", (360, 45), cv2.FONT_HERSHEY_SIMPLEX, 1,
                                (0, 0, 255), 2)
                    continue

                landmarks = hand_landmarks.landmark

                # Detect the orientation of the hand
                orientation = detect_orientation(hand_landmarks.landmark)
                middle_orientation = detect_orientation_of_the_middle(hand_landmarks.landmark)

                if gesture(frame, landmarks, orientation, middle_orientation):
                    box_width = 200
                    box_height = 50
                    box_pos_x = 20
                    box_pos_y = 10
                    cv2.rectangle(frame, (box_pos_x, box_pos_y), (box_pos_x + box_width, box_pos_y + box_height),
                                  (255, 255, 255), cv2.FILLED)
                    cv2.putText(frame, message, (30, 45), cv2.FONT_HERSHEY_SIMPLEX, 1,
                                (0, 0, 0), 2)
                    box_width = 200
                    box_height = 50
                    box_pos_x2 = 20
                    box_pos_y2 = 80
                    cv2.rectangle(frame, (box_pos_x2, box_pos_y2), (box_pos_x2 + box_width, box_pos_y2 + box_height),
                                  (255, 255, 255), cv2.FILLED)
                    cv2.putText(frame, "Correct !", (30, 115), cv2.FONT_HERSHEY_SIMPLEX, 1,
                                (0, 255, 0), 2)

        # cv2.imshow('MediaPipe Hands', frame)
        frame = cv2.imencode('.jpg', frame)[1].tobytes()
        yield b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n'


def recognise_pinky_orientation(gesture, message):
    global cap
    # Initialize the camera capture
    cap = cv2.VideoCapture(0)

    while True:
        # Read a frame from the camera
        if cap is not None:
            # Read a frame from the camera
            ret, frame = cap.read()
            if not ret:
                print("Error: Could not read frame")
                continue

        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame")
            continue
        frame = cv2.flip(frame, 1)

        # set Flags
        frame.flags.writeable = False

        # Convert the frame to RGB for processing with MediaPipe
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process the frame with MediaPipe to detect hands
        results = hands.process(frame)
        frame.flags.writeable = True
        # Convert the frame back to BGR for displaying
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        # If hands are detected, get the landmarks and draw them on the frame
        if results.multi_hand_landmarks:
            for hand_landmarks, hand in zip(results.multi_hand_landmarks, results.multi_handedness):
                # Only process the left hand
                if hand.classification[0].label != "Left":
                    box_width = 250
                    box_height = 50
                    box_pos_x = 350
                    box_pos_y = 10
                    cv2.rectangle(frame, (box_pos_x, box_pos_y), (box_pos_x + box_width, box_pos_y + box_height),
                                  (255, 255, 255), cv2.FILLED)
                    cv2.putText(frame, "Wrong hand", (360, 45), cv2.FONT_HERSHEY_SIMPLEX, 1,
                                (0, 0, 255), 2)
                    continue

                landmarks = hand_landmarks.landmark

                # Detect the orientation of the hand
                orientation = detect_orientation(hand_landmarks.landmark)
                pinky_orientation = detect_orientation_of_the_pinky(hand_landmarks.landmark)

                if gesture(frame, landmarks, orientation, pinky_orientation):
                    box_width = 200
                    box_height = 50
                    box_pos_x = 20
                    box_pos_y = 10
                    cv2.rectangle(frame, (box_pos_x, box_pos_y), (box_pos_x + box_width, box_pos_y + box_height),
                                  (255, 255, 255), cv2.FILLED)
                    cv2.putText(frame, message, (30, 45), cv2.FONT_HERSHEY_SIMPLEX, 1,
                                (0, 0, 0), 2)
                    box_width = 200
                    box_height = 50
                    box_pos_x2 = 20
                    box_pos_y2 = 80
                    cv2.rectangle(frame, (box_pos_x2, box_pos_y2), (box_pos_x2 + box_width, box_pos_y2 + box_height),
                                  (255, 255, 255), cv2.FILLED)
                    cv2.putText(frame, "Correct !", (30, 115), cv2.FONT_HERSHEY_SIMPLEX, 1,
                                (0, 255, 0), 2)

        # cv2.imshow('MediaPipe Hands', frame)
        frame = cv2.imencode('.jpg', frame)[1].tobytes()
        yield b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n'


"""Sign language detection code adapted from:
Repository: https://github.com/datamagic2020/sign-language-detection
Author: datamagic2020
I was inspired by the idea of recognising of the finger are open or not their code "landmarks[tip].y < landmarks[tip - 1].y < landmarks[tip - 2].y" 
However, due to some limitation like when the finger is bend or in other word half closed the condition for open finger is "landmarks[tip].y < landmarks[tip - 1].y"  """


def recognise_number_one_left(image, landmarks, orientation, orientation_finger):
    finger_fold_status = []
    for tip in three_finger:
        if landmarks[tip].y > landmarks[tip - 3].y:
            finger_fold_status.append(True)
        else:
            finger_fold_status.append(False)

    if orientation == "Up":
        if orientation_finger == "Up":
            if landmarks[index_tip].y < landmarks[index_tip - 1].y:
                if landmarks[thumb_tip].x < landmarks[pinky_tip].x:
                    if landmarks[thumb_tip].x > landmarks[thumb_tip - 1].x:
                        if all(finger_fold_status):
                            return "Number one"
    return None


def recognise_number_two_left(image, landmarks, orientation, orientation_middle):
    finger_fold_status = []

    for tip in two_finger_down:
        if landmarks[tip].y > landmarks[tip - 3].y:
            finger_fold_status.append(True)
        else:
            finger_fold_status.append(False)

    if orientation == "Up":
        if orientation_middle == "Up":
            if landmarks[middle_tip].y < landmarks[middle_tip - 1].y < landmarks[middle_tip - 2].y:
                if landmarks[index_tip].y < landmarks[index_tip - 1].y < landmarks[index_tip - 2].y:
                    if landmarks[thumb_tip].x < landmarks[pinky_tip].x:
                        if landmarks[thumb_tip].x > landmarks[thumb_tip - 1].x:
                            if all(finger_fold_status):
                                return "Number two"
    return


def recognise_number_three_left(image, landmarks, orientation):
    finger_straight_status = []

    for tip in three_finger:
        if landmarks[tip].y < landmarks[tip - 1].y < landmarks[tip - 2].y:
            finger_straight_status.append(True)
        else:
            finger_straight_status.append(False)

    if orientation == "Up":
        if landmarks[pinky_tip].y > landmarks[pinky_tip - 1].y:
            if landmarks[thumb_tip].x < landmarks[pinky_tip].x:
                if all(finger_straight_status):
                    distance = findDistance(landmarks[4], landmarks[20])
                    if distance <= 0.04:
                        return "Number Three"
    return None


def recognise_number_four_left(image, landmarks, orientation, orientation_pinky):
    finger_straight_status = []
    for tip in finger_tips:
        if landmarks[tip].y < landmarks[tip - 2].y:
            finger_straight_status.append(True)
        else:
            finger_straight_status.append(False)

    if orientation == "Up":
        if orientation_pinky == "Up":
            if landmarks[thumb_tip - 3].x < landmarks[thumb_tip].x < landmarks[pinky_tip].x:
                if all(finger_straight_status):
                    return "Number Four"
    return None


def recognise_number_five_left(image, landmarks, orientation, orientation_index):
    finger_straight_status = []
    for tip in finger_tips:
        if landmarks[tip].y < landmarks[tip - 2].y:
            finger_straight_status.append(True)
        else:
            finger_straight_status.append(False)

    if orientation == "Up":
        if orientation_index == "Up":
            if landmarks[thumb_tip].x < landmarks[thumb_tip - 3].x:
                if landmarks[index_tip].x < landmarks[pinky_tip].x:
                    if all(finger_straight_status):
                        return "Number Five"
    return None


def recognise_number_six_left(image, landmarks_value, orientation_value):
    finger_fold_status = []
    for tip in finger_tips:
        if landmarks_value[tip].x < landmarks_value[tip - 2].x:
            finger_fold_status.append(True)
        else:
            finger_fold_status.append(False)

    if orientation_value == "Right":
        if landmarks_value[thumb_tip - 2].y > landmarks_value[thumb_tip].y > landmarks_value[thumb_tip - 1].y:
            if all(finger_fold_status):
                return "Number Six"
    return


def recognise_number_seven_left(image, landmarks_value, orientation_value):
    finger_fold_status = []
    for tip in two_finger_down :
        if landmarks_value[tip].x < landmarks_value[tip - 3].x:
            finger_fold_status.append(True)
        else:
            finger_fold_status.append(False)

    if orientation_value == "Right":
        if landmarks_value[index_tip].x > landmarks_value[index_tip - 1].x:
            if landmarks_value[thumb_tip].y < landmarks_value[thumb_tip - 1].y < landmarks_value[thumb_tip - 2].y:
                if all(finger_fold_status):
                    return "Number seven"
    return None


def recognise_number_eight_left(image, landmarks_value, orientation_value):
    finger_fold_status = []
    for tip in two_finger_down:
        if landmarks_value[tip].x < landmarks_value[tip - 3].x:
            finger_fold_status.append(True)
        else:
            finger_fold_status.append(False)
    if orientation_value == "Right":
        if landmarks_value[index_tip].x > landmarks_value[index_tip - 1].x:
            if landmarks_value[middle_tip].x > landmarks_value[middle_tip - 1].x > landmarks_value[middle_tip - 2].x:
                if landmarks_value[thumb_tip].y < landmarks_value[thumb_tip - 1].y < landmarks_value[thumb_tip - 2].y:
                    if all(finger_fold_status):
                        return "Number Eight"
    return None


def recognise_number_nine_left(image, landmarks_value, orientation_value):
    finger_straight_status = []
    for tip in three_finger:
        if landmarks_value[tip].x > landmarks_value[tip - 2].x:
            finger_straight_status.append(True)
        else:
            finger_straight_status.append(False)

    if orientation_value == "Right":
        if landmarks_value[pinky_tip].x < landmarks_value[pinky_tip - 2].x:
            if landmarks_value[thumb_tip].y < landmarks_value[thumb_tip - 1].y < landmarks_value[thumb_tip - 2].y:
                if all(finger_straight_status):
                    return "Number Nine"
    return None

def detect_number_six_left_wales(image, landmarks,orientation):
    finger_fold_status = []
    for tip in three_finger:
        if landmarks[tip].x < landmarks[tip - 2].x:
            finger_fold_status.append(True)
        else:
            finger_fold_status.append(False)

    if orientation == "Right":
        if landmarks[pinky_tip].x > landmarks[pinky_tip - 1].x > landmarks[pinky_tip - 2].x:
            if landmarks[thumb_tip].y > landmarks[thumb_tip- 2].y:
                if all(finger_fold_status):
                    return "Number six "
    return None
