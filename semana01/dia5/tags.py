import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=605
        height=497
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_312=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_312["font"] = ft
        GLabel_312["fg"] = "#333333"
        GLabel_312["justify"] = "center"
        GLabel_312["text"] = "Nombre"
        GLabel_312.place(x=30,y=30,width=70,height=25)

        GLineEdit_920=tk.Entry(root)
        GLineEdit_920["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_920["font"] = ft
        GLineEdit_920["fg"] = "#333333"
        GLineEdit_920["justify"] = "center"
        GLineEdit_920["text"] = "Entry"
        GLineEdit_920.place(x=130,y=30,width=160,height=30)

        GLabel_65=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_65["font"] = ft
        GLabel_65["fg"] = "#333333"
        GLabel_65["justify"] = "center"
        GLabel_65["text"] = "label"
        GLabel_65.place(x=20,y=80,width=70,height=25)

        GLineEdit_362=tk.Entry(root)
        GLineEdit_362["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_362["font"] = ft
        GLineEdit_362["fg"] = "#333333"
        GLineEdit_362["justify"] = "center"
        GLineEdit_362["text"] = "Entry"
        GLineEdit_362.place(x=130,y=80,width=159,height=30)

        GRadio_577=tk.Radiobutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GRadio_577["font"] = ft
        GRadio_577["fg"] = "#333333"
        GRadio_577["justify"] = "center"
        GRadio_577["text"] = "RadioButton"
        GRadio_577.place(x=40,y=150,width=85,height=25)
        GRadio_577["command"] = self.GRadio_577_command

        GCheckBox_745=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_745["font"] = ft
        GCheckBox_745["fg"] = "#333333"
        GCheckBox_745["justify"] = "center"
        GCheckBox_745["text"] = "CheckBox"
        GCheckBox_745.place(x=40,y=200,width=70,height=25)
        GCheckBox_745["offvalue"] = "0"
        GCheckBox_745["onvalue"] = "1"
        GCheckBox_745["command"] = self.GCheckBox_745_command

        GButton_904=tk.Button(root)
        GButton_904["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_904["font"] = ft
        GButton_904["fg"] = "#000000"
        GButton_904["justify"] = "center"
        GButton_904["text"] = "Button"
        GButton_904.place(x=50,y=260,width=70,height=25)
        GButton_904["command"] = self.GButton_904_command

        GListBox_312=tk.Listbox(root)
        GListBox_312["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GListBox_312["font"] = ft
        GListBox_312["fg"] = "#333333"
        GListBox_312["justify"] = "center"
        GListBox_312.place(x=350,y=30,width=80,height=25)

    def GRadio_577_command(self):
        print("command")


    def GCheckBox_745_command(self):
        print("command")


    def GButton_904_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
