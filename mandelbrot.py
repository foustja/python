#!/usr/bin/env python

#madelbrot.py
#Jack Foust
#foustja@gmail.com

'''
This code runs under Python 2.7.6 and imports math, PIL (Python Imaging
Library) and Tkinter modules. PIL and Tkinter will need to be installed.
It has been tested under Ubuntu 14.04. Code was edited using Atom 1.0.1

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

and the square of the modulus of z_new, mzsq = x_new*x_new + y_new*y_new.

It is the square of the modulus (mzsq) which is tested, and if mzsq < 4.0 after
20 iterations, then the initial value of c for this series of iterations is
considered to belong to the Mandelbrot set, and the corresponding screen pixel
at (m, n) is colored black.


Code and algorithms were adapted from "Dynamical Systems and Fractals: Computer
graphics experiments in Pascal," by Karl-Heinz Becker and Michael Doerfler, 2nd
edition, 1988.
'''

import math
from PIL import Image, ImageTk
import Tkinter

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
                if(mzsq>4.0 and 0 <= counter <= 13):
                    canvas.putpixel ( (m, n), (25, 15, 105))

                elif(mzsq>4.0 and 14 <= counter <= 15):
                    canvas.putpixel ( (m, n), (45, 20, 160))

                elif(mzsq>4.0 and 16 <= counter <= 17):
                    canvas.putpixel ( (m, n), (65, 25, 180))

                elif(mzsq>4.0 and 18 <= counter <= 20):
                    canvas.putpixel ( (m, n), (75, 30, 235))

                elif(mzsq<=4.0):
                    canvas.putpixel ( (m, n), (0, 0, 0))

                x = x_new
                y = y_new
                counter = counter + 1

def displayTkWindow():
    #function to display results of Mandelbrot in a simple Tk window
    tkcanvas_width = 800
    tkcanvas_height = 600

    root = Tkinter.Tk()

    tkcanvas = Tkinter.Canvas(root, width=tkcanvas_width,
    height=tkcanvas_height)
    tkcanvas.pack()

    img = ImageTk.PhotoImage(canvas)
    tkcanvas.create_image(400, 300, image=img)
    tkcanvas.image = img

    Tkinter.mainloop()

def main():
    #main function as recommended by Guido for good pythonic style
    Mandelbrot()
    displayTkWindow()
    #canvas.show()

    #the canvas.show() method can be uncommented to provide a another way of
    #displaying results. Whether or not it works is likely to be OS dependent.
    #In Ubuntu it was necessary to modify the Tkinter ImageShow.py module in 
    #order for the method to call the default viewer. A complete explanation
    #can be found at: 
    
    #http://stackoverflow/questions/16279441/image-show-wont-display-the-picture
    
if __name__ == "__main__":
    main()
