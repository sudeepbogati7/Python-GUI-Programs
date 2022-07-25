#---------------------------------------------------------------------------------------------------
#                               Creating Graphical User Interface
#---------------------------------------------------------------------------------------------------

from tkinter import *

window = Tk()   #instanciate an instance of a window
#window.geometry("700x700")      #defines height and width
window.title("Sudeep Bogati First GUI program ")

#-----------icon----------------------

icon = PhotoImage(file='logo.png')
window.iconphoto(True,icon)

#----------End Logo Icon ---------------

#-------backgroud_color-------------
#window.config(background="black")

#---------- label -----------------------------
photo = PhotoImage(file='image.png')
label = Label(window,
              text= "Hey ! This is me Sudeep ",
              font=('Arial',30,'bold'),
              fg='#00FF00',
              bg='black',
              relief=RAISED,
              bd=20,
              padx=20,
              pady=20,
              image=photo,
              compound='bottom')
label.pack()

#--------------End level --------------

#-------------------Button -------------------
count = 0

def click():
    global count
    count += 1
    print("You clicked the button ", count, "times!" )

button = Button(window,
                text="Click Me ! ",
                font=('Comic Sans',15,'bold'),
                command=click,
                fg='#00FF00',
                bg='black',
                )
button.pack()


window .mainloop()      #places window on computer screen


