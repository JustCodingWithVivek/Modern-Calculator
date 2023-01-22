from tkinter import *
import customtkinter as ctk
from tkinter import messagebox

#main configurations
root = ctk.CTk()
root.geometry("250x350")
root.minsize(250,350)
root.maxsize(250,350)
root.title("Calculator")
root.config(bg="#000000")
ctk.set_appearance_mode("White")
ctk.set_default_color_theme("blue")
#style
font_1=('halventica',20,'bold')

#function
i=0
equation=""

def show(value):
    global i 
    global equation
    if (value=="%"):
        value="/100"
    equation+=value
    user_entry.insert(i,value)
    i=i+1

def clear():
    global equation
    user_entry.delete(0,END)
    equation=""
    
def calculate():
    try:
        global equation
        result=""
        result=eval(equation)
        clear()
        user_entry.insert(0,result)
    except:
        messagebox.showerror(title="Error",message="Please enter a valid number")

#main
user_entry=ctk.CTkEntry(root,font=font_1,width=250,height=50,text_color="White",fg_color="#000000",border_color="#000000",bg_color="black")
user_entry.place(x=0,y=10)

button1=ctk.CTkButton(root,text="Clear Out",command=clear,font=font_1,width=100,height=40,fg_color="#b5520b",hover_color="#b5520b",bg_color="Black")
button1.place(x=10,y=65)

button2=ctk.CTkButton(root,command=lambda:show("/"),text="/",font=font_1,width=50,height=40,fg_color="#b5520b",hover_color="#b5520b",bg_color="Black")
button2.place(x=190,y=65)

button3=ctk.CTkButton(root,command=lambda:show("%"),text="%",font=font_1,width=50,height=40,fg_color="#b5520b",hover_color="#b5520b",bg_color="Black")
button3.place(x=130,y=65)

button4=ctk.CTkButton(root,command=lambda:show("*"),text="X",font=font_1,width=50,height=40,fg_color="#b5520b",hover_color="#b5520b",bg_color="Black")
button4.place(x=190,y=120)

button5=ctk.CTkButton(root,command=lambda:show("7"),text="7",font=font_1,width=50,height=40,fg_color="#005b96",hover_color="#005b96",bg_color="Black")
button5.place(x=10,y=120)

button6=ctk.CTkButton(root,command=lambda:show("8"),text="8",font=font_1,width=50,height=40,fg_color="#005b96",hover_color="#005b96",bg_color="Black")
button6.place(x=70,y=120)

button7=ctk.CTkButton(root,command=lambda:show("9"),text="9",font=font_1,width=50,height=40,fg_color="#005b96",hover_color="#005b96",bg_color="Black")
button7.place(x=130,y=120)

button8=ctk.CTkButton(root,command=lambda:show("+"),text="+",font=font_1,width=50,height=40,fg_color="#b5520b",hover_color="#b5520b",bg_color="Black")
button8.place(x=190,y=180)

button9=ctk.CTkButton(root,command=lambda:show("4"),text="4",font=font_1,width=50,height=40,fg_color="#005b96",hover_color="#005b96",bg_color="Black")
button9.place(x=10,y=180)

button10=ctk.CTkButton(root,command=lambda:show("5"),text="5",font=font_1,width=50,height=40,fg_color="#005b96",hover_color="#005b96",bg_color="Black")
button10.place(x=70,y=180)

button11=ctk.CTkButton(root,command=lambda:show("6"),text="6",font=font_1,width=50,height=40,fg_color="#005b96",hover_color="#005b96",bg_color="Black")
button11.place(x=130,y=180)

button12=ctk.CTkButton(root,command=lambda:show("-"),text="-",font=font_1,width=50,height=40,fg_color="#b5520b",hover_color="#b5520b",bg_color="Black")
button12.place(x=190,y=240)

button13=ctk.CTkButton(root,command=lambda:show("0"),text="0",font=font_1,width=50,height=40,fg_color="#005b96",hover_color="#005b96",bg_color="Black")
button13.place(x=70,y=300)

button14=ctk.CTkButton(root,command=lambda:show("1"),text="1",font=font_1,width=50,height=40,fg_color="#005b96",hover_color="#005b96",bg_color="Black")
button14.place(x=10,y=240)

button15=ctk.CTkButton(root,command=lambda:show("2"),text="2",font=font_1,width=50,height=40,fg_color="#005b96",hover_color="#005b96",bg_color="Black")
button15.place(x=70,y=240)

button16=ctk.CTkButton(root,command=lambda:show("3"),text="3",font=font_1,width=50,height=40,fg_color="#005b96",hover_color="#005b96",bg_color="Black")
button16.place(x=130,y=240)

button17=ctk.CTkButton(root,command=lambda:show("."),text=".",font=font_1,width=50,height=40,fg_color="#005b96",hover_color="#005b96",bg_color="Black")
button17.place(x=10,y=300)

button18=ctk.CTkButton(root,command=calculate,text="=",font=font_1,width=110,height=40,fg_color="#7bc043",hover_color="#7bc043",bg_color="Black")
button18.place(x=130,y=300)


root.mainloop()
