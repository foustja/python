#!/usr/bin/env python

#fractal 1.0.1.py
#Jack Foust
#foustja@gmail.com

'''
This code runs under Ubuntu 14.0 and Python 2.7.6. It imports math, PIL
(Python Imaging Library) and Tkinter modules. Code was edited using Atom 1.0.1.
Python, PIL (including ImageTk) and Tkinter will need to be installed:

sudo apt-get install python-tk
sudo apt-get install python-pil
sudo apt-get install python-pil.imagetk

Python 2.7 should be installed by default. If not:

sudo apt-get install python2.7

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

The square of the modulus of z_new, mzsq = x_new*x_new + y_new*y_new

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
import tkFileDialog
import tkMessageBox

def mandelbrotImageIterate():
    #function to test values of c = a + i*b for inclusion in Mandelbrot set
    global fracImage

    fracImageWidth = 800
    fracImageHeight = 600

    fracImage = Image.new("RGB", (fracImageWidth, fracImageHeight))

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

                """if(mzsq>4.0 and 0 <= counter <= 20):
                    fracImage.putpixel ( (m, n)

                elif(mzsq<=4.0):
                    fracImage.putpixel ( (m, n), (0, 0, 0))"""


                if(mzsq>4.0 and 0 <= counter <= 13):
                    fracImage.putpixel ( (m, n), (25, 15, 105))
                    """tkCanvas.create_line (m, n, m, n,
                    fill=("#%02x%02x%02x" % (25, 15, 105)))"""

                elif(mzsq>4.0 and 14 <= counter <= 15):
                    fracImage.putpixel ( (m, n), (45, 20, 160))
                elif(mzsq>4.0 and 16 <= counter <= 17):
                    fracImage.putpixel ( (m, n), (65, 25, 180))

                elif(mzsq>4.0 and 18 <= counter <= 20):
                    fracImage.putpixel ( (m, n), (75, 30, 235))


                elif(mzsq<=4.0):
                    fracImage.putpixel ( (m, n), (0, 0, 0))

                x = x_new
                y = y_new
                counter = counter + 1

    imageDisplay()


def juliaImageIterate():
    #function to test values of c = a + i*b for inclusion in Mandelbrot set
    global fracImage

    fracImageWidth = 800
    fracImageHeight = 600

    fracImage = Image.new("RGB", (fracImageWidth, fracImageHeight))

    c1 = float(c1Entry.get())
    c2 = float(c2Entry.get())

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
            x = a
            y = b
            mzsq = 0.00
            counter = 0

            while (counter <= 20):
                #loop to iterate function z = z*z - c
                x_new = x*x - y*y - c1
                y_new = 2.00*x*y - c2
                #calculate square of the modulus of z
                mzsq = x_new*x_new + y_new*y_new

                #series of tests to determine if c is a member of he Julia
                #set and to color the screen pixels according to whether or not
                #the value of c is included in the set, and how many iterations
                #have been performed

                """if(mzsq>4.0 and 0 <= counter <= 20):
                    fracImage.putpixel ( (m, n), (25, 15, 105))

                elif(mzsq<=4.0):
                    fracImage.putpixel ( (m, n), (0, 0, 0))"""


                if(mzsq>4.0 and 0 <= counter <= 13):
                    fracImage.putpixel ( (m, n), (25, 15, 105))
                    """tkCanvas.create_line (m, n, m, n,
                    fill=("#%02x%02x%02x" % (25, 15, 105)))"""

                elif(mzsq>4.0 and 14 <= counter <= 15):
                    fracImage.putpixel ( (m, n), (45, 20, 160))

                elif(mzsq>4.0 and 16 <= counter <= 17):
                    fracImage.putpixel ( (m, n), (65, 25, 180))

                elif(mzsq>4.0 and 18 <= counter <= 20):
                    fracImage.putpixel ( (m, n), (75, 30, 235))


                elif(mzsq<=4.0):
                    fracImage.putpixel ( (m, n), (0, 0, 0))

                x = x_new
                y = y_new
                counter = counter + 1

    imageDisplay()


def imageDisplay():
    global fracImage
    global tkCanvas

    img = ImageTk.PhotoImage(fracImage)
    tkCanvas.create_image(400, 300, image=img)
    tkCanvas.image = img

def openImage():
    global fracImage
    global tkCanvas

    filename=tkFileDialog.askopenfilename(title='Open File',
    defaultextension='.bmp', filetypes=(("BMP", "*.bmp"),("PNG", "*.png"),
    ("JPEG", "*.jpg"), ("All Files", "*.*")))

    img = ImageTk.PhotoImage(file=filename)
    tkCanvas.create_image(400, 300, image=img)
    tkCanvas.image = img

def saveImage():
    global fracImage

    filename = tkFileDialog.asksaveasfilename(title='Save to File',
    defaultextension='.bmp', filetypes=(("BMP", "*.bmp"),("PNG", "*.png"),
    ("JPEG", "*.jpg"), ("All Files", "*.*")))
    fracImage.save(filename)

def clearImage():
    global tkCanvas

    tkCanvas.delete('all')

def infoBox():
    tkMessageBox.showinfo('About fractal 1.0.1',
    'Python fractal generating script\n\nfoustja@gmail.com\n2016')

def textBox():
    global tkRoot

    tkToplevel = Tkinter.Toplevel(tkRoot)
    tkToplevel.title('Program Information and Reference')

    tkText = Tkinter.Text(tkToplevel, height= 40, width= 60)
    quote = """

    The python script underlying this application
    generates images of the Mandelbrot and Julia sets
    using an iterated complex function z_new = z*z - c
    (see reference by Becker and Doerfler below). The
    Julia set requires user input of two parameters,
    c1 and c2. (Try c1=0.8 and c2=0.12, to start.)

    The original code runs under Ubuntu 14.0 and Python
    2.7.6. It imports math, PIL (Python Imaging Library)
    and Tkinter modules. Code was edited using Atom 1.0.1.

    If run in its original form as a Python script, Python,
    PIL (including ImageTk) and Tkinter will need to be
    installed:

    sudo apt-get install python-tk
    sudo apt-get install python-pil
    sudo apt-get install python-pil.imagetk

    Python 2.7 should be installed by default. If not:

    sudo apt-get install python2.7

    The file may be run as a script at the the terminal
    prompt:

    ./frac1.py (or whatever name you give it)

    File must have execute permissions:

    chmod u+c

    Code and algorithms were adapted from "Dynamical
    Systems and Fractals: Computer graphics experiments
    in Pascal," by Karl-Heinz Becker and Michael Doerfler,
    2nd edition, 1988.

    """
    tkText.insert(Tkinter.END, quote)
    tkText.pack(side=Tkinter.TOP)

    tkFrame = Tkinter.Frame(tkToplevel)
    tkFrame.pack(side=Tkinter.TOP)

    tkButton = Tkinter.Button(tkFrame, text='Close', width=25,
    command=tkToplevel.destroy)
    tkButton.pack()


def displayTkWindow():
    #function to display results of Mandelbrot in a simple Tk window
    global tkRoot
    global tkCanvas
    global c1Entry
    global c2Entry

    tkCanvas_width = 800
    tkCanvas_height = 600

    tkRoot = Tkinter.Tk()
    tkRoot.title ('fractal 1.0.1')
    icon = ImageTk.PhotoImage(file='fractal.bmp')
    tkRoot.tk.call('wm', 'iconphoto', tkRoot._w, icon)

    tkCanvas = Tkinter.Canvas(tkRoot, width=tkCanvas_width,
    height=tkCanvas_height)
    tkCanvas.pack()

    tkFrame = Tkinter.Frame(tkRoot)
    tkFrame.pack(side=Tkinter.LEFT)

    tkFrame2 = Tkinter.Frame(tkRoot)
    tkFrame2.pack(side=Tkinter.LEFT)

    """tkFrame3 = Tkinter.Frame(tkRoot)
    tkFrame3.pack(side=Tkinter.LEFT)"""

    tkButton1 = Tkinter.Button(tkFrame, text='Mandelbrot', width=25,
    command=mandelbrotImageIterate)
    tkButton1.pack(side=Tkinter.LEFT)

    tkButton2 = Tkinter.Button(tkFrame, text='Julia', width=25,
    command=juliaImageIterate)
    tkButton2.pack(side=Tkinter.LEFT)

    """tkButton = Tkinter.Button(tkFrame2, text='Save', width=25,
    command=saveImage)
    tkButton.pack(side=Tkinter.TOP)

    tkButton = Tkinter.Button(tkFrame2, text='Exit', width=25,
    command=tkRoot.destroy)
    tkButton.pack(side=Tkinter.TOP)"""

    c1Label = Tkinter.Label(tkFrame2, text='c1')
    c1Label.pack(side=Tkinter.LEFT)

    c1Entry = Tkinter.Entry(tkFrame2)
    c1Entry.pack(side=Tkinter.LEFT)
    c1Entry.insert(0, 0.0)

    c2Label = Tkinter.Label(tkFrame2, text='c2')
    c2Label.pack(side=Tkinter.LEFT)

    c2Entry = Tkinter.Entry(tkFrame2)
    c2Entry.pack(side=Tkinter.LEFT)
    c2Entry.insert(0, 0.0)

    # create a toplevel menu
    menubar = Tkinter.Menu(tkRoot)
    # create a pulldown menu, and add it to the menu bar
    filemenu = Tkinter.Menu(menubar, tearoff=0)
    filemenu.add_command(label='Open', command=openImage)
    filemenu.add_command(label='Save', command=saveImage)
    filemenu.add_command(label='Clear', command=clearImage)
    filemenu.add_command(label='Quit', command=tkRoot.destroy)

    filemenu2 = Tkinter.Menu(menubar, tearoff=0)
    filemenu2.add_command(label='About fractal 1.0.1', command=infoBox)
    filemenu2.add_command(label='Information and Reference', command=textBox)

    menubar.add_cascade(label='File', menu=filemenu)
    menubar.add_cascade(label='About', menu=filemenu2)
    tkRoot.config(menu=menubar)


    Tkinter.mainloop()

def main():
    #main function as recommended by Guido for good pythonic style

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
