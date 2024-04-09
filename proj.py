from tkinter import*
"""to create the gui-tkinter"""
from PIL import Image,ImageTk
"""PIL(pillow)-used for inserting imgs"""
import random
def scissor():
    l=["scissor","rock","paper"]
    b=l[random.randint(0,2)]
    
    if b=="scissor":
        e="tie"
        final_msg(e)
        
    elif b=="rock":
        e="loss"
        final_msg(e)
        
    elif b=="paper":
        e="won"
        final_msg(e)
        
    else:
        e="invalip input"
        final_msg(e)
    label3=Label(window,text="coomputer:"+b,width=20,height=5,font=20,bg="purple",fg="white").grid(row=4,column=0)
def rock():
    l=["scissor","rock","paper"]
    b=l[random.randint(0,2)]
    print(b)
    
    if b=="scissor":
        e="win"
        final_msg(e)
    elif b=="rock":
        e="tie"
        final_msg(e)
    elif b=="paper":
        e="loss"
        final_msg(e)
    else:
        e="invalip input"
        final_msg(e)
    label3=Label(window,text="coomputer:"+b,width=20,height=5,font=20,bg="purple",fg="white").grid(row=4,column=0)
def paper():
    l=["scissor","rock","paper"]
    b=l[random.randint(0,2)]
    print(b)
    
    if b=="scissor":
        e="loss"
        final_msg(e)
    elif b=="rock":
        e="win"
        final_msg(e)
    elif b=="paper":
        e="tie"
        final_msg(e)
    else:
        e="invalip input"
        final_msg(e)
    label3=Label(window,text="coomputer:"+b,width=20,height=5,font=20,bg="purple",fg="white").grid(row=4,column=0)
window=Tk()
window.title("python mini project")
window.configure(background="yellow")

def final_msg(d):
    
    final_message=Label(window,width=7,height=2,text=d,font=("arial narrow",40,"bold"),bg="red",fg="white").grid(row=3,column=3)

"""scissor_img=ImageTk.PhotoImage(Image.open("scissor.png"))
rock_img=ImageTk.PhotoImage(Image.open("fist.png"))
paper_img=ImageTk.PhotoImage(Image.open("paper.png"))"""

scissor_but=Button(window,width=25,height=5,text="SCISSORS",font=("arial narrow",20,"bold"),bg="white",fg='black',command=scissor).grid(row=1,column=1)
rock_but=Button(window,width=25,height=5,text="ROCK",font=("arial narrow",20,"bold"),bg="white",fg='black',command=rock).grid(row=1,column=3)
paper_but=Button(window,width=25,height=5,text="PAPER",font=("arial narrow",20,"bold"),bg="white",fg='black',command=paper).grid(row=1,column=5)



