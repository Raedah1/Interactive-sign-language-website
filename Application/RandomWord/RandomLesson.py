from Application.LetterLesson.Functions_Letter import *

def detect_House(frame, left_hand_landmarks, right_hand_landmarks):
    letter = None
    if left_hand_landmarks and right_hand_landmarks:
        right_index_tip = right_hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
        left_index_tip = left_hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
        right_middle_tip = right_hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
        left_middle_tip = left_hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
        right_ring_tip = right_hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP]
        left_ring_tip = left_hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP]
        right_pinky_tip = right_hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP]
        left_pinky_tip = left_hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP]
        right_thumb_tip = right_hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
        left_thumb_tip = left_hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
        right_wrist = right_hand_landmarks.landmark[mp_hands.HandLandmark.WRIST]
        left_wrist = left_hand_landmarks.landmark[mp_hands.HandLandmark.WRIST]

        distance1 = findDistance(left_index_tip, right_index_tip)
        distance2 = findDistance(left_middle_tip, left_middle_tip)
        distance3 = findDistance(left_ring_tip, right_ring_tip)
        distance4 = findDistance(left_pinky_tip, right_pinky_tip)
        distance5 = findDistance(right_thumb_tip, left_thumb_tip)
        distance6 = findDistance(left_wrist, right_wrist)

        if distance1 <= 0.06 and distance2 <= 0.02 and distance3 <= 0.04 and distance4 <= 0.08 and 0.04 <= distance5 <= 0.17:
            if 0.13 <= distance6 <= 0.34:
                return "House"
    return None


def showH():
    return recognising_letter(detect_House)
