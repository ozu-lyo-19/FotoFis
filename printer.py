import os, sys
from escpos import *
from datetime import datetime
p = printer.Usb(0x0416, 0x5011)
def thermprint(pic, date = True, count = 1):
    now = datetime.now().strftime('%d-%m-%Y %H:%M')
    for x in range(count):
        p.text("\n")
        p.image(pic)
        if date: 
            p.text(now)
        p.cut()
# p.text(" RAHATSIZ ETME\nCOK MESGUL")
# p.cut()