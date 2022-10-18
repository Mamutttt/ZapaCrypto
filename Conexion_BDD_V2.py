import mysql.connector

class BDD:
    #Definimos los datos de la conexión
    direccion_servidor = 'aws-sa-east-1.connect.psdb.cloud'
    nombre_bd = 'zapacryptodb'
    usr = 'avtrlpr7q9s8fg8kd3yp'
    pwd = 'pscale_pw_v2vCTEV5quiGIwG5wA8c0BKVHUvamHiNljdbnvReCQY'
    
    #Datos usuario
    id_rol = 0
    id_usuario = ""
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
        # 1 - Usuario inexistente
        # 2 - Usuario existente, contra incorrecta
        # 3 - Usuario y contraseña correctos 
        consulta = 1
        
        try:
            #Armamos la consulta
            cursor = self.conexion.cursor()
            sp = """SELECT
			U.id_usuario
			, U.contra
		FROM
			Usuario `U`
		WHERE
			U.usuario = '""" + self.usuario + "';"""
	    
            cursor.execute(sp)
            contra = cursor.fetchall()
           
            #Validamos que haya encontrado un usuario 
            if(len(contra)!=0):
                consulta+=1
                for linea in contra:
                    #Validamos que la contraseña sea correcta y, si lo es,
                    #carga el id del usuario (para recuperar su rol y demás)
                    if(linea[1]==self.contraseña):
                        consulta+=1
                        self.id_usuario = linea[0] 
                
            cursor.close()

        except Exception as e:
            consulta = 0
            
        finally:
            return consulta

    def registrar_usuario(self):
        mensaje = ""
        try:
            #Validamos que no exista el usuario
            if(self.validar_login()>1):
                mensaje = "El nombre de usuario dado ya existe. Por favor, elija otro."

            #Validamos que no haya ocurrido un error en la validación
            elif(self.validar_login()==0):
                mensaje = "Lo sentimos, hubo un error inesperado en el sistema. Vuelva a intentarlo."

            #Registramos al usuario
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
                
                mensaje = "Se registro al usuario correctamente."

        except Exception as e:
            mensaje = str(e)

        finally:
            print(mensaje)
            return mensaje
            
                           
    def recuperar_rol(self):
        try:
            #Armamos la consulta
            cursor = self.conexion.cursor()
            sp = """SELECT
                        RUR.id_rol
                    FROM
                        Usuario `U`
                        , rel_usuario_rol `RUR`
                    WHERE
                        U.id_usuario = RUR.id_usuario
                    AND
			U.id_usuario = '""" + str(self.id_usuario) + "';"""
	    
            cursor.execute(sp)
            rol = cursor.fetchone()
            
            #Validamos que haya encontrado un usuario 
            if(rol!=None):
                for linea in rol:
                    #Validamos que la contraseña sea correcta
                    self.id_rol = linea             
            else:
                print("Usuario común, sin rol.")
                
            cursor.close()
            
        except Exception as e:
            print(e)
            
    
if __name__=='__main__':
    obj_conexion = BDD()
    conexion = obj_conexion.conexion_bdd()

    #Listado de mensajes a imprimir según el resultado de la validación
    mensajes = ["Se produjo un error en la validación."
                ,"El usuario no existe."
                ,"La contraseña es incorrecta."
                ,"Ingreso correcto. Bienvenido al sistema."]
    
    #Datos de prueba que deberían ser recuperados con un txtnombrelabel.get()
    obj_conexion.usuario = "caro2"
    obj_conexion.contraseña = "1234567"

    #Prueba de validación de de datos, con su correspondiente mensaje
    posicion= obj_conexion.validar_login()
    print(mensajes[posicion])

    obj_conexion.nombre = "Carolina"
    obj_conexion.apellido = "Linares"
    obj_conexion.dni = "44939978"
    obj_conexion.mail = "carolinares003@gmail.com"
    obj_conexion.teléfono = "1127354645"
    obj_conexion.código_postal = "1407"
    

    print(obj_conexion.registrar_usuario())
    
    obj_conexion.validar_login()
    
    obj_conexion.recuperar_rol()

    
