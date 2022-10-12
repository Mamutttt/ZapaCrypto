from tkinter import * 
from tkinter import ttk
from turtle import bgcolor
from Conexionsql import cnx
from PIL import ImageTk, Image
root = Tk() 


# root window title and dimension
root.title("Contabilidad")
root.geometry('720x500')
root.resizable(0, 0)
root.configure(background="white")

leftbar=Frame(root, width=150, height=500, background="#252424")
leftbar.place(x=0, y=0)

# Definir directorios de imagenes
sylphoto = PhotoImage(file = r"C:\Users\agust\OneDrive\Escritorio\Proyecto Berea\APP\App 2\Images\stockylogistica.png") 
conphoto = PhotoImage(file = r"C:\Users\agust\OneDrive\Escritorio\Proyecto Berea\APP\App 2\Images\contabilidad.png") 
vycphoto = PhotoImage(file = r"C:\Users\agust\OneDrive\Escritorio\Proyecto Berea\APP\App 2\Images\ventasyclientes.png")
cypphoto = PhotoImage(file = r"C:\Users\agust\OneDrive\Escritorio\Proyecto Berea\APP\App 2\Images\comprasyproveedores.png")

#Modificar tamaño imagenes
photoimage1 = sylphoto.subsample(2, 2)
photoimage2 = conphoto.subsample(2, 2) 
photoimage3 = vycphoto.subsample(2, 2) 
photoimage4 = cypphoto.subsample(2, 2) 


#Botones
BotonSYL = Button(root, text = 'Stock y Logistica', image = photoimage1, bg='#252424',  compound=TOP).grid(row=0, column=0)

BotonCON = Button(root, text = 'Contabilidad', image = photoimage2, bg='#252424',  compound=TOP).grid(row=2, column=0)

BotonVYC = Button(root, text = 'Ventas y Clientes', image = photoimage3, bg='#252424',  compound=TOP).grid(row=3, column=0)

BotonCYP = Button(root, text = 'Compras y Proveedores', image = photoimage4, bg='#252424', compound=TOP).grid(row=4, column=0)



mainloop() 