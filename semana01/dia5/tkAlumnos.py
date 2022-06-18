from tkinter import  *
from tkinter.ttk import Treeview

class Alumno:

    def __init__(self,window):
        self.wind = window
        self.wind.title('CRUD DE ALUMNOS')
        self.wind.geometry('420x390')
        self.wind.configure(bg='#49A')

        #frame
        frame = LabelFrame(self.wind,text='Registro de nuevo Alumno')
        frame.grid(row=0,column=0,columnspan=3,pady=20,padx=20)

        #CAMPO NOMBRE
        lbNombre = Label(frame,text='Nombre : ')
        lbNombre.grid(row=1,column=0)
        self.nombre = Entry(frame)
        self.nombre.grid(row=1,column=1)

        #CAMPO EMAIL
        lbEmail = Label(frame,text='Email : ')
        lbEmail.grid(row=2,column=0)
        self.email = Entry(frame)
        self.email.grid(row=2,column=1)

        #BOTON
        btnNuevoAlumno = Button(frame,text='Insertar',command=self.registrarAlumno)
        btnNuevoAlumno.grid(row=4,columnspan=2,sticky=W+E)

        #TREVIEW
        self.TrvAlumnos = Treeview(height=10,columns=2)
        self.TrvAlumnos.grid(row=5,column=0,columnspan=2,padx=10)
        self.TrvAlumnos.heading('#0',text='Nombre',anchor=CENTER)
        self.TrvAlumnos.heading('#1',text='Email',anchor=CENTER)

    def registrarAlumno(self):
        self.TrvAlumnos.insert('',END,text=self.nombre.get(),values=[self.email.get()])

window = Tk()
app = Alumno(window)
window.mainloop()