from tkinter import *
from random import randint

root=Tk()
root.title("gui")
root.geometry("400x500")
root.config(bg="#262626")
root.resizable(False,False)

def newrand():
    pw_en.delete(0,END)
    pw_len=int(ent.get())
    pas=''

    for x in range(pw_len):
        pas+=chr(randint(33,126))

    pw_en.insert(0,pas)
        


    
def clipper():
    root.clipboard_clear()
    root.clipboard_append(pw_en.get())
#-------label frame-----------------

lf=LabelFrame(root,text='How many characters?')
lf.pack(pady=20)
#--------entry box---------------
ent=Entry(lf,font=("arial",24))
ent.pack(pady=20,padx=20)
#--------entry result----------

pw_en=Entry(root,text='',font=("arial",24))
pw_en.pack(pady=20)

#-----------frame button

frame=Frame(root)
frame.pack(pady=20)

#----------button-------
but=Button(frame,text='generate strong password',command=newrand)
but.grid(row=0,column=0,padx=10)

#----------clipboard-----------

clip=Button(frame,text='copy to clipboard',command=clipper)
clip.grid(row=0,column=1,padx=10)





















root.mainloop() 
