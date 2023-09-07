from Application.NumberLesson.Number_left import *


def show1L():
    return recognise_gesture_index_orientation(recognise_number_one_left, "Number 1")

def show2L():
    return recognise_gesture_middle_orientation(recognise_number_two_left, "Number 2")

def show3L():
    return recognise_number_generator(recognise_number_three_left,"Number 3")

def show4L():
    return recognise_pinky_orientation(recognise_number_four_left, "Number 4")

def show5L():
    return recognise_gesture_index_orientation(recognise_number_five_left, "Number 5")

def show6L():
    return recognise_number_generator(recognise_number_six_left, "Number 6")


def show7L():
    return recognise_number_generator(recognise_number_seven_left, "Number 7")


def show8L():
    return recognise_number_generator(recognise_number_eight_left, "Number 8")


def show9L():
    return recognise_number_generator(recognise_number_nine_left, "Number 9")

def show6WL():
    return recognise_number_generator(detect_number_six_left_wales, "Number 6")

