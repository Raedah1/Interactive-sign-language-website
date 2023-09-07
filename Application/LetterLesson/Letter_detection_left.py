from Application.LetterLesson.Letter_left import *

def showAL():
    return recognising_letter(recognising_letter_A_Left)

def showBL():
    return recognising_letter(recognising_letter_B_Left)


def showCL():
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

        # Process the frame with MediaPipe to detect hands
        results = hands.process(frame)
        #frame.flags.writeable = True

        # Convert the frame back to BGR for displaying
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        # Detect the hand landmarks
        frame, left_hand_landmarks, right_hand_landmarks = detect_hand(frame)

        # Detect the letter
        letter_detected = recognisign_letter_C_Left(frame,left_hand_landmarks)

        # Display the letter on the frame
        if letter_detected is not None:
            box_width = 200
            box_height = 50
            box_pos_x = 20
            box_pos_y = 10
            cv2.rectangle(frame, (box_pos_x, box_pos_y), (box_pos_x + box_width, box_pos_y + box_height),
                          (255, 255, 255), cv2.FILLED)
            cv2.putText(frame, letter_detected, (box_pos_x + 10, box_pos_y + 35), cv2.FONT_HERSHEY_SIMPLEX, 1,
                        (0, 0, 0), 2)
            box_width = 200
            box_height = 50
            box_pos_x2 = 20
            box_pos_y2 = 80
            cv2.rectangle(frame, (box_pos_x2, box_pos_y2), (box_pos_x2 + box_width, box_pos_y2 + box_height),
                          (255, 255, 255), cv2.FILLED)
            cv2.putText(frame, "Correct !", (box_pos_x2 + 10, box_pos_y2 + 35), cv2.FONT_HERSHEY_SIMPLEX, 1,
                        (0, 255, 0), 2)
        frame.flags.writeable = True

        # Show the frame
        frame = cv2.imencode('.jpg', frame)[1].tobytes()
        yield b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n'




def showDL():
    return recognising_letter(recognising_letter_D_Left)

def showPL():
    return recognising_letter(recognising_letter_P_Left)