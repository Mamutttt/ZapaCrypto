import mysql.connector

class BDD:
    #Definimos los datos de la conexión
    direccion_servidor = 'aws-sa-east-1.connect.psdb.cloud'
    nombre_bd = 'zapacryptodb'
    usr_bd = 'avtrlpr7q9s8fg8kd3yp'
    pwd_bd = 'pscale_pw_v2vCTEV5quiGIwG5wA8c0BKVHUvamHiNljdbnvReCQY'
    
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
          
    
    def conectar_bdd(self):   
        #Establecemos la conexión con gestión de errores
        try:
            self.conexion = mysql.connector.connect(host= self.direccion_servidor,
                                                database=self.nombre_bd,
                                                user=self.usr_bd,
                                                password=self.pwd_bd)
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
        consulta = 0
        try:
            #Validamos que no exista el usuario
            if(self.validar_login()>1):
                consulta = 1
                #mensaje = "El nombre de usuario dado ya existe. Por favor, elija otro."

            #Validamos que no haya ocurrido un error en la validación
            elif(self.validar_login()==0):
                consulta = 2
                #mensaje = "Lo sentimos, hubo un error inesperado en el sistema. Vuelva a intentarlo."

            #Registramos al usuario
            else:
                cursor = self.conexion.cursor()
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

                consulta = 3
                #mensaje = "Se registro al usuario correctamente."

        except Exception as e:
            print(e)
            #consulta = 0

        finally:
            return consulta
            
        
                           
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


        cursor = conexion.cursor()
        cursor.execute("Select * from Proveedor; ")

        proveedor = cursor.fetchall()

        for proveedor in proveedor:
            print(proveedor)

        cursor.close()
        conexion.close()
