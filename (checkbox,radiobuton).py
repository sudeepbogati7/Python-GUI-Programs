from tkinter import *

window = Tk()
X = IntVar()
def display():
    if(X.get()==1):
        print("You agreed the statement !")
    else:
        print("You denied the statement!")

#photo = PhotoImage(file='img2.jpg')
check_button = Checkbutton(window,
                           text="I agree all the rules and regulations .",
                           command=display,
                           variable=X,
                           onvalue=1,
                           offvalue=0,
                           font=('Arial',20),
                           fg="#00FF00",
                           bg="black",
                           activeforeground="#00FF00",
                           activebackground="black",
                           padx=20,pady=20)
#                           image=photo,
#                           compound='left')
check_button.pack()

#*****************************************************************************************************
#                                  Radio_Buttons
#*****************************************************************************************************
label = Label(window,
              text="Select your Gender: ",
              font=("Sans Serif",15,"bold"))
label.pack(side="left")
options = ["Male","Female","Others"]
x = IntVar()

maleImage = PhotoImage(file='man.png')
femaleImage = PhotoImage(file='female.png')
otherImage = PhotoImage(file='other.png')

images= [maleImage,femaleImage,otherImage]
def order():
    if(x.get()==0):
        print("You are male.")
    elif(x.get()==1):
        print("you are female !")
    elif(x.get()==2):
        print("You selected others:(")
for index in range(len(options)):
    radio_button = Radiobutton(window,
                               text=options[index],   # add the text to the radio button
                               variable=x,  # groups the radio buttotns together if they share the same variable
                               value=index,    #assigns each radio button a different value
                               font=("Arial",12,),
                               padx=30,pady=20,   # adds padding
                               image=images[index],     #assigns images according to the index method
                               compound='left',        # adds image and text to the left/ left-side
                               indicatoron=0,
                               width=400,           #defines the width of the radio button
                               command=order        #connects order named funtion with the radio button
                               )
    radio_button.pack(side="left")
window.mainloop()