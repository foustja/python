#!/usr/bin/env python

#mandel_music.py
#Jack Foust
#3/12/2016
#foustja@gmail.com

'''
OS and environment

Variants of this code run under Python 2.7.6 and 3.4.3 (this version has been
written for 2.7.6). It imports math, PIL (Python Imaging Library) and Tkinter
(tkinter under python3) modules.

PIL and Tkinter will need to be installed.

It has been tested under Ubuntu 14.04. Code was edited using Atom 1.0.1



Install Tkinter under Ubuntu 14.04 with the command:

sudo apt-get install python-tk



To install PIL you may need to do something like this:

sudo apt-get install python-pip
sudo apt-get build-dep python-imaging
sudo apt-get install libjpeg8 libjpeg62-dev libfreetype6 libfreetype6-dev
sudo pip install Pillow

(This installs Pillow, which replaces PIL.)



If you are using python3, you may also need to use these commands:

sudo apt-get install python3-pil
sudo apt-get install python-pil.imagetk
sudo apt-get install python3-pil.imagetk

Tkinter is imported as tkinter under python3 and requires installation of
python3-tk:

sudo apt-get install python3-tk
sudo apt-get install python-imaging-tk


Mathematical background

The script draws an image of the Mandelbrot set using shades of blue to
indicate how many iterations of the Mandelbrot generating algorithm have taken
place without the result exceeding a pre-defined bound (in this case, 4.0). If
the result does not exceed 4.0 after 20 iterations, then it is expected that
this value will be confined to the set of finite real numbers and not diverge
to infinity. The set of points in the complex plane which satisfies these
conditions is referred to as the Mandelbrot set, and these points will be
colored black (0, 0, 0) in the image.


The function used to generate the Mandelbrot set is the iterated function:

z_new = z*z - c

where z and c are complex numbers of the form:

z = x + i*y

and

c = a + i*b

The initial value of z is set to 0, and the function is iterated 20 times for
each value of c in the subset of the complex plane represented by the values
-1.5 to 2.5 for a and -1.5 to 1.5 for b. Horizontal values represent the real
values a, and values on the vertical axis represent imaginary values b.

(The computer sets a value of (0, 0) to the upper left hand corner of the
screen, and so the screen values (m, n) are transformed to (x, y) plane values
before they are entered into the function. Pixel colors are set according to
(m, n) values on the screen.)

The results of the iterated function can be represented thus:

z_new = z*z - c
z_new = (x*x - y*y -a) + i*(2*x*y - b)

where

x_new = x*x - y*y - a
y_new = 2*x*y - b

and the square modulus of z_new, mzsq = x_new*x_new + y_new*y_new.

(The square modulus is the square of the distance from the origin between the
real and the imaginary values of a complex number. It is obtained by adding the
squares of the real and the imaginary parts.)

It is the square modulus (mzsq) which is tested, and if mzsq < 4.0 after 20
iterations, then the initial value of c for this series of iterations is
considered to belong to the Mandelbrot set, and the corresponding screen pixel
at (m, n) is colored black.

Code and algorithms were adapted from "Dynamical Systems and Fractals: Computer
graphics experiments in Pascal," by Karl-Heinz Becker and Michael Doerfler, 2nd
edition, 1988.


Sound

The original code, which produced an image of the Madelbrot set, has been
modified for sound production. The sounds producd are still very rudimentary.
The concept is to produce tones according to patterns produced by the iterated
formulae and square modulus tests described above.

The sound module used is the Snack toolkit, developed by Kare Sjolander 
of the Department of Speech, Music and Hearing, KTH Royal Institute of 
Technology, Stockholm.

The web page for the Snack toolkit may be found at: 

http://www.speech.kth.se/snack/

Under Ubuntu, the necessary packages can be installed using the following
commands:

sudo apt-get install libsnack2
sudo apt-get install libsnack2-dev
sudo apt-get install libsnack2-alsa
sudo apt-get install python-tksnack

Snack must be used in conjunction with Tkinter. Import as tkSnack. A tutorial
is available at http://www.speech.kth.se/snack/man/snack2.2/python-man.html.

'''

import math
from PIL import Image, ImageTk
import Tkinter
from tkSnack import *
from time import sleep

root = Tkinter.Tk()

initializeSnack(root)

s = Sound() #tksnack Sound object
filt = Filter('generator', 220.0) #sound Filter object, initialized
freq = 440.0 #A4
dur  = 2.0 #duration of sound produced in seconds
frequencyarray = [] #python list stores frequencies
interrupt = 1
maxarray = 500000 #upper limit for frequency list size
#frequencyarray = [2*391.9954, 2*440.0000, 2*349.2282, 2*174.6141]


def Mandelbrot():
    #function to test values of c = a + i*b for inclusion in Mandelbrot set
    canvasWidth = 800
    canvasHeight = 600
    global canvas
    canvas = Image.new("RGB", (canvasWidth, canvasHeight))

    for m in range(800):
        a_system = m
        a = -1.5 + a_system/200.00
        #transforms m to a value in the complex plane with the origin placed
        #somewhat ofset from the center of the window, to provide a good image
        #of the set

        for n in range(600):
            b_system = n
            b = 1.5 - b_system/200.00
            #transforms n to a value in the complex plane
            x = 0.0
            y = 0.0
            mzsq = 0.00
            counter = 0

            while (counter <= 20):
                #loop to iterate function z = z*z - c
                x_new = x*x - y*y - a
                y_new = 2.00*x*y - b
                #calculate square of the modulus of z
                mzsq = x_new*x_new + y_new*y_new

                #series of tests to determine if c is a member of he Mandelbrot
                #set and to color the screen pixels according to whether or not
                #the value of c is included in the set, and how many iterations
                #have been performed
                if mzsq>4.0 and 0 <= counter <= 13:
                    canvas.putpixel ( (m, n), (25, 15, 105))

                elif mzsq>4.0 and 14 <= counter <= 15:
                    canvas.putpixel ( (m, n), (45, 20, 160))

                elif mzsq>4.0 and 16 <= counter <= 17:
                    canvas.putpixel ( (m, n), (65, 25, 180))
                    if len(frequencyarray) < maxarray:
                        frequencyarray.append(2*329.6276)#E5

                elif mzsq>4.0 and 18 <= counter <= 20:
                    canvas.putpixel ( (m, n), (75, 30, 235))
                    if len(frequencyarray) < maxarray:
                        frequencyarray.append(2*261.6256)#c5

                elif mzsq<=4.0:
                    canvas.putpixel ( (m, n), (0, 0, 0))
                    #if len(frequencyarray) < maxarray:
                        #frequencyarray.append(2*391.9954)#G5

                x = x_new
                y = y_new
                counter = counter + 1


def tone(freq, dur):
    s.stop()
    filt.configure(freq, 30000, 0.0, 'sine', int(dur*11500))
    s.play(filter=filt, blocking=1)


def music(n): #recursive function, not used due to python's maximum recursion
              #depth of 1000.
    root.update()
    if interrupt == 0 and n<=(len(frequencyarray) - 1):
        tone(frequencyarray[n], dur)
        root.after(1, music(n+1))

#contains for loop which polls the OS for events prior to each iteration
def music2():
    for i in frequencyarray:
        if interrupt == 0:
            tone(i, dur)
            root.update()


def music3():# does not allowing ermination by stop function
    while interrupt == 0:
        for i in frequencyarray:
            tone(i, dur)
            root.update()
            sleep(1)


def start():
    global interrupt
    interrupt=0
    #music(0)
    music2()
    #music3()

def stop():
    global interrupt
    interrupt=1


def displayTkWindow():
    #function to display results of Mandelbrot in a simple Tk window
    tkcanvas_width = 800
    tkcanvas_height = 600

    root.title ("Mandelbrot")

    tkcanvas = Tkinter.Canvas(root, width=tkcanvas_width,
    height=tkcanvas_height)
    tkcanvas.pack(side='top')

    img = ImageTk.PhotoImage(canvas)
    tkcanvas.create_image(400, 300, image=img)
    tkcanvas.image = img

    playbutton=Tkinter.Button(root, text='Music', command=start)
    playbutton.pack(side='left')
    stopbutton=Tkinter.Button(root, text='Stop', command=stop)
    stopbutton.pack(side='left')

    root.mainloop()


def main():
    #main function as recommended by Guido for good pythonic style
    Mandelbrot()
    displayTkWindow()
    #canvas.show()

if __name__ == "__main__":
        main()

"""
The canvas.show() method can be uncommented to provide a another way of
displaying results. Whether or not it works is likely to be OS dependent.
In Ubuntu 14.04 it was necessary to modify the code in the ImageShow.py
module in order for it to call the default viewer.

This is done in the following manner:

Find /usr/lib/python2.7/dist-packages/PIL/ImageShow.py (or lib/python3.4/
site-packages/PIL/ImageShow.py) and open for editing. Look for the following
code:

class DisplayViewer(UnixViewer):
    def get_command_ex(self, file, **options):
        command = executable = "display"
        return command, executable

if which("display"):
    register(DisplayViewer)

Replace "display" (which is the command for imagemagick) with "eog" (which
calls the default viewer in Ubuntu). The module should now work correctly.

This solution was provided by Clemens Sielaff (clemens-sielaff.com) and can be
found at

http://stackoverflow.com/questions/16279441/image-show-wont-display-the-picture

"""
