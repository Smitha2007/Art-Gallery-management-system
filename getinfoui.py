import os
import pickle
import tkinter

details_list=[]
l2=[]
G = []
def file_save():
    NAME_PRO = details_list[0]
    ADDRESS_PRO = details_list[1]
    MOBILE_NO_PRO = details_list[2]
    ROOM_NO_PRO = details_list[3]
    PRICE_PRO = details_list[4]
    f = open("hotel.dat", "ab")
    a=save(NAME_PRO,ADDRESS_PRO,MOBILE_NO_PRO,ROOM_NO_PRO,PRICE_PRO)
    pickle.dump(a,f,protocol=2)
    f.close()
    restart_program()


def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)






class save:
    def __init__(self, NAME_PRO, ADDRESS_PRO, MOBILE_NO_PRO, ROOM_NO_PRO, PRICE_PRO):
        self.name=NAME_PRO
        self.address=ADDRESS_PRO
        self.mobile_no=MOBILE_NO_PRO
        self.room_no=ROOM_NO_PRO
        self.price=PRICE_PRO
        print(self.name,self.address,self.mobile_no,self.room_no,self.price)

import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

from PIL import ImageTk,Image


class HOTEL_MANAGEMENT:
    def __init__(self):
        def gotinfo():
            self.gettininfo = str(self.gather.get())
            print(self.gettininfo)
            print("\n")
            if self.gettininfo.isdigit() == True and len(self.gettininfo) != 0:
                self.Text1.insert(INSERT, " valid room number ""\n")
            else :
                self.Text1.insert(INSERT,"invalid room number""\n")

            try:
                n = 0
                f2 = open("hotel.dat", "rb")
                while True:
                    s = pickle.load(f2)
                    a = str(s.room_no)
                    print (a)
                    if self.gettininfo == a:
                        n = 1
                        print("NAME-", "\t", "\t", s.name)
                        print("\n")
                        print("ADDRESS-", "\t", s.address)
                        print("\n")
                        print("MOBILE NO.-", "  ", s.mobile_no)
                        print("\n")
                        print("HIS TOTAL BILL IS Rs.", s.price)
                    elif EOFError:
                        if n == 0:
                            print("NO GUEST IN ROOM ", self.gettininfo)
                        else:
                            n = 0
                            continue
            except EOFError:
                pass
                f2.close()

        root = Tk()

        #root.mainloop()
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#d9d9d9' # X11 color: 'gray85'
        font10 = "-family {Segoe UI} -size 17 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font11 = "-family {Segoe UI} -size 28 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font9 = "-family {Segoe UI} -size 23 -weight bold -slant roman"  \
            " -underline 0 -overstrike 0"

        root.geometry("881x582+249+104")
        root.title("ART GALARY")
        root.configure(background="#ffe6e6")



        self.Frame1 = Frame(root)
        self.Frame1.place(relx=0.02, rely=0.03, relheight=0.94, relwidth=0.94)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="0")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#ffe6e6")
        self.Frame1.configure(width=825)

        if False:
            '''
            self.Text1 = Text(self.Frame1)
            self.Text1.place(relx=0.04, rely=0.46, relheight=0.48, relwidth=0.93)
            self.Text1.configure(background="white")
            self.Text1.configure(font="TkTextFont")
            self.Text1.configure(foreground="black")
            self.Text1.configure(highlightbackground="#d9d9d9")
            self.Text1.configure(highlightcolor="black")
            self.Text1.configure(insertbackground="black")
            self.Text1.configure(selectbackground="#c4c4c4")
            self.Text1.configure(selectforeground="black")
            self.Text1.configure(width=764)
            self.Text1.configure(wrap=WORD)



            self.Label1 = Label(self.Frame1)
            self.Label1.place(relx=0.12, rely=0.15, height=48, width=377)
            self.Label1.configure(background="#d9d9d9")
            self.Label1.configure(disabledforeground="#a3a3a3")
            self.Label1.configure(font=font9)
            self.Label1.configure(foreground="#000000")
            self.Label1.configure(text='ENTER THE ROOM NO.   :')

            self.Entry1 = Entry(self.Frame1)
            self.gather=StringVar()
            self.Entry1.place(relx=0.65, rely=0.17,height=40, relwidth=0.1)
            self.Entry1.configure(background="white")
            self.Entry1.configure(disabledforeground="#a3a3a3")
            self.Entry1.configure(font="TkFixedFont")
            self.Entry1.configure(foreground="#000000")
            self.Entry1.configure(insertbackground="black")
            self.Entry1.configure(width=84)
            self.Entry1.configure(textvariable=self.gather)


            self.Button1 = Button(self.Frame1)
            self.Button1.place(relx=0.39, rely=0.29, height=74, width=197)
            self.Button1.configure(activebackground="#d9d9d9")
            self.Button1.configure(activeforeground="#000000")
            self.Button1.configure(background="#d9d9d9")
            self.Button1.configure(disabledforeground="#a3a3a3")
            self.Button1.configure(font=font10)
            self.Button1.configure(foreground="#000000")
            self.Button1.configure(highlightbackground="#d9d9d9")
            self.Button1.configure(highlightcolor="black")
            self.Button1.configure(pady="0")
            self.Button1.configure(text='SUBMIT')
            self.Button1.configure(width=197)
            self.Button1.configure(command=gotinfo)

            self.Message1 = Message(self.Frame1)
            self.Message1.place(relx=0.22, rely=0.02, relheight=0.12, relwidth=0.56)
            self.Message1.configure(background="#d9d9d9")
            self.Message1.configure(font=font11)
            self.Message1.configure(foreground="#000000")
            self.Message1.configure(highlightbackground="#d9d9d9")
            self.Message1.configure(highlightcolor="black")
            self.Message1.configure(text='GET INFO HERE ..!!')
            self.Message1.configure(width=460)
            '''

        self.canvas = []
        self.img = []
        self.canvas_img = []
        self.label = []
        image = []
        i = 0
        j = 0
        index = 0
        for filename in os.listdir('images'):
            #print(filename)

            self.canvas.append('')
            self.img.append('')
            self.canvas_img.append('')
            self.label.append('')
            image.append('')

            self.canvas[index] = Canvas(root, width=200, height=180)
            self.canvas[index].pack()
            self.canvas[index].place(relx=0.08+i, rely=0.03+j)#, relheight=0.4, relwidth=0.4)
            image[index] = Image.open('images/'+filename)
            image[index] = image[index].resize((200,200), Image.ANTIALIAS)
            self.img[index] = ImageTk.PhotoImage(image[index])
            self.canvas_img[index] = self.canvas[index].create_image(0, 0, anchor="nw", image=self.img[index])
            self.label[index] = tkinter.Label(root, image=self.img[index])
            i += 0.3
            #j += 1
            index += 1

            if index%3 == 0:
                j += 0.32
                i = 0
                print(index, j)
            #print('here')

        '''
        self.canvas1 = Canvas(root, width=200, height=200)
        self.canvas1.pack()
        self.canvas1.place(relx=0.3, rely=0.03)#, relheight=0.4, relwidth=0.4)
        image1 = Image.open("images/hh.jpg")
        image1 = image1.resize((200,200), Image.ANTIALIAS)
        self.img1 = ImageTk.PhotoImage(image1)
        self.canvas_img1 = self.canvas1.create_image(0, 0, anchor="nw", image=self.img1)
        self.label1 = tkinter.Label(root, image=self.img1)

        self.canvas.append('')
        self.img.append('')
        self.canvas_img.append('')
        self.label.append('')

        self.canvas[0] = Canvas(root, width=200, height=200)
        self.canvas[0].pack()
        self.canvas[0].place(relx=0.02, rely=0.03)#, relheight=0.4, relwidth=0.4)
        image = Image.open("Smitha_Image.jpeg")
        image = image.resize((200,200), Image.ANTIALIAS)
        self.img[0] = ImageTk.PhotoImage(image)
        self.canvas_img[0] = self.canvas[0].create_image(0, 0, anchor="nw", image=self.img[0])
        self.label[0] = tkinter.Label(root, image=self.img)


        self.canvas1 = Canvas(root, width=200, height=200)
        self.canvas1.pack()
        self.canvas1.place(relx=0.3, rely=0.03)#, relheight=0.4, relwidth=0.4)
        image1 = Image.open("images/hh.jpg")
        image1 = image1.resize((200,200), Image.ANTIALIAS)
        self.img1 = ImageTk.PhotoImage(image1)
        self.canvas_img1 = self.canvas1.create_image(0, 0, anchor="nw", image=self.img1)
        self.label1 = tkinter.Label(root, image=self.img1)
        '''


        if False:
            '''
            self.canvas = Canvas(root, width = 300, height = 300)
            self.canvas.place(relx=0.22, rely=0.08, relheight=0.12, relwidth=0.56)
            image = Image.open("Smitha_Image.jpeg")
            image = image.resize((40,40), Image.ANTIALIAS)
            self.img = ImageTk.PhotoImage(image)
            self.canvas.create_image(0, 0, anchor='nw', image=self.img)
            self.canvas.pack()
            '''
            #self.img = Label(self.img)
            #self.img.image = self.img
            #self.img.place(x=0, y=0)

            '''
            image = Image.open('path_to_your_image.png')
            # The (450, 350) is (height, width)
            image = image.resize((450, 350), Image.ANTIALIAS)
            my_img = ImageTk.PhotoImage(image)
            my_img = Label(image = my_img)
            my_img.pack()

            root.mainloop()
            '''

        root.mainloop()




if __name__ == '__main__':
    GETINFO=HOTEL_MANAGEMENT()
