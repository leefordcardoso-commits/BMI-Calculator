import tkinter as tk
from tkinter import Frame, IntVar, Label, Tk,Button,Entry,Radiobutton

window=tk.Tk()
window.title("homework")
window.config(bg = "lightblue")

frame1= tk.Frame(window)
frame1.config(bg = "white")
frame1.grid(column=0,row=0, padx=20,pady=20)

frame2= tk.Frame(frame1)
frame2.config(bg = "white")
frame2.grid(column=0,row=0, padx=10,pady=10)



mainheading= tk.Label(frame2,text="Calculate your BMI",font=("Calibri bold", 24))
mainheading.config(bg = "light grey",fg="black",width=24,height=1)
mainheading.grid(column=0,row=0,columnspan=4)

headingKG= tk.Label(frame2,text="Enter your weight in kg\nto the right:"\
                    ,font=("Calibri bold", 12))
headingKG.config(bg = "light grey",fg="black",width=24,height=2)
headingKG.grid(column=0,row=1,columnspan=3,sticky="w",pady=10)

entry1= tk.Entry(frame2)
entry1.config(bg = "white",width=5,font=("Calibri bold", 26),justify="center")
entry1.grid(column=3,row=1, columnspan=2 ,pady=10,sticky="e")

headingHeight= tk.Label(frame2,text="Enter your height in Metres\nto the right:"\
                    ,font=("Calibri bold", 12))
headingHeight.config(bg = "light grey",fg="black",width=24,height=2)
headingHeight.grid(column=0,row=2,columnspan=3,sticky="w",pady=10)

entry2= tk.Entry(frame2)
entry2.config(bg = "white",width=5,font=("Calibri bold", 26),justify="center")
entry2.grid(column=3,row=2, columnspan=2 ,pady=10,sticky="e")

weightclass= tk.Label(frame2,font=("Calibri bold", 12))
weightclass.config(bg = "white",fg="black",width=30,height=2)
weightclass.grid(column=0,row=6,columnspan=5,pady=10,sticky="nsew")

headingBMI= tk.Label(frame2,text="Your BMI is:",font=("Calibri bold", 22))
headingBMI.config(bg = "white",fg="black",width=24,height=2)
headingBMI.grid(column=0,row=4,columnspan=4,pady=10)

heading_gender= tk.Label(frame2,text="Select your gender",font=("Calibri bold", 12))
heading_gender.config(bg = "light grey",fg="black",width=24,height=2)
heading_gender.grid(column=0,row=3,columnspan=4,pady=10,sticky="w")

def gender_color():
    if gender.get()==1:
        window.config(bg="light blue")
        mainheading.config(bg="light blue")
    elif gender.get()==2:
        window.config(bg="light pink")
        mainheading.config(bg="light pink")


        

gender= IntVar()

gender_male=Radiobutton(frame2,text="Male",variable=gender,value=1,\
                   font=("Calibri bold", 12),command=gender_color,bg="white")
gender_male.grid(column=2,row=3,sticky="e")

gender_female=Radiobutton(frame2,text="Female",variable=gender,value=2,\
                   font=("Calibri bold", 12),command=gender_color,bg="white")
gender_female.grid(column=3,row=3,sticky="e")



def BMI_and_check():

    if entry1.get()=="" or entry2.get()=="":
        weightclass.config(text="You have missing information")
    else:
        weightclass.config(text="")

    BMI=round(float(entry1.get())/float(entry2.get())**2,2)
    headingBMI.config(text="Your BMI is: "+str(BMI))

    if BMI<20:
        weightclass.config(text="This means that You are underweight")
    elif BMI>=20 and BMI<25:
        weightclass.config(text="This means that You are in the healthy weight range")
    elif BMI>=25:
        weightclass.config(text="This means that You are obese")



button= tk.Button(frame2,text="Press to find\nyour BMI",\
                 command=BMI_and_check,\
                    font=("Calibri bold", 12))
button.config(bg = "dark blue", fg="white",width=14,height=2)
button.grid(column=0,row=5, columnspan=4 ,pady=10)


window.mainloop()