from tkinter import *
import tkinter

from functools import partial

Keyboard_App = tkinter.Tk()
Keyboard_App.title(" Visual Keyboard ")
Keyboard_App ['bg'] = 'blue'
Keyboard_App.resizable(0, 0)

def select(value):
    if value ==" Space ":
        entry.insert(tkinter.END,'  ')
    else:
        entry.insert(tkinter.END,value)

labell=Label(Keyboard_App,text='',bg='blue', fg="#000000").grid(row = 1,columnspan = 14) 
entry = Text(Keyboard_App, width=130)
entry.grid(row =2, columnspan = 20)


buttons = [
'q','w','e','r','t','y','u','i','o','<','>','7','8','9','-','_',
'a','s','d','f','g','h','j','k','l','[',']','4','5','6','+',
'.','x','c','v','b','n','m','z',',','?','"',';','1','2','3','/',
' Space ',
]


varRow = 3
varColumn = 0

for button in buttons:
    command = lambda x=button: select(x)
    if buttons != " Space ":
       tkinter.Button(Keyboard_App,text = button,width=5,fg="#ffffff",padx=3,pady=3,bd=12,bg ='blue',relief ='raised',
                      command=command).grid(row=varRow,column=varColumn )
    if buttons == " Space ":
       tkinter.Button(Keyboard_App,text = button,width=118,padx=4,pady=4,bd=4,bg ='blue',fg="#ffffff",relief ='raised',
                       command = command).grid(row = 6 ,column = 16)

    varColumn+=1
    if varColumn > 15 and varRow == 3:
        varColumn = 0
        varRow+=1
    if varColumn  > 15 and varRow == 4:
        varColumn = 0
        varRow+=1
        
Keyboard_App.mainloop()
                                                                                                               
