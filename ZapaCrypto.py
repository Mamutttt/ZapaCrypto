from tkinter import *

############ holis 2

def StockYLogística():
    SYL=Tk()
    SYL.geometry("1920x1080")   
    SYL.configure(bg="pink")

    SYL.mainloop()

def VentasYClientes():
    VYC=Tk()
    VYC.geometry("1920x1080")   
    VYC.configure(bg="pink")
    print("actualizacion4")
    VYC.mainloop()

def ComprasYProveedores():
    CYP=Tk()
    CYP.geometry("1920x1080")   
    CYP.configure(bg="blue")

    BCYP = Button(CYP, text="ComprasYProveedores", height=5, width=30)
    BCYP.place(x=400, y=10)
    BCYP
    
    CYP.mainloop()

def Contabilidad():
    CONT=Tk()
    CONT.geometry("1920x1080")   
    CONT.configure(bg="pink")

    CONT.mainloop()

ventana = Tk()
ventana.geometry("1920x1080")

SYL = PhotoImage(file ="C:/Users/Ryzen/Desktop/ASD.png") 
IMG1 = Button(ventana, image = SYL, borderwidth = 0, command=StockYLogística)   
IMG1.place(x=125, y=300)

user_name = Label(text = "Stock y Logística").place(x = 155, y = 515)

VYC = PhotoImage(file ="C:/Users/Ryzen/Desktop/ASD.png") 
IMG2 = Button(ventana, image = VYC, borderwidth = 0, command=VentasYClientes)   
IMG2.place(x=425, y=300)

user_name = Label(text = "Ventas y Clientes").place(x = 455, y = 515)

CYP = PhotoImage(file ="C:/Users/Ryzen/Desktop/ASD.png") 
IMG3 = Button(ventana, image = CYP, borderwidth = 0, command=ComprasYProveedores)   
IMG3.place(x=725, y=300)


user_name = Label(text = "Compras y Proveedores").place(x = 755, y = 515)

CONT = PhotoImage(file ="C:/Users/Ryzen/Desktop/ASD.png") 
IMG4 = Button(ventana, image = CONT, borderwidth = 0, command=Contabilidad)   
IMG4.place(x=1025, y=300)

user_name = Label(text = "Contabilidad").place(x = 1055, y = 515)


ventana.mainloop()
