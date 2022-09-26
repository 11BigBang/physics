# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 07:28:52 2020

@author: wbmar
"""

from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter import ttk

class Frame1(Frame):
    

    DEFAULT_PEN_SIZE = 5.0
    DEFAULT_COLOR = 'black'
    
    def __init__(self, parent, photo):
        Frame.__init__(self, parent, bg="red")
        
        image_file = r"C:\Users\wbmar\OneDrive\Documents\Phalanx\BulgarianSplitSquat.png"
        photo = PhotoImage(file=image_file)
        
        self.parent = parent
        self.pen_button = Button(self, text='pen', command=self.use_pen)
        self.pen_button.grid(row=0, column=0)

        self.brush_button = Button(self, text='brush', command=self.use_brush)
        self.brush_button.grid(row=0, column=1)

        self.color_button = Button(self, text='color', command=self.choose_color)
        self.color_button.grid(row=0, column=2)

        self.eraser_button = Button(self, text='eraser', command=self.use_eraser)
        self.eraser_button.grid(row=0, column=3)

        self.choose_size_button = Scale(self, from_=1, to=10, orient=HORIZONTAL)
        self.choose_size_button.grid(row=0, column=4)

        self.c = Canvas(self, bg='white', width=600, height=600)
        self.c.grid(row=1, columnspan=5)

        self.photo = photo
        self.img = self.c.create_image(0, 0, image=photo, anchor='nw')
        self.c.bind("<B1-Motion>", self.move_image)

        self.setup()

    def move_image(self, event):
        # delete the old image
        self.c.delete(self.img)
        # get the mouse position
        x = event.x
        y = event.y
        # create the new image at position x, y
        self.img = self.c.create_image(x, y, image=self.photo,
            anchor='nw')
        self.c.update()

    def setup(self):
        self.old_x = None
        self.old_y = None
        self.line_width = self.choose_size_button.get()
        self.color = self.DEFAULT_COLOR
        self.eraser_on = False
        self.active_button = self.pen_button
        self.c.bind('<B1-Motion>', self.paint)
        self.c.bind('<ButtonRelease-1>', self.reset)

    def use_pen(self):
        self.activate_button(self.pen_button)

    def use_brush(self):
        self.activate_button(self.brush_button)

    def choose_color(self):
        self.eraser_on = False
        self.color = askcolor(color=self.color)[1]

    def use_eraser(self):
        self.activate_button(self.eraser_button, eraser_mode=True)

    def activate_button(self, some_button, eraser_mode=False):
        self.active_button.config(relief=RAISED)
        some_button.config(relief=SUNKEN)
        self.active_button = some_button
        self.eraser_on = eraser_mode

    def paint(self, event):
        self.line_width = self.choose_size_button.get()
        paint_color = 'white' if self.eraser_on else self.color
        if self.old_x and self.old_y:
            self.c.create_line(self.old_x, self.old_y, event.x, event.y,
                               width=self.line_width, fill=paint_color,
                               capstyle=ROUND, smooth=TRUE, splinesteps=36)
        self.old_x = event.x
        self.old_y = event.y

    def reset(self, event):
        self.old_x, self.old_y = None, None


class MainW(Tk):
    
    image_file = r"C:\Users\wbmar\OneDrive\Documents\Phalanx\BulgarianSplitSquat.png"
    photo = PhotoImage(file=image_file)

    def __init__(self, parent):
        Tk.__init__(self, parent)
        self.parent = parent
        self.title('ChopBlock')
        self.mainWidgets()
        self.geometry('1350x600')
        self.reftext1()
        self.reftext2()
        
    def mainWidgets(self):
        
        self.tabControl = ttk.Notebook(self)
        self.tab1 = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tab1, text='ranger info')
        self.tabControl.grid(column=0, row=0)
        self.tab2 = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tab2, text='infantry stuff')

        self.window = Frame1(self,photo)
        self.window.grid(row=0, column=2, rowspan=30)
        
    def reftext1(self):
        self.rangertext = Text(self.tab1,width='50',height='3')
        self.rangertext.grid(row=2)
        self.rangertext.insert(END,'some ranger text')
        
    def reftext2(self):
        self.infantrytext = Text(self.tab2,width='50',height='3')
        self.infantrytext.grid(row=2)
        self.infantrytext.insert(END,'some infantry text')


if __name__=="__main__":
    app = MainW(None)
    app.mainloop()