# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 16:05:59 2021
@author: Uday Kiran
"""
from tkinter import * 

root = Tk() 
root.title("Calculator") 
first_operand = 0.0
second_operand = 0.0
symbol = str()  

def evaluate() : 
    global first_operand 
    global second_operand
    global symbol 
    if symbol == '+' : 
        return first_operand + second_operand 
    elif symbol == '-' : 
        return first_operand - second_operand 
    elif symbol == '/' : 
        return first_operand / second_operand 
    elif symbol == '*' : 
        return first_operand * second_operand 
    elif symbol == '%': 
        return first_operand % second_operand
        

def Done() : 
    global second_operand
    second_operand = float(e.get()) 
    clear_event()
    res = evaluate() 
    e.insert(0,str(res))
    
def op_click(op) : 
    global symbol 
    global first_operand
    symbol = op
    first_operand = float(e.get())
    clear_event() 
    
def my_click(n) : 
    current = e.get() 
    e.delete(0,END)
    e.insert(0,current+str(n)) 
    
def clear_event() :
    e.delete(0,END)
    
   
    
e = Entry(root,width=40,borderwidth = 5,font = 15) 


button_1 = Button(root,text = "1",padx = 40,pady = 20,command = lambda : my_click(1)) 
button_2 = Button(root,text = "2",padx = 40,pady = 20,command = lambda : my_click(2)) 
button_3 = Button(root,text = "3",padx = 40,pady = 20,command = lambda : my_click(3)) 


button_4 = Button(root,text = "4",padx = 40,pady = 20,command = lambda : my_click(4)) 
button_5 = Button(root,text = "5",padx = 40,pady = 20,command = lambda : my_click(5)) 
button_6 = Button(root,text = "6",padx = 40,pady = 20,command = lambda : my_click(6)) 


button_7 = Button(root,text = "7",padx = 40,pady = 20,command = lambda : my_click(7)) 
button_8 = Button(root,text = "8",padx = 40,pady = 20,command = lambda : my_click(8)) 
button_9 = Button(root,text = "9",padx = 40,pady = 20,command = lambda : my_click(9)) 
 
button_clear = Button(root,text = "clr",padx = 40,pady = 20,command = clear_event) 
button_0 = Button(root,text = "0",padx = 40,pady = 20,command = lambda : my_click(0)) 
button_dot = Button(root,text = ".",padx = 40,pady = 20,command = lambda : my_click('.')) 

button_add = Button(root,text = "+",padx = 40,pady = 20,command = lambda : op_click('+')) 
button_sub = Button(root,text = "-",padx = 40,pady = 20,command = lambda : op_click('-')) 
button_mul = Button(root,text = "*",padx = 40,pady = 20,command = lambda : op_click('*')) 
button_div = Button(root,text = "/",padx = 40,pady = 20,command = lambda : op_click('/')) 
button_done = Button(root,text = "Dn",padx = 40,pady = 20,command = Done)

button_mod = Button(root,text = "%",padx = 40,pady = 20,command = lambda : op_click('%')) 


e.grid(row = 0,column = 0,columnspan = 30)
button_1.grid(row = 3 ,column =0) 
button_2.grid(row = 3,column = 1)
button_3.grid(row = 3,column = 2)
button_4.grid(row = 2,column = 0)
button_5.grid(row = 2,column = 1)
button_6.grid(row = 2,column = 2)
button_7.grid(row = 1,column =0)
button_8.grid(row = 1,column = 1)
button_9.grid(row = 1,column = 2)


button_mod.grid(row = 4,column = 0)
button_0.grid(row = 4,column = 1)
button_dot.grid(row =4 ,column =2 )
button_add.grid(row = 4,column = 4)
button_sub.grid(row = 3,column = 4)
button_mul.grid(row = 2,column = 4)
button_div.grid(row = 1,column =4 )

button_done.grid(row = 5,column = 0)
button_clear.grid(row = 5,column = 1 )












root.mainloop()
