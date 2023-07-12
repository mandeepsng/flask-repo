from flask import Flask, render_template
import pyautogui
import random
import time


app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html", title="Hello")


@app.route('/demo')
def demo():
    random_time = random.randint(1, 5)

    # create a time delay using the sleep()
    # method
    time.sleep(random_time)

    # Take the screenshot using screenshot()
    # method
    myScreenshot = pyautogui.screenshot()

    # Save the screenshot shot using current
    # time as file name.
    file_name = str(time.time())+".png"
    myScreenshot.save(file_name)