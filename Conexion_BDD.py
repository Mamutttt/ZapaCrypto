import mysql.connector

class BDD:
    #Definimos los datos de la conexión
    direccion_servidor = 'aws-sa-east-1.connect.psdb.cloud'
    nombre_bd = 'zapacryptodb'
    usr = 'avtrlpr7q9s8fg8kd3yp'
    pwd = 'pscale_pw_v2vCTEV5quiGIwG5wA8c0BKVHUvamHiNljdbnvReCQY'
    
    #Datos usuario
    usuario = ""
    contraseña = ""
    nombre = ""
    apellido = ""
    dni = ""
    mail = ""
    teléfono = ""
    código_postal = ""
          
    
    def conexion_bdd(self):   
        #Establecemos la conexión con gestión de errores
        try:
            self.conexion = mysql.connector.connect(host= self.direccion_servidor,
                                                database=self.nombre_bd,
                                                user=self.usr,
                                                password=self.pwd)
            #Conexion exitosa
            #Se recupera la información de la conexión
            db_Info = self.conexion.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            
            return self.conexion

        except mysql.connector.Error as e:
            #Falla en la conexión
            print("Ocurrió un error al conectar a SQL Server: ", e)
            

    def validar_login(self):
        #Consulta
        # 0 - Error en la ejecución
        # 1 - Usuario existente, contra incorrecta
        # 2 - Usuario y contraseña correctos
        
        consulta = 0
        
        try:
            #Armamos la consulta
            cursor = self.conexion.cursor()
            sp = """SELECT
			U.contra
		FROM
			Usuario `U`
		WHERE
			U.usuario = '""" + self.usuario + "';"""
	    
            cursor.execute(sp)
            contra = cursor.fetchone()
            
            #Validamos que haya encontrado un usuario 
            if(contra!=None):
                consulta+=1
                for linea in contra:
                    #Validamos que la contraseña sea correcta
                    if(linea==self.contraseña):
                        print("user correcto")
                        consulta+=1
                    
            else:
                print("No hay contra.")
                
            cursor.close()


        except Exception as e:
            consulta = 0
            print(e)
            
        finally:
            print(consulta)
            return consulta

    def registrar_usuario(self):
        try:
            print(self.usuario)
            
            #Validamos que no exista el usuario
            if(self.validar_login()>0):
                print("usuario ya existente")

            else:
                cursor = conexion.cursor()
                sp = """INSERT INTO
                        Usuario(usuario
                                , contra
                                , nombre
                                , apellido
                                , dni
                                , mail
                                , telefono
                                , codigo_postal
                                )
                        VALUES('""" + self.usuario + """'
                                ,'""" + self.contraseña + """'
                                ,'""" + self.nombre + """'
                                ,'""" + self.apellido + """'
                                ,'""" + str(self.dni) + """'
                                ,'""" + self.mail + """'
                                ,'""" + str(self.teléfono) + """'
                                ,'""" + self.código_postal + """'
                                );""" 
                     
                cursor.execute(sp)
                self.conexion.commit()

                cursor.close()
                print("se registro al usuario")

        except Exception as e:
            print(e)
                           

    
if __name__=='__main__':
    obj_conexion = BDD()
    conexion = obj_conexion.conexion_bdd()

    #Datos de prueba que deberían ser recuperados con un txtnombrelabel.get()
    obj_conexion.usuario = "caro"
    obj_conexion.contraseña = "123456"

    obj_conexion.validar_login()

    obj_conexion.nombre = "Carolina"
    obj_conexion.apellido = "Linares"
    obj_conexion.dni = "44939978"
    obj_conexion.mail = "carolinares003@gmail.com"
    obj_conexion.teléfono = "1127354645"
    obj_conexion.código_postal = "1407"
    
    obj_conexion.registrar_usuario()

    obj_conexion.validar_login()

    
