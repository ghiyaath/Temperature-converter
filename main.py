from tkinter import *
from tkinter import messagebox

window = Tk()
window.title('Temperature Convector')
window.minsize(width=500, height=500)
window.config(bg="aqua")
celcius_var= IntVar
fahrenheit_var =IntVar


l1=LabelFrame(window,text='Celcius To Fahrenheit',bg="yellow", fg="Black", borderwidth=5, font=("Arial 15 bold"), padx=20, pady=20)
l1.grid(row=2, column=0)
E1=Entry(l1,state='disable')
E1.grid(row=4, column=0)

#Activates celcuis to fahrenheit
def Cel_Active():
    E2.configure(state='disable')
    E1.configure(state='normal')

btn_active=Button(window,text='Activate -Celcius to Fahrenheit', bg="yellow", fg="Black", borderwidth=5, font=("Arial 15 bold"), command=Cel_Active)
btn_active.grid(row=6, column=0)

l2=LabelFrame(window, text='Fahrenheit to Celcius', bg="yellow", fg="Black", borderwidth=5, font=("Arial 15 bold"), padx=20, pady=20)
l2.grid(row=2, column=5)
E2=Entry(l2,state='disable')
E2.grid(row=4, column=5)

#Activates Fahrenheit to celcuis
def Far_Active():
    E1.configure(state='disable')
    E2.configure(state='normal')
btn_active1=Button(window,text='Activate -Fahrenheit to Celcius', bg="yellow", fg="Black", borderwidth=5, font=("Arial 15 bold"), command=Far_Active)
btn_active1.grid(row=6, column=5)


#exits
def exit():
    window.destroy()


exit_btn = Button(text = "Quit",bg="yellow", fg="Black", borderwidth=5, font=("Arial 15 bold"), command=exit)
exit_btn.place(x=500, y=250, height=70, width=80)
#converts celcuis to fahrenheit
def convert_C():
    if E1:
        try:
            celcius = float(E1.get())
            fahrenheit = (celcius*9/5)+32
            result_entry.insert(0, str(fahrenheit))
        except:
            messagebox.showinfo("ERROR", "Please insert correct data values")
            E1.delete(0, END)
#converts fahrenheit to celcuis
def convert_f():
    if E2:
        try:
            fahrenheit = float(E2.get())
            celcius = (fahrenheit-32)*5/9
            result_entry.insert(0, str(round(celcius,1)))
        except:
            messagebox.showinfo("ERROR", "Please insert correct data values")
            E2.delete(0, END)
#covert buttons
result_bnt=Button(window, text='Convert C-F', bg="yellow", fg="Black", borderwidth=5, font=("Arial 15 bold"), command=convert_C)
result_bnt.grid(row=7, column=2)

#results
result_bnt2=Button(window, text='Convert F-C',bg="yellow", fg="Black", borderwidth=5, font=("Arial 15 bold"), command=convert_f)
result_bnt2.grid(row=7, column=4)
result_entry=Entry(window, bg='light green')
result_entry.grid(row=8, column=2)

#clears content thats been put in
def Clear():
    E1.configure(state="disable")
    E2.configure(state="disable")
    E1.delete(0, END)
    E2.delete(0, END)
    result_entry.delete(0,END)
#clears content thats been put in
Clear_btn=Button(window, text='Clear', bg="yellow", fg="Black", borderwidth=5, font=("Arial 15 bold"), command=Clear)
Clear_btn.place(x=400, y=250, height=70, width=80)

window.mainloop()


