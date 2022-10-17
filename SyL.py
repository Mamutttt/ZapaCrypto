from Conexion_BDD_V2 import BDD

def mostrarArt():
    bdd = BDD()
    conexion = bdd.conexion_bdd()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM Articulo")
    respuesta = cursor.fetchall()
    for x in respuesta:
        print(x)

def aStockArticulo():
    bdd = BDD()
    conexion = bdd.conexion_bdd()
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO Articulo VALUES (<getIdArt>, <getIdProd>, <getTalle>, <getColor>)")
    respuesta = cursor.fetchall()
    for x in respuesta:
        print(x)