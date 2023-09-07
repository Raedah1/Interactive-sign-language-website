from Application.LetterLesson.Functions_Letter import *

def recognising_letter_A_Left(frame, left_hand_landmarks, right_hand_landmarks):
    letter = None

    # calculate the distance between the index finger and thumb of the right hand
    if left_hand_landmarks and right_hand_landmarks:
        thumb_tip = right_hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
        index_finger_tip = left_hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
        distance = findDistance(thumb_tip, index_finger_tip)

        # If the distance is less than or equal to 0.03 and the index, middle, ring, and pinky fingers are opened, classify the hand gesture as the letter A
        if distance <= 0.03:
            left_landmarks = left_hand_landmarks.landmark
            right_landmarks = right_hand_landmarks.landmark
            finger_stright_status = []
            finger_folded_status = []
            for right_tip in finger_up:
                if right_landmarks[right_tip].y < right_landmarks[right_tip - 2].y:
                    finger_stright_status.append(True)
                else:
                    finger_stright_status.append(False)

            for left_tip in finger_down:
                if left_landmarks[left_tip].x < left_landmarks[left_tip - 2].x:
                    finger_folded_status.append(True)
                else:
                    finger_folded_status.append(False)

            if all(finger_stright_status):
                if all(finger_folded_status):
                    return " Letter A"

    return None

def recognising_letter_B_Left(frame, left_hand_landmarks, right_hand_landmarks):
    letter = None


    if left_hand_landmarks and right_hand_landmarks:
        left_index_tip = left_hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
        right_index_tip = right_hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
        index_distance = findDistance(left_index_tip, right_index_tip)

        # Calculate the distance between the middle fingertip of the left hand and the left hand.
        left_middle_tip = left_hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
        right_middle_tip = right_hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
        middle_distance = findDistance(left_middle_tip, right_middle_tip)

        # Calculate the distance between the ring fingertip of both hands
        left_ring_tip = left_hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP]
        right_ring_tip = right_hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP]
        ring_distance = findDistance(left_ring_tip, right_ring_tip)

        # Calculate the distance between the pinky fingertip of both hands
        left_pinky_tip = left_hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP]
        right_pinky_tip = right_hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP]
        pinky_distance = findDistance(left_pinky_tip, right_pinky_tip)

        # Calculate the distance between the thumb and the index finger in the left hand
        left_thumb_tip = left_hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
        left_index_tip = left_hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
        left_distance = findDistance(left_index_tip, left_thumb_tip)

        # Calculate the distance between the thumb and the index finger in the right hand
        right_thumb_tip = left_hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
        right_index_tip = left_hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
        right_distance = findDistance(right_index_tip, right_thumb_tip)

        # If the distance is less than or equal to 0.03, classify the hand gesture as the letter A
        if index_distance <= 0.08 and middle_distance <= 0.08 and ring_distance <= 0.08 and pinky_distance <= 0.10 and left_distance <=0.05 and right_distance <=0.05:
            return "Letter B"

    return None



def recognisign_letter_C_Left(frame,left_hand_landmarks):
    letter = None

    # calculate the distance between the left tip with the tip of the left index finger
    if left_hand_landmarks:
        left_thumb_tip = left_hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
        left_index_finger_tip = left_hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
        distance = findDistance(left_thumb_tip, left_index_finger_tip)

        left_landmarks = left_hand_landmarks.landmark
        finger_folded_status = []
        for left_tip in finger_down:
            if left_landmarks[left_tip].x > left_landmarks[left_tip - 3].x:
                finger_folded_status.append(True)
            else:
                finger_folded_status.append(False)


        if (0.09<= distance <=0.13):
            if all(finger_folded_status):
                return "Letter C"

    return None

def recognising_letter_D_Left(frame, left_hand_landmarks, right_hand_landmarks):
    letter = None

    if right_hand_landmarks and left_hand_landmarks :
        left_thumb_tip = left_hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
        left_index_finger_tip = left_hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
        right_index_tip = right_hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
        right_index_mcp = right_hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP]
        distance_1 = findDistance(left_index_finger_tip, right_index_tip)
        distance_2 = findDistance(left_thumb_tip, right_index_mcp)

        right_landmarks = right_hand_landmarks.landmark
        left_landmarks = left_hand_landmarks.landmark
        finger_folded_status = []
        for tip in finger_down:
            if left_landmarks[tip].x > left_landmarks[tip - 3].x:
                if right_landmarks[tip].x > right_landmarks[tip -3].x:
                    finger_folded_status.append(True)
            else:
                finger_folded_status.append(False)

        if distance_1 <=0.08 and distance_2 <= 0.12:
            if all(finger_folded_status):
                return "Letter D"
    return None

def recognising_letter_P_Left(frame, left_hand_landmarks, right_hand_landmarks):
    letter = None

    if right_hand_landmarks and left_hand_landmarks:
        left_thumb_tip = left_hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
        left_index_finger_tip = left_hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
        right_index_tip = right_hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
        distance_1 = findDistance(left_index_finger_tip, right_index_tip)
        distance_2 = findDistance(left_thumb_tip, right_index_tip)
        distance_3 = findDistance(left_thumb_tip, left_index_finger_tip)

        right_landmarks = right_hand_landmarks.landmark
        left_landmarks = left_hand_landmarks.landmark
        finger_folded_status = []
        for tip in finger_down:
            if left_landmarks[tip].x > left_landmarks[tip - 3].x:
                if right_landmarks[tip].x > right_landmarks[tip - 3].x:
                    finger_folded_status.append(True)
            else:
                finger_folded_status.append(False)

        if distance_1 <=0.10 and distance_2 <= 0.10 and distance_3 <= 0.04:
            if all(finger_folded_status):
                letter = "Letter P"
    return letter