import easygui

import tkinter
from tkinter import *

from tkinter import ttk
from tkinter import messagebox 
import tkinter.font as tkFont
from PIL import ImageTk, Image

import warnings

from functools import partial

from Conexion_BDD_V2 import BDD
from SyL import *

############ holis 2
# command = lambda:[<nombre función1(), <nombre función2()]


class Entorno_Grafico():
    
    def __init__(self):
        #Pantalla de inicio
        self.ventana = Tk()
        self.ventana.geometry("900x600")
        self.ventana.title("ZapaCrypto61")
        self.ventana.iconbitmap("Fotos/Logo.ico")
        
        Fondo = tkinter.PhotoImage(file="Fotos/Fondo.png")
        
        background = Label(image=Fondo, text="Imagen S.O de fondo")
        background.place(x=0, y=0, relwidth=1, relheight=1)

        Logo = tkinter.PhotoImage(file=r"Fotos/Logo.PNG")
        LogoIMG = tkinter.Label(self.ventana, image=Logo)
        LogoIMG.place(x=350, y=100)
        Label(text="Administra tu empresa").place(x=390, y=310)
        
        fontStyle = tkFont.Font(family="Bell Gothic Std Black", size=10)
     
        #Botones
        imagen_boton = Image.open("imagen_boton_low.png")
        imagen_ajustada = imagen_boton.resize((130,70), Image.ANTIALIAS)
        self.imagen_final = ImageTk.PhotoImage(imagen_ajustada)
        
        btn_inicio = Button(self.ventana,
                            image=self.imagen_final,
                            bg = "#1c1f50", borderwidth=0,
                            font=fontStyle, fg = "black",
                            text = "Iniciar sesión", compound='center',
                            command= self.CargarInicio)
        
        btn_inicio.place(x=300, y=350)
        
        btn_registro = Button(self.ventana,
                              image=self.imagen_final,
                              bg = "#1c1f50", borderwidth=0,
                              font=fontStyle, fg = "black",
                              text = "Registrarse", compound='center',
                              command= self.CargarRegistro)
        
        btn_registro.place(x=470, y=350)

        
        SYL = PhotoImage(file=r"Fotos/StockYLogística.png")
        IMG1 = Button(self.ventana, image=SYL, borderwidth=0, command=self.StockYLogística)
        IMG1.place(x=150, y=150)
        Label(text="Stock y Logística").place(x=150, y=260)

        VYC = PhotoImage(file=r"Fotos/VentasYClientes.png")
        IMG2 = Button(self.ventana, image=VYC, borderwidth=0, command=self.VentasYClientes)
        IMG2.place(x=150, y=300)
        Label(text="Ventas y Clientes").place(x=150, y=410)

        CYP = PhotoImage(file=r"Fotos/ComprasYProveedores.png")
        IMG3 = Button(self.ventana, image=CYP, borderwidth=0, command=self.ComprasYProveedores)
        IMG3.place(x=650, y=150)
        Label(text="Compras y Proveedores").place(x=650, y=260)

        CONT = PhotoImage(file=r"Fotos/Contabilidad.png")
        IMG4 = Button(self.ventana, image=CONT, borderwidth=0, command=self.Contabilidad)
        IMG4.place(x=650, y=300)
        Label(text="Contabilidad").place(x=650, y=410)


        #Instancia de capa de archivos compartida
        self.obj_conexion = BDD()
        self.conexion = self.obj_conexion.conectar_bdd()

        #Listado de mensajes a imprimir según el resultado de la validación
        self.mensajes = ["Se produjo un error en la validación."
                        ,"El usuario no existe."
                        ,"La contraseña es incorrecta."
                        ,"Ingreso correcto. Bienvenido al sistema."]
        
        
        self.ventana.mainloop()
        
        
    def Atrás(self, ventana_a_cerrar):
        ventana_a_cerrar.destroy()
        self.ventana.deiconify()

        
    def validar_ingresos(self, labels, lista):
        vacios = []
        for i in range(0, len(lista)):
            if not lista[i]:
                vacios.append(labels[i])

        return vacios

#Sesión de usuario
    def CargarInicio(self):
        #Ventana de inicio
        ventanaI = Toplevel()
        ventanaI.geometry("300x225")
        ventanaI.configure(bg="BLUE")
        ventanaI.title("ZapaCrypto61 - Login")
        
        ventanaI.iconbitmap("Fotos/Logo.ico")

        #Detalles de usuario
        lbl_usuario = Label(ventanaI,
                            bg = "CYAN", borderwidth=0,
                            font=('Helvetica', 12),
                            #font=fontStyle, fg = "black",
                            text = "Usuario: ")
        lbl_usuario.place(x=60, y=40)

        self.txt_usuario = Text(ventanaI,
                           font=('Century 12'),
                           borderwidth=0)
        self.txt_usuario.place(x=150, y=40, width=90, height=20)

        
        lbl_contra = Label(ventanaI,
                           bg = "CYAN", borderwidth=0,
                           font=('Helvetica', 12),
                           text = "Contraseña: ")
        lbl_contra.place(x=40, y=90)
        
        self.txt_contra = Text(ventanaI,
                          font=('Century 12'),
                          borderwidth=0)
        self.txt_contra.place(x=150, y=90, width=100, height=20)


        #Boton de validación
        btn_inicio = Button(ventanaI,
                            image= self.imagen_final,
                            bg = "CYAN", borderwidth=0,
                            font=('Helvetica', 10),
                            text = "Iniciar sesión", compound='center',
                            command= partial(self.validar_login, ventanaI))
        
        btn_inicio.place(x=80, y=130)

    def validar_login(self, ventana):
        #Recuperamos los datos del usuario
        self.obj_conexion.usuario = self.txt_usuario.get("1.0","end-1c")
        self.obj_conexion.contraseña = self.txt_contra.get("1.0","end-1c")

        labels = ['Usuario', 'Contraseña']
        lista = [self.obj_conexion.usuario, self.obj_conexion.contraseña]
        
        vacios = self.validar_ingresos(labels, lista)
        
        if(len(vacios)==0):
            #El resultado del cotejo de datos en la bdd  
            #nos indicará el resultado de la operación hecha
            posicion = self.obj_conexion.validar_login()
            easygui.msgbox(self.mensajes[posicion], title = "Login")

            #Si la validación fue correcta, el usuario inicia su
            #sesión, cargando por default la pantalla de Stock y Logística
            if(posicion==3):
                ventana.destroy()
                self.obj_conexion.recuperar_rol()
                self.StockYLogística()
                
        else:
            mensaje = "Ingreso incorrecto. Por favor complete los campos: " + str(vacios)
            easygui.msgbox(mensaje, title = "Login") 
            
        
    def CargarRegistro(self):
        ventanaR = Tk()
        
        lbl_usuario = Label(ventanaR,
                            bg = "CYAN", borderwidth=0,
                            #font=fontStyle, fg = "black",
                            text = "Usuario: ")
        lbl_usuario.pack()

        txt_usuario = Text(ventanaR,
                           borderwidth=0)
        txt_usuario.pack()
#Registro      
    def CargarRegistro(self):
        #Ventana de inicio
        ventanaR = Toplevel()
        ventanaR.geometry("340x520")
        ventanaR.configure(bg="pink")
        ventanaR.title("ZapaCrypto61 - Registro")
        
        ventanaR.iconbitmap("Fotos/Logo.ico")

        #Detalles de usuario
        lbl_usuario = Label(ventanaR,
                            bg = "pink", borderwidth=0,
                            font=('Helvetica', 12),
                            #font=fontStyle, fg = "black",
                            text = "Usuario: ")
        lbl_usuario.place(x=60, y=40)

        self.txt_usuario = Text(ventanaR,
                           font=('Century 12'),
                           borderwidth=0)
        self.txt_usuario.place(x=150, y=40, width=100, height=20)

        
        lbl_contra = Label(ventanaR,
                           bg = "pink", borderwidth=0,
                           font=('Helvetica', 12),
                           text = "Contraseña: ")
        lbl_contra.place(x=40, y=90)
        
        self.txt_contra = Text(ventanaR,
                          font=('Century 12'),
                          borderwidth=0)
        self.txt_contra.place(x=150, y=90, width=100, height=20)

        #Datos persona
        lbl_nombre = Label(ventanaR,
                            bg = "pink", borderwidth=0,
                            font=('Helvetica', 12),
                            #font=fontStyle, fg = "black",
                            text = "Nombre: ")
        lbl_nombre.place(x=60, y=140)

        self.txt_nombre = Text(ventanaR,
                           font=('Century 12'),
                           borderwidth=0)
        self.txt_nombre.place(x=150, y=140, width=100, height=20)

        
        lbl_apellido = Label(ventanaR,
                           bg = "pink", borderwidth=0,
                           font=('Helvetica', 12),
                           text = "Apellido: ")
        lbl_apellido.place(x=60, y=190)
        
        self.txt_apellido = Text(ventanaR,
                          font=('Century 12'),
                          borderwidth=0)
        self.txt_apellido.place(x=150, y=190, width=100, height=20)

        # Datos contacto
        lbl_dni = Label(ventanaR,
                            bg = "pink", borderwidth=0,
                            font=('Helvetica', 12),
                            #font=fontStyle, fg = "black",
                            text = "DNI: ")
        lbl_dni.place(x=70, y=240)

        self.txt_dni = Text(ventanaR,
                           font=('Century 12'),
                           borderwidth=0)
        self.txt_dni.place(x=150, y=240, width=150, height=20)

        
        lbl_mail = Label(ventanaR,
                           bg = "pink", borderwidth=0,
                           font=('Helvetica', 12),
                           text = "Mail: ")
        lbl_mail.place(x=70, y=290)
        
        self.txt_mail = Text(ventanaR,
                          font=('Century 12'),
                          borderwidth=0)
        self.txt_mail.place(x=150, y=290, width=150, height=20)


        # Datos contacto 2
        lbl_telefono = Label(ventanaR,
                        bg = "pink", borderwidth=0,
                        font=('Helvetica', 12),
                        #font=fontStyle, fg = "black",
                        text = "Telefono: ")
        lbl_telefono.place(x=50, y=340)

        self.txt_telefono = Text(ventanaR,
                           font=('Century 12'),
                           borderwidth=0)
        self.txt_telefono.place(x=150, y=340, width=150, height=20)

        
        lbl_codigo_postal = Label(ventanaR,
                           bg = "pink", borderwidth=0,
                           font=('Helvetica', 12),
                           text = "Codigo postal: ")
        lbl_codigo_postal.place(x=30, y=390)
        
        self.txt_codigo_postal = Text(ventanaR,
                          font=('Century 12'),
                          borderwidth=0)
        self.txt_codigo_postal.place(x=150, y=390, width=150, height=20)


        #Boton de validación
        btn_inicio = Button(ventanaR,
                            image= self.imagen_final,
                            bg = "pink", borderwidth=0,
                            font=('Helvetica', 10),
                            text = "Registrarse", compound='center',
                            command= partial(self.registrar_usuario, ventanaR))
        
        btn_inicio.place(x=90, y=430)

        
    def registrar_usuario(self, ventana):
        #Recuperamos los datos del usuario
        self.obj_conexion.usuario = self.txt_usuario.get("1.0","end-1c")
        self.obj_conexion.contraseña = self.txt_contra.get("1.0","end-1c")

        self.obj_conexion.nombre = self.txt_nombre.get("1.0","end-1c")
        self.obj_conexion.apellido = self.txt_apellido.get("1.0","end-1c")
        
        self.obj_conexion.dni = str(self.txt_dni.get("1.0","end-1c"))
        self.obj_conexion.mail = str(self.txt_mail.get("1.0","end-1c"))
        self.obj_conexion.teléfono = str(self.txt_telefono.get("1.0","end-1c"))
        self.obj_conexion.codigo_postal = str(self.txt_codigo_postal.get("1.0","end-1c"))

        #Validamos que no haya datos nulos
        labels = ['Usuario', 'Contraseña', 'Nombre', 'Apellido', 'DNI', 'Mail', 'Teléfono', 'Código Postal']
        lista = [self.obj_conexion.usuario,
                 self.obj_conexion.contraseña,
                 self.obj_conexion.nombre,
                 self.obj_conexion.apellido,
                 self.obj_conexion.dni,
                 self.obj_conexion.teléfono,
                 self.obj_conexion.codigo_postal]
        
        vacios = self.validar_ingresos(labels, lista)
        
        if(len(vacios)==0):
            #Validamos que se ingresen los datos numéricos requeridos
            #requeridos como tal mediante un manejo de excepciones
            try:
                self.obj_conexion.dni = int(self.txt_dni.get("1.0","end-1c"))
                self.obj_conexion.teléfono = int(self.txt_telefono.get("1.0","end-1c"))
                
                mensajes = ["Lo sentimos, se produjo un error en el registro. Intente nuevamente."
                            , "El nombre de usuario dado ya existe. Por favor, elija otro."
                            , "Lo sentimos, hubo un error inesperado en el sistema. Intente nuevamente."
                            , "¡Bienvenido al sistema, " + self.obj_conexion.usuario + "!"]
                

                #Validamos que el usuario no exista
                posicion = self.obj_conexion.registrar_usuario()
                easygui.msgbox(mensajes[posicion], title = "Registro")

                if(posicion==3):
                    ventana.destroy()
                    self.StockYLogística()
                    
            except Exception as e:
                easygui.msgbox("Recuerde que los campos de teléfono y dni deben ser numéricos.", title = "Registro")

        else:
            mensaje = "Ingreso incorrecto. Por favor complete los campos: " + str(vacios)
            easygui.msgbox(mensaje, title = "Registro")  


#Stock y Logística
    def StockYLogística(self):
        SYL = Tk()
        SYL.geometry("900x600")
        SYL.configure(bg="BLUE")
        SYL.title("Stock y Logística")



        BSYL = tkinter.Button(SYL, text="Volver", command=lambda: [self.Atrás(SYL), ()])
        BSYL.place(x=850, y=5)

        ASYL = tkinter.Button(SYL, text="Stock Y \nLogística", height=5, width=12, command=lambda: [])
        ASYL.place(x=30, y=100)

        AVYC = tkinter.Button(SYL, text="Ventas Y \nClientes", height=5, width=12, command=lambda: [self.VentasYClientes(), SYL.withdraw()])
        AVYC.place(x=30, y=200)

        ACYP = tkinter.Button(SYL, text="Compras Y \nProveedores", height=5, width=12, command=lambda: [self.ComprasYProveedores(), SYL.withdraw()])
        ACYP.place(x=30, y=300)

        ACONT = tkinter.Button(SYL, text="Contabilidad", height=5, width=12, command=lambda: [self.Contabilidad(), SYL.withdraw()])
        ACONT.place(x=30, y=400)

        B1SYL = tkinter.Button(SYL, text="Actualizar Stock", command=lambda: [self.Fun1SYL(),])
        B1SYL.place(x=150, y=50)

        B2SYL = tkinter.Button(SYL, text="Actualizar Empleado", command="")
        B2SYL.place(x=150, y=75)

        B2SYL = tkinter.Button(SYL, text="Listar Remitos", command="")
        B2SYL.place(x=150, y=100)


        self.ventana.withdraw()

    def Fun1SYL(self):
        F1SYL = Tk()
        F1SYL.geometry("900x600")
        F1SYL.title("adfs")
        var = ""
        mostrarArt(var)
        lblMostrarArt = Label(F1SYL, textvariable=var, relief=RAISED)
        lblMostrarArt.pack()
        F1SYL.mainloop()


    def registrarCompra(self,art):



        print("Se registro la compra"+art)
        datos= list()
        for i in range (len(art)):
            if art[i]!=",":
                datos.append(art[i])
        print(datos)
        easygui.msgbox("Se registró la compra exitosamente de los articulos: "+art, title="ZapaCrypto")

#Los datos que hay que pasar a stock, stock:


    def mostrarArticulos(self):

        self.ventanaArt=Tk()
        self.ventanaArt.geometry("1000x700")
        self.ventanaArt.configure(bg="BLUE")
        Articulos=Listbox(self.ventanaArt,height=30,width=50)
        Articulos.place(x=20,y=33)

        BVYC = tkinter.Button(self.ventanaArt, text="Volver", command=lambda: [self.Atrás(self.ventanaArt)])
        BVYC.place(x=950, y=5)

        Labelart = Label(self.ventanaArt, text="ID", bg="CYAN", font=("Helvetica", 14))
        Labelart.place(x=15, y=5)
        Labelart3 = Label(self.ventanaArt, text="Lista de articulos", bg="CYAN", font=("Helvetica", 14))
        Labelart3.place(x=40, y=5)
        # Meter articulos en la lista
        bdd = BDD()
        conexion = bdd.conectar_bdd()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM Articulo")
        respuesta = cursor.fetchall()
        for x in respuesta:
            Articulos.insert(END, x)

        Labelart2 = Label(self.ventanaArt, text="Elija ID de articulos a comprar", bg="CYAN", font=("Helvetica", 14))
        Labelart2.place(x=350, y=40)
        Labelart4 = Label(self.ventanaArt, text="(separado por comas)", bg="CYAN", font=("Helvetica", 8))
        Labelart4.place(x=616, y=46)

        Entryvyc = Entry(self.ventanaArt, text="...", width=50)
        Entryvyc.place(x=350, y=70)


        botonCompra = Button(self.ventanaArt, text="Comprar", command=lambda:[self.registrarCompra(Entryvyc.get())], font=("Helvetica", 18))
        botonCompra.place(x=430, y=110)


        print ("Mostrar articulos")

    def atencionAlCliente(self):
        easygui.msgbox("Para comunicarse con atencion al cliente, comunicarse con: 11 2561-1025", title="Atencion al cliente")


#Ventas y Clientes
    def VentasYClientes(self):
        VYC = Tk()
        VYC.geometry("900x600")
        VYC.configure(bg="BLUE")
        VYC.title("Ventas y Clientes")

        BVYC = tkinter.Button(VYC, text="Volver", command=lambda: [self.Atrás(VYC), ()])
        BVYC.place(x=850, y=5)
        ASYL = tkinter.Button(VYC, text="Stock Y \nLogística", height=5, width=12, command=lambda: [self.StockYLogística(), VYC.withdraw()])
        ASYL.place(x=30, y=100)
        AVYC = tkinter.Button(VYC, text="Ventas Y \nClientes", height=5, width=12, command=lambda: [])
        AVYC.place(x=30, y=200)
        ACYP = tkinter.Button(VYC, text="Compras Y \nProveedores", height=5, width=12, command=lambda: [self.ComprasYProveedores(), VYC.withdraw()])
        ACYP.place(x=30, y=300)
        ACONT = tkinter.Button(VYC, text="Contabilidad", height=5, width=12, command=lambda: [self.Contabilidad(), VYC.withdraw()])
        ACONT.place(x=30, y=400)

        B1VYC = tkinter.Button(VYC, text="Mostrar articulos ", font=("Helvetica", 36),
                               command=lambda: [self.mostrarArticulos(), ])
        B1VYC.place(x=300, y=200)

        B2VYC = tkinter.Button(VYC, text="Atencion al cliente  ", font=("Helvetica", 13),
                               command=lambda: [self.atencionAlCliente()])
        B2VYC.place(x=700, y=550)

        #B16VYC = tkinter.Button(VYC, text="Funcionalidad 16", command=lambda: [(), ()])
        #B16VYC.place(x=150, y=425)

        self.ventana.withdraw()
        

#Compras y Proveedores
    def ComprasYProveedores(self):
        self.CYP = Toplevel()
        self.CYP.geometry("900x600")
        self.CYP.title("Compras y Proveedores")
        self.CYP.configure(bg="BLUE")

        BCYP = tkinter.Button(self.CYP, text="Volver", command=lambda: [self.Atrás(self.CYP), ()])
        BCYP.place(x=850, y=5)

        ASYL = tkinter.Button(self.CYP, text="Stock Y \nLogística", height=5, width=12, command=lambda: [self.StockYLogística(), self.CYP.withdraw()])
        ASYL.place(x=30, y=100)

        AVYC = tkinter.Button(self.CYP, text="Ventas Y \nClientes", height=5, width=12, command=lambda: [self.VentasYClientes(), self.CYP.withdraw()])
        AVYC.place(x=30, y=200)

        ACYP = tkinter.Button(self.CYP, text="Compras Y \nProveedores", height=5, width=12, command=lambda: [])
        ACYP.place(x=30, y=300)

        ACONT = tkinter.Button(self.CYP, text="Contabilidad", height=5, width=12, command=lambda: [self.Contabilidad(), self.CYP.withdraw()])
        ACONT.place(x=30, y=400)

        B1CYP = tkinter.Button(self.CYP, text="Proveedores         ", command=lambda: [self.Proveedores(),])
        B1CYP.place(x=150, y=50)

        B2CYP = tkinter.Button(self.CYP, text="Agregar Artículos", command=lambda: [self.AgregarArtProv(),])
        B2CYP.place(x=150, y=75)

        B3CYP = tkinter.Button(self.CYP, text="Funcionalidad 3  ", command="")
        B3CYP.place(x=150, y=100)

        self.ventana.withdraw()

    def Proveedores(self):
        self.Prov = Tk()
        self.Prov.geometry("900x600")
        self.Prov.title("Compras y Proveedores")
        self.Prov.configure(bg="BLUE")

        Provee = Listbox(self.Prov, height=30, width=140)
        Provee.place(x=20, y=60)

        Labelart = Label(self.Prov, text="Contacto de Proveedores", bg="CYAN", font=("Helvetica", 20))
        Labelart.place(x=250, y=5)
        #Labelart3 = Label(self.Prov, text="Lista de articulos", bg="CYAN", font=("Helvetica", 14))
        #Labelart3.place(x=40, y=5)
        # Meter articulos en la lista
        bdd = BDD()
        self.conexion = bdd.conectar_bdd()
        cursor = self.conexion.cursor()
        cursor.execute("Select * from Proveedor; ")

        proveedor = cursor.fetchall()

        for x in proveedor:
            Provee.insert(END, x)

        cursor.close()
        self.conexion.close()

    def AgregarArtProv(self):

        self.ArtProv = Tk()
        self.ArtProv.geometry("900x600")
        self.ArtProv.title("Compras y Proveedores")
        self.ArtProv.configure(bg="BLUE")

        Labelart = Label(self.ArtProv, text="Completar todos los campos antes de continuar", bg="CYAN", font=("Helvetica", 20))
        Labelart.place(x=250, y=5)

        #bdd = BDD()
        #conexion = bdd.conectar_bdd()
        #cursor = conexion.cursor()
        #Agrego = cursor.execute("INSERT INTO Articulo VALUES (<getIdArt>, <getIdArt>, <getIdProd>, <getTalle>, <getColor>)")

        #cursor.close()
        #conexion.close()

        cursor = self.conexion.cursor()
        sp = """INSERT INTO
                Proveedor(talle
                        , color
                        , nombre
                        , precio
                        , id_proveedor
                        )
                VALUES('""" + self.Talle + """'
                        ,'""" + self.Color + """'
                        ,'""" + self.Nombre + """'
                        ,'""" + self.Precio + """'
                        ,'""" + self.IDProv + """'
                        );"""

        cursor.execute(sp)
        self.conexion.commit()

        cursor.close()


        B16CYP = tkinter.Button(self.ArtProv, text="Aceptar", command=sp)
        B16CYP.place(x=525, y=260)

        LTalle = Label(self.ArtProv, text="Talle: ", font=("Helvetica", 12))
        LTalle.place(x=130, y=200)
        Tallee = StringVar(value="")
        Talle = Entry(self.ArtProv, textvariable=Tallee, width=50)
        Talle.place(x=200, y=200)

        LColor = Label(self.ArtProv, text="Color: ", font=("Helvetica", 12))
        LColor.place(x=130, y=230)
        Colorr = StringVar(value="")
        Color = Entry(self.ArtProv, textvariable=Colorr, width=50)
        Color.place(x=200, y=230)

        LNombre = Label(self.ArtProv, text="Nombre: ", font=("Helvetica", 12))
        LNombre.place(x=130, y=260)
        Nombree = StringVar(value="")
        Nombre = Entry(self.ArtProv, textvariable=Nombree, width=50)
        Nombre.place(x=200, y=260)

        LPrecio = Label(self.ArtProv, text="Precio: ", font=("Helvetica", 12))
        LPrecio.place(x=130, y=290)
        Precioo = StringVar(value="")
        Precio = Entry(self.ArtProv, textvariable=Precioo, width=50)
        Precio.place(x=200, y=290)

        LIDProv = Label(self.ArtProv, text="IDProv: ", font=("Helvetica", 12))
        LIDProv.place(x=130, y=320)
        IDProvv = StringVar(value="")
        IDProv = Entry(self.ArtProv, textvariable=IDProvv, width=50)
        IDProv.place(x=200, y=320)



#Contabilidad


    def Contabilidad(self):
        CONT = Tk()
        CONT.geometry("900x600")
        CONT.configure(bg="BLUE")
        CONT.title("Contabilidad")

        BCONT = tkinter.Button(CONT, text="Volver", command=lambda: [self.Atrás(CONT), ()])
        BCONT.place(x=850, y=5)

        ASYL = tkinter.Button(CONT, text="Stock Y \nLogística", height=5, width=12,
                              command=lambda: [self.StockYLogística(), CONT.withdraw()])
        ASYL.place(x=30, y=100)

        AVYC = tkinter.Button(CONT, text="Ventas Y \nClientes", height=5, width=12,
                              command=lambda: [self.VentasYClientes(), CONT.withdraw()])
        AVYC.place(x=30, y=200)

        ACYP = tkinter.Button(CONT, text="Compras Y \nProveedores", height=5, width=12,
                              command=lambda: [self.ComprasYProveedores(), CONT.withdraw()])
        ACYP.place(x=30, y=300)

        ACONT = tkinter.Button(CONT, text="Contabilidad", height=5, width=12, command=lambda: [])
        ACONT.place(x=30, y=400)

        B1CONT = tkinter.Button(CONT, text="Funcionalidad 1  ", command=lambda: [self.Fun1Contabilidad(), ])
        B1CONT.place(x=150, y=50)

        B2CONT = tkinter.Button(CONT, text="Funcionalidad 2  ", command=lambda: [self.Fun2Contabilidad(), ])
        B2CONT.place(x=150, y=75)

        B3CONT = tkinter.Button(CONT, text="Funcionalidad 3  ", command="")
        B3CONT.place(x=150, y=100)

        self.ventana.withdraw()

    def Fun1Contabilidad(self):
        manzanas = [20, 10, 25, 60]
        nombres = ["Activos Fijos", "Activos Corrientes", "Gastos", "Impuestos"]
        plt.pie(manzanas, labels=nombres)
        plt.show()

        bdd = BDD()
        conexion = bdd.conectar_bdd()
        cursor = conexion.cursor()
        cursor.execute("SELECT precio FROM Producto")

    def Fun2Contabilidad(self):
        self.Costo = Tk()
        self.Costo.geometry("900x600")
        self.Costo.title("Contabilidad")
        self.Costo.configure(bg="BLUE")

        Labelcost = Label(self.Costo, text="Completar todos los campos antes de continuar", bg="CYAN",
                          font=("Helvetica", 20))
        Labelcost.place(x=250, y=5)

        # bdd = BDD()
        # conexion = bdd.conectar_bdd()
        # cursor = conexion.cursor()
        # Agrego = cursor.execute("INSERT INTO Costo VALUES (<getIdcosto>, <getTitulo>, <getMonto>, <getDescripcion>")

        # cursor.close()
        # conexion.close()

        # B16CYP = tkinter.Button(self.Costo, text="Aceptar", command=Agrego)
        # B16CYP.place(x=525, y=260)

        LIDCosto = Label(self.Costo, text="Id Costo: ", font=("Helvetica", 12))
        LIDCosto.place(x=130, y=200)
        IDCostoo = StringVar(value="")
        IDCosto = Entry(self.Costo, textvariable=IDCostoo, width=50)

        IDCosto.place(x=200, y=200)

        LDescripcion = Label(self.Costo, text="Descripcion: ", font=("Helvetica", 12))
        LDescripcion.place(x=130, y=230)
        Descripcionn = StringVar(value="")
        Descripcion = Entry(self.Costo, textvariable=Descripcionn, width=50)
        Descripcion.place(x=200, y=230)

        LTitulo = Label(self.Costo, text="Titulo: ", font=("Helvetica", 12))
        LTitulo.place(x=130, y=260)
        tituloo = StringVar(value="")
        titulo = Entry(self.Costo, textvariable=tituloo, width=50)
        titulo.place(x=200, y=260)

        LMonto = Label(self.Costo, text="monto: ", font=("Helvetica", 12))
        LMonto.place(x=130, y=290)
        montoo = StringVar(value="")
        monto = Entry(self.Costo, textvariable=montoo, width=50)
        monto.place(x=200, y=290)


#Main
if __name__=='__main__':
    warnings.filterwarnings('ignore')
    Entorno_Grafico()
