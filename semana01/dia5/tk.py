from tkinter import  *
from tkinter import messagebox

def saludar():
    print("Hola " + txtNombre.get())
    messagebox.showinfo("mensaje","Hola " + txtNombre.get())
app = Tk()
app.geometry('300x100')
app.title('César Mayta')
frame = LabelFrame(app,text='ventana')
frame.grid(row=0,column=0,columnspan=3,pady=20,padx=20)
#label
lbNombre = Label(frame,text='Nombre : ')
lbNombre.grid(row=1,column=0)
#caja de texto
txtNombre = Entry(frame)
txtNombre.grid(row=1,column=1)
#boton
btnSaludo = Button(frame,text='saludar',command=saludar)
btnSaludo.grid(row=1,column=2)
app.mainloop()