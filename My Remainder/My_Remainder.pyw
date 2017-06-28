from Tkinter import *
import tkFont
import os

class My_Remainder:
    def __init__(self,root):
        self.root=root
        root.title("My Remainder!")
        root.geometry("1000x500")
        root.wm_iconbitmap('C:\Users\welcome\Desktop\Ed\Projects\My Remainder\logo.ico')
        root.configure(background="black")



        self.label=Label(root,background='black',foreground='white',text="Anything To Remind !")
        self.label.config(font=("fixedsys", 44))
        self.label.pack(pady=50)


        self.button1=Button(root,text="Nothing",background='white',foreground="black",command=self.open_nothing)
        self.button1.config(font=("fixedsys", 30))
        self.button1.pack(side='left',padx=230)

        self.button1 = Button(root, text="Yeah!", background='white', foreground="black", command=self.open_file)
        self.button1.config(font=("fixedsys", 30))
        self.button1.pack(side='left')

        self.root.resizable(0,0)

    def open_nothing(self):
        
        f=open('C:\Users\welcome\Desktop\Ed\Projects\My Remainder\My_Remainder.txt','w')
        f.truncate()
        f.write("No Remainders\t")
        f.close()
        root.quit()
        

    def open_file(self):
        
        f=open('C:\Users\welcome\Desktop\Ed\Projects\My Remainder\My_Remainder.txt','w')
        f.truncate()
        f.write("Save Before Closing\t")
        f.write("Don't break lines ! Write Continously")
        os.startfile('My_Remainder.txt')
        root.quit()

if __name__=='__main__':
    root=Tk()
    My_Remainder(root)
    root.mainloop()

