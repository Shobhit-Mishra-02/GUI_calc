# author : Shobhit Mishra
# Here I have created a calculator with the help of tkinter tool-kit.
# This GUI will perform addition, subtraction, multiplication ,division , power


from tkinter import *
from tkinter import ttk

#creating calculator.

class calculator_gui:
    def __init__(self, width, height):
        self.win=Tk()
        self.win.geometry(f"{width}x{height}")
        self.win.minsize(width,height)
        self.win.maxsize(width,height)
        self.win.wm_iconbitmap("2.ico")
        self.win.title("Calculator")
        self.f_1=Frame(self.win)
        self.f_2=Frame(self.win)
        self.var_entry=StringVar()
        self.text_on_screen=""
        
    #creating the entry widget for showing the result.
    def entry_window(self):
        self.f_1.pack(side=TOP, fill=X)
        entry=Entry(self.f_1, textvariable=self.var_entry, font="helvertica 24 bold", state="readonly",
                    borderwidth=4, relief="sunken")
        entry.pack(fill=X)

    #creating the button and processing of the equations.
    def buttons_calculation(self):
        
        def click(event):#processing the given numbers
            x=event.widget.cget("text")
            
            if x=="c":
                self.text_on_screen=""
                self.var_entry.set(self.text_on_screen)
            elif x=="=":
                try:
                    self.var_entry.set(eval(self.text_on_screen))
                except:
                    pass
            else:
                self.text_on_screen = self.text_on_screen + x
                self.var_entry.set(self.text_on_screen)

        #creating the buttons 
        #Here I am using a list button_lt to store the text of each button
        self.f_2.pack(side=TOP, fill=BOTH)
        button_lt=[["1","2","3"],["4","5","6"],["7","8","9"],["0","-","**"],["+","/","*"],[".","=","c"]]

        for i in range(len(button_lt)):
            lt = button_lt[i]
            for j in range(len(lt)):
                b=Button(self.f_2, text=f"{lt[j]}", font="lucida 15 bold", width=11, bg="#ae5e5e",
                        activebackground="#ff0f0f", borderwidth=3, relief="raised" )
                b.grid(row=i, column=j, stick="nwes")
                b.bind("<Button-1>", click)
                
    #This will end the loop
    def end(self):
        self.win.mainloop()




#Here I have created the calculator
if __name__=="__main__":
    cal=calculator_gui(432,311)
    cal.entry_window()
    cal.buttons_calculation()
    cal.end()