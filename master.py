from tkinter import *
import tkinter as tk
import tkinter.messagebox

from tkinter import ttk, Tk
import ctypes
from PIL import ImageTk,Image

class APP():
    def __init__(self):
        self.screen = Tk()
        self.screen.resizable(0, 0)
        LR = []
        for i in self.getGeometry(660, 415): LR.append(i)
        self.screen.geometry("%dx%d+%d+%d" % (LR[0], LR[1], LR[2], LR[3]))
        self.screen.title('ElConvertor')
        #self.screen.iconbitmap(default='DATA/ico.ico')
        myappid = 'mycompany.myproduct.subproduct.version'
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
        ph_BG = ImageTk.PhotoImage(file='Data/bg.png')
        self.icon_size = ttk.Label(self.screen, image=ph_BG)
        self.icon_size.place(x=-2, y=-2)
        OPTIONS = [
            
            ]
        for i in range(2,17):
            desc=""
            if(i==2):
                desc = " -Binarie"
            elif(i==8):
                desc = " -Octal"
            elif (i==10):
                desc = " -Decimal"
            elif (i==16):
                desc = " -HexDecimal"
            OPTIONS.append("BASE "+str(i)+desc)
        OPTIONS.append("BASE 24")
        OPTIONS.append("BASE 32")
        self.sl_var1 = StringVar(self.screen)
        self.sl_var1.set("Select Base") # default value
        self.sl_var2 = StringVar(self.screen)
        self.sl_var2.set("Select Base") # default value
        self.SL1 = OptionMenu(self.screen, self.sl_var1, *OPTIONS)
        self.SL1.config(width=18)
        self.SL1.place(x=183, y=147)


        self.SL2 = OptionMenu(self.screen, self.sl_var2, *OPTIONS)
        self.SL2.config(width=18)
        self.SL2.place(x=389, y=147)
        
        self.ent = ttk.Entry(self.screen, width=59)

        self.ent.place(x=183,y=192)

        self.screen.wm_attributes('-transparentcolor', '#ab23ff')
        ph_out = ImageTk.PhotoImage(file='Data/out.png')
        self.Res = Label(self.screen, text = "Resultat",  font=("Montserrat", 15),
         width=30, height=2, bg= '#7301B8', foreground="white")
        self.Res.configure(text= " Resultat: ",anchor="w", justify=RIGHT)
        self.Res.place(x=112, y=241)

        ph5 = tk.PhotoImage(file='Data/btn.png')
        self.bu5 = tk.Button(self.screen, width=147, height=24, image=ph5,
                             borderwidth=0, command=self.Start)
        self.bu5.place(x=412, y=318)

        self.screen.mainloop()
    def getGeometry(self, width, height):
        frm = Tk()
        screen_height = frm.winfo_screenheight()
        screen_width = frm.winfo_screenwidth()
        frm.destroy()
        window_height = height
        window_width = width
        fw = (screen_width - window_width) // 2
        fh = (screen_height - window_height) // 2
        L = [width, height, fw, fh]
        return L

    def Start(self):
        def CheckBaSE(n, B):
            st = str(n)
            i=0
            STP=False
            while(i<len(st) and STP==False):
                if (not("0"<=st[i]<="9")):
                    if(B<11):
                        STP = True
                    elif(not("A"<=st[i].upper()<="F")):
                        STP = True

                i+=1
            return i==len(st)
        def convert_B10_B(N, B):
            STri = "" 
            while True:
                R = N % B
                if(R<=9):
                    STri = str(R) + STri
                else:
                    STri = chr(R+55) + STri
                N//=B
                if(N==0):
                    break
            return STri
        def convert_B_B10(N, B):
            P = 1
            D = 0
            for i in range(len((N))-1, -1, -1):
                print(D)
                if(ord(N[i])>=ord("A")):
                    D += (ord(N[i])-55)*P
                else:
                    D += int(N[i])*P
                P*=B
            return D
        FB = str(self.sl_var1.get())
        TB = str(self.sl_var2.get())
        if(FB=="Select Base" or TB=="Select Base"):
            tkinter.messagebox.showerror("El Convertor",
                    "Please Select Base")  # BS NOT FOUND
        elif(FB==TB):
            tkinter.messagebox.showerror("El Convertor",
                    "Please Select Different Base To Convert")  # BS NOT FOUND
        else:
            INP = self.ent.get()
            if(len(INP)==0 or (not(CheckBaSE(INP, int(FB[FB.find(" ")+1: FB.find("-")-1]))))):
                tkinter.messagebox.showerror("El Convertor",
                    "Please Enter A Number")  # BS NOT FOUND
            else:
                
                B10  = convert_B_B10(str(INP.upper()), int(FB[FB.find(" ")+1: FB.find("-")-1]))
                print(B10)
                DONE = convert_B10_B(int(B10), int(TB[TB.find(" ")+1: TB.find("-")-1]))
                print(DONE)
                self.Res.configure(text="Resultat: "+str(DONE) ,anchor="w", justify=RIGHT)

        

APP()
