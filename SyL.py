from Conexion_BDD_V2 import BDD

def mostrarArt(respuesta):
    bdd = BDD()
    conexion = bdd.conectar_bdd()
    print(conexion)
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM Articulo")
    respuesta = cursor.fetchall()
    for x in respuesta:
        print(x)

def aStockArticulo():
    bdd = BDD()
    conexion = bdd.conectar_bdd()
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO Articulo VALUES (<getIdArt>, <getIdProd>, <getTalle>, <getColor>)")
    cursor.execute("SELECT * FROM Articulo")
    respuesta = cursor.fetchall()
    for x in respuesta:
        print(x)



def bStockArticulo():
    bdd = BDD()
    conexion = bdd.conectar_bdd()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM Articulo WHERE id_articulo=<getIdArt>")
    cursor.execute("SELECT * FROM Articulo")
    respuesta = cursor.fetchall()
    for x in respuesta:
        print(x)

def mStockArticulo():
    bdd = BDD()
    conexion = bdd.conectar_bdd()
    cursor = conexion.cursor()
    cursor.execute("UPDATE Articulo SET <getCampo>=<getValor> WHERE id_articulo=<getArtId>")
    cursor.execute("SELECT * FROM Articulo")
    respuesta = cursor.fetchall()
    for x in respuesta:
        print(x)

def aStockProducto():
    bdd = BDD()
    conexion = bdd.conectar_bdd()
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO Producto VALUES (<getIdProd>, <getModel>, <getDesc>, <getPrecio>)")
    cursor.execute("SELECT * FROM Articulo")
    respuesta = cursor.fetchall()
    for x in respuesta:
        print(x)

def mostrarProd():
    bdd = BDD()
    conexion = bdd.conectar_bdd()
    cursor = conexion.cursor()
    cursor.execute("SELECT <getCampo> FROM Producto")
    respuesta = cursor.fetchall()
    for x in respuesta:
        print(x)