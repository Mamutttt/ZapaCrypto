import tkinter
from tkinter import *
import easygui
from SyL import *
from Conexion_BDD_V2 import BDD
############ holis 2
# command = lambda:[<nombre función1(), <nombre función2()]

ventana = Tk()
ventana.geometry("900x600")


def Atrás(ventana_a_cerrar):
    ventana_a_cerrar.destroy()
    ventana.deiconify()


def StockYLogística():
    SYL = Tk()
    SYL.geometry("900x600")
    SYL.configure(bg="pink")
    SYL.title("Stock y Logística")

    BSYL = tkinter.Button(SYL, text="Volver", command=lambda: [Atrás(SYL), ()])
    BSYL.place(x=850, y=5)

    ASYL = tkinter.Button(SYL, text="Stock Y \nLogística", height=5, width=12, command=lambda: [])
    ASYL.place(x=30, y=100)

    AVYC = tkinter.Button(SYL, text="Ventas Y \nClientes", height=5, width=12, command=lambda: [VentasYClientes(), SYL.withdraw()])
    AVYC.place(x=30, y=200)

    ACYP = tkinter.Button(SYL, text="Compras Y \nProveedores", height=5, width=12, command=lambda: [ComprasYProveedores(), SYL.withdraw()])
    ACYP.place(x=30, y=300)

    ACONT = tkinter.Button(SYL, text="Contabilidad", height=5, width=12, command=lambda: [Contabilidad(), SYL.withdraw()])
    ACONT.place(x=30, y=400)

    B1SYL = tkinter.Button(SYL, text="Funcionalidad 1  ", command=lambda: [Fun1SYL(),])
    B1SYL.place(x=150, y=50)

    B2SYL = tkinter.Button(SYL, text="Funcionalidad 2  ", command="")
    B2SYL.place(x=150, y=75)

    B3SYL = tkinter.Button(SYL, text="Funcionalidad 3  ", command="")
    B3SYL.place(x=150, y=100)

    B4SYL = tkinter.Button(SYL, text="Funcionalidad 4  ", command="")
    B4SYL.place(x=150, y=125)

    B5SYL = tkinter.Button(SYL, text="Funcionalidad 5  ", command="")
    B5SYL.place(x=150, y=150)

    B6SYL = tkinter.Button(SYL, text="Funcionalidad 6  ", command="")
    B6SYL.place(x=150, y=175)

    B7SYL = tkinter.Button(SYL, text="Funcionalidad 7  ", command="")
    B7SYL.place(x=150, y=200)

    B8SYL = tkinter.Button(SYL, text="Funcionalidad 8  ", command="")
    B8SYL.place(x=150, y=225)

    B9SYL = tkinter.Button(SYL, text="Funcionalidad 9  ", command="")
    B9SYL.place(x=150, y=250)

    B10SYL = tkinter.Button(SYL, text="Funcionalidad 10", command="")
    B10SYL.place(x=150, y=275)

    B11SYL = tkinter.Button(SYL, text="Funcionalidad 11", command="")
    B11SYL.place(x=150, y=300)

    B12SYL = tkinter.Button(SYL, text="Funcionalidad 12", command="")
    B12SYL.place(x=150, y=325)

    B13SYL = tkinter.Button(SYL, text="Funcionalidad 13", command="")
    B13SYL.place(x=150, y=350)

    B14SYL = tkinter.Button(SYL, text="Funcionalidad 14", command="")
    B14SYL.place(x=150, y=375)

    B15SYL = tkinter.Button(SYL, text="Funcionalidad 15", command="")
    B15SYL.place(x=150, y=400)

    B16SYL = tkinter.Button(SYL, text="Funcionalidad 16", command=lambda: [(), ()])
    B16SYL.place(x=150, y=425)

    ventana.withdraw()

def Fun1SYL():
    F1SYL = Tk()
    F1SYL.geometry("900x600")
    F1SYL.title("Función 1")

def registrarCompra():
    pass

def mostrarArticulos():

    VentanaArt=Tk()
    VentanaArt.geometry("1000x700")
    VentanaArt.configure(bg="pink")
    Articulos=Listbox(VentanaArt,height=30,width=50)
    Articulos.place(x=20,y=33)

    BVYC = tkinter.Button(VentanaArt, text="Volver", command=lambda: [Atrás(VentanaArt)])
    BVYC.place(x=950, y=5)

    Labelart=Label(VentanaArt,text="ID", bg="PINK",font=("Helvetica",14))
    Labelart.place(x=15,y=5)
    Labelart3=Label(VentanaArt,text="Lista de articulos", bg="PINK",font=("Helvetica",14))
    Labelart3.place(x=40,y=5)
#Meter articulos en la lista
    bdd = BDD()
    conexion = bdd.conexion_bdd()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM Articulo")
    respuesta = cursor.fetchall()
    for x in respuesta:
        Articulos.insert(END, x)

    Labelart2=Label(VentanaArt,text="Eliga ID de articulos a comprar", bg="PINK",font=("Helvetica",14))
    Labelart2.place(x=350,y=40)
    Labelart4=Label(VentanaArt,text="(separado por comas)", bg="PINK",font=("Helvetica",8))
    Labelart4.place(x=616,y=46)

    Entryvyc=Entry(VentanaArt,text="...",width=50)
    Entryvyc.place(x=350,y=70)
    botonCompra=Button(VentanaArt,text="Comprar",command=registrarCompra,font=("Helvetica",18))
    botonCompra.place(x=430,y=110)



def atencionAlCliente():
    easygui.msgbox("Para comunicarse con atencion al cliente, comunicarse con: 11 2561-1025", title="Atencion al cliente")


def VentasYClientes():
    VYC = Tk()
    VYC.geometry("900x600")
    VYC.configure(bg="pink")
    VYC.title("Ventas y Clientes")



    BVYC = tkinter.Button(VYC, text="Volver", command=lambda: [Atrás(VYC), ()])
    BVYC.place(x=850, y=5)
    ASYL = tkinter.Button(VYC, text="Stock Y \nLogística", height=5, width=12, command=lambda: [StockYLogística(), VYC.withdraw()])
    ASYL.place(x=30, y=100)
    AVYC = tkinter.Button(VYC, text="Ventas Y \nClientes", height=5, width=12, command=lambda: [])
    AVYC.place(x=30, y=200)
    ACYP = tkinter.Button(VYC, text="Compras Y \nProveedores", height=5, width=12, command=lambda: [ComprasYProveedores(), VYC.withdraw()])
    ACYP.place(x=30, y=300)
    ACONT = tkinter.Button(VYC, text="Contabilidad", height=5, width=12, command=lambda: [Contabilidad(), VYC.withdraw()])
    ACONT.place(x=30, y=400)

    #banner = PhotoImage(file=r"Fotos/VYCbanner.png")
    #imgbanner = Button(VYC, image=banner, command=mostrarArticulos)
    #imgbanner.place(x=650, y=300)


    B1VYC = tkinter.Button(VYC, text="Mostrar articulos ",font=("Helvetica",36), command=lambda: [mostrarArticulos(),])
    B1VYC.place(x=300, y=200)

    B2VYC = tkinter.Button(VYC, text="Atencion al cliente  ",font=("Helvetica",13), command=lambda:[atencionAlCliente()])
    B2VYC.place(x=700, y=550)





    #B16VYC = tkinter.Button(VYC, text="Funcionalidad 16", command=lambda: [(), ()])
    #B16VYC.place(x=150, y=425)

    ventana.withdraw()


def ComprasYProveedores():
    CYP = Tk()
    CYP.geometry("900x600")
    CYP.title("Compras y Proveedores")

    BCYP = tkinter.Button(CYP, text="Volver", command=lambda: [Atrás(CYP), ()])
    BCYP.place(x=850, y=5)

    ASYL = tkinter.Button(CYP, text="Stock Y \nLogística", height=5, width=12, command=lambda: [StockYLogística(), CYP.withdraw()])
    ASYL.place(x=30, y=100)

    AVYC = tkinter.Button(CYP, text="Ventas Y \nClientes", height=5, width=12, command=lambda: [VentasYClientes(), CYP.withdraw()])
    AVYC.place(x=30, y=200)

    ACYP = tkinter.Button(CYP, text="Compras Y \nProveedores", height=5, width=12, command=lambda: [])
    ACYP.place(x=30, y=300)

    ACONT = tkinter.Button(CYP, text="Contabilidad", height=5, width=12, command=lambda: [Contabilidad(), CYP.withdraw()])
    ACONT.place(x=30, y=400)

    B1CYP = tkinter.Button(CYP, text="Funcionalidad 1  ", command=lambda: [Proveedores(),])
    B1CYP.place(x=150, y=50)

    B2CYP = tkinter.Button(CYP, text="Funcionalidad 2  ", command="")
    B2CYP.place(x=150, y=75)

    B3CYP = tkinter.Button(CYP, text="Funcionalidad 3  ", command="")
    B3CYP.place(x=150, y=100)

    B4CYP = tkinter.Button(CYP, text="Funcionalidad 4  ", command="")
    B4CYP.place(x=150, y=125)

    B5CYP = tkinter.Button(CYP, text="Funcionalidad 5  ", command="")
    B5CYP.place(x=150, y=150)

    B6CYP = tkinter.Button(CYP, text="Funcionalidad 6  ", command="")
    B6CYP.place(x=150, y=175)

    B7CYP = tkinter.Button(CYP, text="Funcionalidad 7  ", command="")
    B7CYP.place(x=150, y=200)

    B8CYP = tkinter.Button(CYP, text="Funcionalidad 8  ", command="")
    B8CYP.place(x=150, y=225)

    B9CYP = tkinter.Button(CYP, text="Funcionalidad 9  ", command="")
    B9CYP.place(x=150, y=250)

    B10CYP = tkinter.Button(CYP, text="Funcionalidad 10", command="")
    B10CYP.place(x=150, y=275)

    B11CYP = tkinter.Button(CYP, text="Funcionalidad 11", command="")
    B11CYP.place(x=150, y=300)

    B12CYP = tkinter.Button(CYP, text="Funcionalidad 12", command="")
    B12CYP.place(x=150, y=325)

    B13CYP = tkinter.Button(CYP, text="Funcionalidad 13", command="")
    B13CYP.place(x=150, y=350)

    B14CYP= tkinter.Button(CYP, text="Funcionalidad 14", command="")
    B14CYP.place(x=150, y=375)

    B15CYP = tkinter.Button(CYP, text="Funcionalidad 15", command="")
    B15CYP.place(x=150, y=400)

    B16CYP = tkinter.Button(CYP, text="Funcionalidad 16", command=lambda: [])
    B16CYP.place(x=150, y=425)


    # CYP.configure(bg="pink")
    # FondoB = tkinter.PhotoImage(file=r"C:\Users\Ryzen\PycharmProjects\ProyectoFinalDesarrollo\FondoBlanco.png")
    # FondoIMG = tkinter.Label(CYP, image=FondoB)
    # FondoIMG.pack()
    # background = Label(text="Imagen S.O de fondo")
    # background.place(x=0, y=0, relwidth=1, relheight=1)
    # FCYP = tkinter.PhotoImage(file="FondoBlanco.png")
    # FICYP = tkinter.Label(CYP, image=FCYP)
    # FICYP.place(x=350, y=150)

    # ronconcola = PhotoImage(master=CYP, file=r"C:\Users\Ryzen\Desktop\asdasdasdasdasdasdasdasdasda.png")
    # imagen = Label(CYP, image=ronconcola)
    # imagen.place(x=0, y=0)

    # SYL = PhotoImage(file=r"C:\Users\Ryzen\Desktop\ASD.png")
    # IMG1 = Button(CYP, image=SYL, borderwidth=0)
    # IMG1.place(x=170, y=400)

    LogoEti = Label(CYP, text="Administra tu empresa").place(x=390, y=310)


    #LogoSD = tkinter.PhotoImage(file=r"C:\Users\Ryzen\Desktop\Logo.PNG")
    #LogoIMGASD = tkinter.Label(CYP, image=LogoSD)
    #LogoIMGASD.place(x=350, y=100)

    ventana.withdraw()

def Proveedores():
    Prov = Tk()
    Prov.geometry("900x600")
    Prov.title("Compras y Proveedores")


def Contabilidad():
    CONT = Tk()
    CONT.geometry("900x600")
    CONT.configure(bg="pink")
    CONT.title("Contabilidad")

    BCONT = tkinter.Button(CONT, text="Volver", command=lambda: [Atrás(CONT), ()])
    BCONT.place(x=850, y=5)


    ASYL = tkinter.Button(CONT, text="Stock Y \nLogística", height=5, width= 12, command=lambda: [StockYLogística(), CONT.withdraw()])
    ASYL.place(x=30, y=100)

    AVYC = tkinter.Button(CONT, text="Ventas Y \nClientes", height=5, width= 12, command=lambda: [VentasYClientes(), CONT.withdraw()])
    AVYC.place(x=30, y=200)

    ACYP = tkinter.Button(CONT, text="Compras Y \nProveedores", height=5, width= 12, command=lambda: [ComprasYProveedores(), CONT.withdraw()])
    ACYP.place(x=30, y=300)

    ACONT = tkinter.Button(CONT, text="Contabilidad", height=5, width=12, command=lambda: [])
    ACONT.place(x=30, y=400)


    B1CONT = tkinter.Button(CONT, text="Funcionalidad 1  ", command=lambda: [Fun1Contabilidad(),])
    B1CONT.place(x=150, y=50)

    B2CONT = tkinter.Button(CONT, text="Funcionalidad 2  ", command="")
    B2CONT.place(x=150, y=75)

    B3CONT = tkinter.Button(CONT, text="Funcionalidad 3  ", command="")
    B3CONT.place(x=150, y=100)

    B4CONT = tkinter.Button(CONT, text="Funcionalidad 4  ", command="")
    B4CONT.place(x=150, y=125)

    B5CONT = tkinter.Button(CONT, text="Funcionalidad 5  ", command="")
    B5CONT.place(x=150, y=150)

    B6CONT = tkinter.Button(CONT, text="Funcionalidad 6  ", command="")
    B6CONT.place(x=150, y=175)

    B7CONT = tkinter.Button(CONT, text="Funcionalidad 7  ", command="")
    B7CONT.place(x=150, y=200)

    B8CONT = tkinter.Button(CONT, text="Funcionalidad 8  ", command="")
    B8CONT.place(x=150, y=225)

    B9CONT = tkinter.Button(CONT, text="Funcionalidad 9  ", command="")
    B9CONT.place(x=150, y=250)

    B10CONT = tkinter.Button(CONT, text="Funcionalidad 10", command="")
    B10CONT.place(x=150, y=275)

    B11CONT = tkinter.Button(CONT, text="Funcionalidad 11", command="")
    B11CONT.place(x=150, y=300)

    B12CONT = tkinter.Button(CONT, text="Funcionalidad 12", command="")
    B12CONT.place(x=150, y=325)

    B13CONT = tkinter.Button(CONT, text="Funcionalidad 13", command="")
    B13CONT.place(x=150, y=350)

    B14CONT = tkinter.Button(CONT, text="Funcionalidad 14", command="")
    B14CONT.place(x=150, y=375)

    B15CONT = tkinter.Button(CONT, text="Funcionalidad 15", command="")
    B15CONT.place(x=150, y=400)

    B16CONT = tkinter.Button(CONT, text="Funcionalidad 16", command=lambda: [(), ()])
    B16CONT.place(x=150, y=425)


    #hj = tkinter.Button(CONT, text="asd", borderwidth=0, command=StockYLogística)
    #hj.place(x=400, y=400)

    ventana.withdraw()

def Fun1Contabilidad():
    F1C = Tk()
    F1C.geometry("900x600")
    F1C.title("Función 1")


Fondo = tkinter.PhotoImage(file="Fotos/Fondo.png")
# FondoIMG = tkinter.Label(ventana, image=Fondo)
# FondoIMG.pack()
background = Label(image=Fondo, text="Imagen S.O de fondo")
background.place(x=0, y=0, relwidth=1, relheight=1)

Logo = tkinter.PhotoImage(file=r"Fotos/Logo.PNG")
LogoIMG = tkinter.Label(ventana, image=Logo)
LogoIMG.place(x=350, y=100)
Label(text="Administra tu empresa").place(x=390, y=310)

Label(text="Usuario"). place(x=350, y=400)
entry1 = Entry(ventana, width=20)
entry1.place(x=350,y=425)

Label(text="Contraseña"). place (x=350, y=460)
Contraseña = Entry(ventana, width=20)
Contraseña.place(x=350,y=485)

Ingresar = Button(text="Ingresar")
Ingresar.place(x=385, y=510)

SYL = PhotoImage(file=r"Fotos/StockYLogística.png")
IMG1 = Button(ventana, image=SYL, borderwidth=0, command=StockYLogística)
IMG1.place(x=150, y=150)
Label(text="Stock y Logística").place(x=150, y=260)

VYC = PhotoImage(file=r"Fotos/VentasYClientes.png")
IMG2 = Button(ventana, image=VYC, borderwidth=0, command=VentasYClientes)
IMG2.place(x=150, y=300)
Label(text="Ventas y Clientes").place(x=150, y=410)

CYP = PhotoImage(file=r"Fotos/ComprasYProveedores.png")
IMG3 = Button(ventana, image=CYP, borderwidth=0, command=ComprasYProveedores)
IMG3.place(x=650, y=150)
Label(text="Compras y Proveedores").place(x=650, y=260)

CONT = PhotoImage(file=r"Fotos/Contabilidad.png")
IMG4 = Button(ventana, image=CONT, borderwidth=0, command=Contabilidad)
IMG4.place(x=650, y=300)
Label(text="Contabilidad").place(x=650, y=410)

ventana.mainloop()

