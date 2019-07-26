from flask import Flask, request, render_template, redirect,url_for
import os
from flask_socketio import SocketIO, send, emit
import RPi.GPIO as GPIO
from threading import Thread
import camera
from time import sleep

CONFIG = {
    count: 1,
    date: True,
    currentPic: None
}

GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD)
app = Flask(__name__)
socket = SocketIO(app)
buttonPin= 40
GPIO.setup(buttonPin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
def buttonsmh():
    while camera.not_captured:
        buttonState = GPIO.input(buttonPin)
        if buttonState and camera.previewing:
            camera.capture()
            socket.emit("redirect", camera.capture())
            camera.not_captured = False
@app.route("/")
def anasayfa():
    camera.not_captured = True
    but = Thread(target = buttonsmh)
    but.start()
    return render_template("index.html")
@app.route("/fototime")
def fototime():
    kut = Thread(target = camera.preview)
    kut.start()
@app.route("/print/<src>")
def printx(src):
    return render_template("yazdir.html", img = "/arsiv/" + src)
@app.route("/galeri")
def galeri():
    return "Galeri"

@socket.on("print")
def printer(img):
    printer.thermprint(img, CONFIG.date, CONFIG.count)
    redirect("/")
@socket.on("set config")
def newconfig(data):
    CONFIG.count = data.count
    CONFIG.date = data.date
if __name__ == "__main__":
    socket.run(app)
    