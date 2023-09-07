from flask import Flask, render_template, Response, request
from Application.NumberLesson.Number_detection_left import *
from Application.NumberLesson.Number_detection_right import *
from Application.LetterLesson.Letter_detection_right import *
from Application.LetterLesson.Letter_detection_left import *
from Application.RandomWord.RandomLesson import *

app = Flask(__name__)
cap = None

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/lessons")
def lessons():
    return render_template("lessons.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/RightLetterLesson")
def RightLetterLesson():
    return render_template("RightLetterLesson.html")

@app.route("/rightLesson")
def rightLesson():
    return render_template("rightLesson.html")

@app.route("/LeftOrRightNumber")
def LeftOrRightNumber():
    return render_template("LeftOrRightNumber.html")

@app.route("/LeftOrRightLetter")
def LeftOrRightLetter():
    return render_template("LeftOrRightLetter.html")

@app.route("/LeftLetterLesson")
def LeftLetterLesson():
    return render_template("LeftLetterLesson.html")

@app.route("/random")
def random():
    return render_template("random.html")

@app.route("/RightNumberW")
def RightNumberW():
    return render_template("RightNumberW.html")

@app.route("/LeftNumberW")
def LeftNumberW():
    return render_template("LeftNumberW.html")

@app.route('/leftLesson')
def leftLesson():
    return render_template('leftLesson.html')


def get_video_feed(mode):
    video = {
        'number_one_left': show1L,
        'number_two_left': show2L,
        'number_three_left': show3L,
        'number_four_left': show4L,
        'number_five_left': show5L,
        'number_six_left': show6L,
        'number_seven_left': show7L,
        'number_eight_left': show8L,
        'number_nine_left': show9L,
        'number_one_right': show1R,
        'number_two_right': show2R,
        'number_three_right': show3R,
        'number_four_right': show4R,
        'number_five_right': show5R,
        'number_six_right': show6R,
        'number_seven_right': show7R,
        'number_eight_right': show8R,
        'number_nine_right': show9R,
        'letter_A_right': showAR,
        'letter_B_right': showBR,
        'letter_C_right': showCR,
        'letter_D_right': showDR,
        'letter_P_right': showPR,
        'letter_A_left': showAL,
        'letter_B_left': showBL,
        'letter_C_left': showCL,
        'letter_D_left': showDL,
        'letter_P_left': showPL,
        'House-sign': showH,
        'number_six_right_wales': show6W,
        'number_six_left_wales': show6WL,

    }
    return video.get(mode)


@app.route('/video_feed_left/<mode>')
def video_feed_left(mode):
    # Get the generator function based on the mode
    video = get_video_feed(mode)

    if video is None:
        return "Invalid"

    # Return the response with the video feed function
    return Response(video(), mimetype='multipart/x-mixed-replace; boundary=frame')
