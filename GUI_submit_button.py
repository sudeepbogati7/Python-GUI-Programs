from tkinter import *

#==========================================================================================
#                       Submit Buttton
#==========================================================================================
window = Tk()

window.title("SB - submit")
entry = Entry(window,
              font=('Comic Sans',30),
              fg='#00FF00',
              bg='black',
              show="*")
entry.pack(side=LEFT)

#-------------------submit button-------------------------

def submit():
    username = entry.get()
    print("Hello, "+username)
    entry.config(state=DISABLED)

submit_button = Button(window,
                       text='Submit',
                       command=submit
                       )
submit_button.pack(side=RIGHT)

#------------------------delete button ----------------------
def delete():
    entry.delete(0,END)


delete_button = Button(window,
                       text= 'delete',
                       command=delete)
delete_button.pack(side=RIGHT)

#-------------------- Backspace Button ---------------------------------

def backspace():
    entry.delete(len(entry.get())-1, END)

backspace_button = Button(window,
                          text="Backspace",
                          command=delete)
backspace_button.pack(side=RIGHT)
window.mainloop()