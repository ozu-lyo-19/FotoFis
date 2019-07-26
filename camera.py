import RPi.GPIO as GPIO
from threading import Thread
from picamera import PiCamera
from time import sleep
from PIL import Image
import shutil, os, datetime
camera = PiCamera()
not_captured = True
previewing = False
def capture():
    # camera.start_preview()
    camera.resolution= (400,400)
    camera.color_effects = (128,128)
    name = str(datetime.datetime.now().strftime("%H-%M-%S-%d-%m-%y"))+".jpg"
    camera.capture(name)
    camera.stop_preview()
    shutil.move(name, "arsiv/")
    return name
def preview():
    camera.start_preview()
    previewing = True
    camera.resolution= (400,400)
    camera.color_effects = (128,128)
    sleep(1)

