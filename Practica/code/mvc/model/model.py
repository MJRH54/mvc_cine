from mysql import connector

class Model:
    """
    A data model with MySQL for a CineDB
    """

    def __init__(self, config_db_file='config.txt'):
        self.config_db_file = config_db_file
        self.config_db = self.read_config_db()
        self.connect_to_db()

    def read_config_db(self):
        d = {}
        with open(self.config_db_file) as f_r:
            for line in f_r:
                (key,val) = line.strip().split(':')
                d[key] = val
            return d

    def connect_to_db(self):
        self.cnx = connector.connect(**self.config_db)
        self.cursor = self.cnx.cursor(buffered=True)
        #self.cursor2 = self.cnx.cursor(buffered=True)

    def close_db(self):
        self.cnx.close()

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------* ADMINS *----------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------* Users Methods *-------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        #**************************************************************#
        #                        * Users Methods *                     #
        #**************************************************************#
        #BASIC CRUD METHODS

    def create_user(self,nombre,correo,tipousuario,usuario,password):
        try:
            null, verify = self.read_thisuser_byuser(usuario)#Buscamos al usuario para evitar que haya dos o mas usuarios iguales registrados
            if (verify == False):
                sql = 'INSERT INTO usuarios(`nombre`,`correo`,`tipo_usuario`,`usuario`,`pass`) VALUES (%s,%s,%s,%s,%s)'
                vals = (nombre,correo,tipousuario,usuario,password)
                self.cursor.execute(sql,vals)
                self.cnx.commit()
                return True
            else:
                null = 1062
                return null
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_user(self,idusuario):
        try:
            sql = 'SELECT * FROM usuarios WHERE id_usuario = %s'
            vals = (idusuario,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err
    
    def read_user_byname(self,nombre):
        try:
            sql = "SELECT * FROM usuarios WHERE nombre LIKE "
            sql += "'%" + nombre + "%';"
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err
    
    def read_all_users(self):
        try:
            sql = 'SELECT * FROM usuarios'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err
            
    #LECTURA DE TODOS LOS DATOS DE UN USUARIO POR EL USUARIO
    def read_user_information_byuser(self,user):
        try:
            sql = 'SELECT * FROM usuarios WHERE usuario LIKE ' + "'" + user + "';"
            self.cursor.execute(sql)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err
    
    #METODO DE VERIFICACION DE USUARIO         
    def read_thisuser_byuser(self,user):
        try:
            sql = 'SELECT * FROM usuarios WHERE usuario LIKE ' + "'" + user + "';"
            self.cursor.execute(sql)
            record = self.cursor.fetchone()
            if(record == None):
                return 0, False
            else:
                return record[1],True           
        except connector.Error as err:
            return err
    #METODO DE VERIFICACION DE CONTRASEÑA DE USUARIO
    def read_user_byuser(self,user,password):
        try:
            sql = 'SELECT usuarios.pass FROM usuarios WHERE usuario LIKE ' + "'" + user + "';"
            self.cursor.execute(sql)
            record = self.cursor.fetchone()
            if(record[0] == password):
                return True
            else:
                return False
        except connector.Error as err:
            return err
    
    def update_user(self,fields,vals):
        try:
            sql = 'UPDATE usuarios SET '+','.join(fields)+' WHERE id_usuario = %s'
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    def remove_user(self,idusuario):
        try:    
            sql = 'DELETE FROM usuarios WHERE id_usuario = %s'
            vals = (idusuario,)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------* Admin Methods *------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        #**************************************************************#
        #                        * Admin Methods *                     #
        #**************************************************************#
        #BASIC CRUD METHODS

    def create_admin(self,nombre,correo,direccion,telefono,usuario,password):
        try:
            null, verify = self.read_thisadmin_byadmin(usuario)#Buscamos al usuario para evitar que haya dos o mas usuarios iguales registrados
            if(verify == False):
                sql = 'INSERT INTO administradores(`nombre`,`correo`,`direccion`,`telefono`,`usuario`,`pass`) VALUES (%s,%s,%s,%s,%s,%s)'
                vals = (nombre,correo,direccion,telefono,usuario,password)
                self.cursor.execute(sql,vals)
                self.cnx.commit()
                return True
            else:
                null = 1062
                return null
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_admin(self,idadmin):
        try:
            sql = 'SELECT * FROM administradores WHERE id_admin = %s'
            vals = (idadmin,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_all_admin(self):
        try:
            sql = 'SELECT * FROM administradores'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err
    #LECTURA DE TODOS LOS DATOS DE UN USUARIO POR EL USUARIO
    def read_admin_information_byuser(self,user):
        try:
            sql = 'SELECT * FROM administradores WHERE usuario LIKE ' + "'" + user + "';"
            self.cursor.execute(sql)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err
    #METODO DE VERIFICACION DE ADMINISTRADOR
    def read_thisadmin_byadmin(self,user):
        try:
            sql = 'SELECT * FROM administradores WHERE usuario LIKE ' + "'" + user + "';"
            self.cursor.execute(sql)
            record = self.cursor.fetchone()
            if(record == None):
                return 0, False
            else:
                return record[1],True
        except connector.Error as err:
            return err
    #METODO DE VERIFICACION DE CONTRASEÑA DE ADMINISTRADOR
    def read_admin_byadmin(self,user,password):
        try:
            sql = 'SELECT administradores.pass FROM administradores WHERE usuario LIKE ' + "'" + user + "';"
            self.cursor.execute(sql)
            record = self.cursor.fetchone()
            if(record[0] == password):
                return True
            else:
                return False
        except connector.Error as err:
            return err
    

    def read_admin_byname(self,nombre):
        try:
            sql = "SELECT * FROM administradores WHERE nombre LIKE "
            sql += "'%" + nombre + "%';"
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err
    
    def update_admin(self,fields,vals):
        try:
            sql = 'UPDATE administradores SET '+','.join(fields)+' WHERE id_admin = %s'
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    def remove_admin(self,idadmin):
        try:    
            sql = 'DELETE FROM administradores WHERE id_admin = %s'
            vals = (idadmin,)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------ * Peliculas Methods *--------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        #**************************************************************#
        #                        * Peliculas Methods *                 #
        #**************************************************************#

    def create_pelicula(self,nombre,sipnosis,flanzamiento):
        try:
            sql = 'INSERT INTO peliculas(`nombre`,`sipnosis`,`FLanzamiento`) VALUES (%s,%s,%s)'
            vals = (nombre,sipnosis,flanzamiento)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_pelicula(self,idpelicula): #Leer peliculas por id_pelicula p/administradores
        try:
            sql = 'SELECT * FROM peliculas WHERE id_pelicula = %s'
            vals = (idpelicula,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_all_pelicula(self): #Leer todas las peliculas, configurar p/usuarios
        try:
            sql = 'SELECT * FROM peliculas'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_pelicula_nombre(self,nombre):
        try:
            sql = "SELECT * FROM peliculas WHERE nombre LIKE "
            sql += "'%" + nombre + "%';"
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def update_pelicula(self,fields,vals):
        try:
            sql = 'UPDATE peliculas SET '+','.join(fields)+' WHERE id_pelicula = %s'            
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_pelicula(self,idpelicula):
        try:
            sql = 'DELETE FROM peliculas WHERE id_pelicula = %s'
            vals = (idpelicula,)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------* Horarios  Methods *----------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        #**************************************************************#
        #                        * Horarios  Methods *                 #
        #**************************************************************#

    def verify_horario(self,dia,hora):
        try:
            sql = "SELECT * FROM horarios WHERE dia LIKE " + "'" + dia + "'" + " AND " + " hora LIKE " + "'" + hora + "';"
            self.cursor.execute(sql)
            record = self.cursor.fetchone()
            if (record == None):
                return 0,True
            else:
                return 1062, False
        except connector.Error as err:
            return err        


    def create_newhorario(self,dia,hora):
        try:
            null, verify = self.verify_horario(dia,hora)
            if(verify == True):
                sql = 'INSERT INTO horarios(`dia`,`hora`) VALUES (%s,%s)'
                vals = (dia,hora)
                self.cursor.execute(sql,vals)
                self.cnx.commit()
                return True
            if(verify == False):
                return null
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_horario(self,idhorario): 
        try:
            sql = 'SELECT * FROM horarios WHERE id_horario = %s'
            vals = (idhorario,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_all_horarios(self): 
        try:
            sql = 'SELECT * FROM horarios'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_horario_bydia_hora(self,dia,hora):
        try:
            sql = "SELECT * FROM horarios WHERE dia LIKE " + "'" + dia + "' AND hora LIKE " + "'" + hora + "';"
            self.cursor.execute(sql)
            records = self.cursor.fetchone()
            return records
        except connector.Error as err:
            return err


    def update_horario(self,fields,vals):
        try:
            sql = 'UPDATE horarios SET '+','.join(fields)+' WHERE id_horario = %s'
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_horario(self,idhorario):
        try:
            sql = 'DELETE FROM horarios WHERE id_horario = %s'
            vals = (idhorario,)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------* Salas  Methods *-------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        #**************************************************************#
        #                        * Salas  Methods *                 #
        #**************************************************************#

    def verify_sala(self,numerosala):
        try:
            sql = "SELECT * FROM salas WHERE numero_sala LIKE " + "'" + numerosala + "';"
            self.cursor.execute(sql)
            record = self.cursor.fetchone()
            if(record == None):
                return 0, True
            else: 
                return 1062, False
        except connector.Error as err:
            return err        

    def create_newsala(self,numerosala,tiposala,numeroasientos):
        try:
            null, verify = self.verify_sala(numerosala)
            if(verify == True):
                sql = 'INSERT INTO salas(`numero_sala`,`tipo_sala`,`numero_asientos`) VALUES (%s,%s,%s)'
                vals = (numerosala,tiposala,numeroasientos)
                self.cursor.execute(sql,vals)
                self.cnx.commit()
                return True
            if(verify == False):
                return null
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_sala(self,idsala): 
        try:
            sql = 'SELECT * FROM salas WHERE id_sala = %s'
            vals = (idsala,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err
    def read_sala_numerosala(self,numerosala): 
        try:
            sql = 'SELECT * FROM salas WHERE numero_sala = %s'
            vals = (numerosala,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_all_sala(self): 
        try:
            sql = 'SELECT * FROM salas'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err


    def update_sala(self,fields,vals):
        try:
            sql = 'UPDATE salas SET '+','.join(fields)+' WHERE id_sala = %s'
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_sala(self,idsala):
        try:
            sql = 'DELETE FROM salas WHERE id_sala = %s'
            vals = (idsala,)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------* Asientos  Methods *-----------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  
        #**************************************************************#
        #                        * Asientos  Methods *                 #
        #**************************************************************#

    def verify_asiento(self,fila,numero):
        try:
            sql = "SELECT * FROM asientos WHERE fila LIKE " + "'" + fila + "'" + " AND " + " numero LIKE " + "'" + numero + "';"
            self.cursor.execute(sql)
            record = self.cursor.fetchone()
            if (record == None):
                return 0,True
            else:
                return 1062, False
        except connector.Error as err:
            return err   

    def create_newasiento(self,fila,numero):
        try:
            null, verify = self.verify_asiento(fila,numero)
            if(verify == True):
                sql = 'INSERT INTO asientos(`fila`,`numero`) VALUES (%s,%s)'
                vals = (fila,numero)
                self.cursor.execute(sql,vals)
                self.cnx.commit()
                return True
            if(verify == False):
                return null
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_asiento(self,idasiento): 
        try:
            sql = 'SELECT * FROM asientos WHERE id_asiento = %s'
            vals = (idasiento,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err
    
    def read_all_asientos(self): 
        try:
            sql = 'SELECT * FROM asientos'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err


    def update_asiento(self,fields,vals):
        try:
            sql = 'UPDATE asientos SET '+','.join(fields)+' WHERE id_asiento = %s'
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_asiento(self,idasiento):
        try:
            sql = 'DELETE FROM asientos WHERE id_asiento = %s'
            vals = (idasiento,)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------* Generos  Methods *-----------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        #**************************************************************#
        #                        * Generos  Methods *                 #
        #**************************************************************#

    def verify_genero(self,genero):
        try:
            sql = "SELECT * FROM generos WHERE genero LIKE " + "'" + genero + "';"
            self.cursor.execute(sql)
            record  = self.cursor.fetchone()
            if(record == None):
                return 0, True
            else:
                return 1062, False
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def create_newgenero(self,idgenero,genero):
        try:
            null, value = self.verify_genero(genero)
            if (value == True):
                sql = 'INSERT INTO generos(`id_genero`,`genero`) VALUES (%s,%s)'
                vals = (idgenero,genero)
                self.cursor.execute(sql,vals)
                self.cnx.commit()
                return True
            if(value == False):
                return null
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    def read_genero(self,idgenero): 
        try:
            sql = 'SELECT * FROM generos WHERE id_genero = %s'
            vals = (idgenero,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err
    
    def read_all_generos(self): 
        try:
            sql = 'SELECT * FROM generos'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err


    def update_genero(self,fields,vals):
        try:
            sql = 'UPDATE generos SET '+','.join(fields)+' WHERE id_genero = %s' 
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            print(err)
            return err

    def delete_genero(self,idgenero):
        try:
            sql = 'DELETE FROM generos WHERE id_genero = %s'
            vals = (idgenero,)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------* Peliculas_Generos  Methods *--------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


        #**************************************************************#
        #               * Peliculas_Generos  Methods *                 #
        #**************************************************************#
    def verify_pelicula_genero(self,idpelicula,idgenero):
        try:
            sql = "SELECT * FROM peliculas_generos WHERE id_pelicula LIKE " + "'" +idpelicula+ "'" + " AND id_genero LIKE " + "'" +idgenero+"';"
            self.cursor.execute(sql)
            record = self.cursor.fetchone()
            if(record == None):
                return 0,True
            else:
                return 1062,False
        except connector.Error as err:
            return err

    def create_new_pelicula_genero(self,idpelicula,idgenero):
        try:
            null, verify = self.verify_pelicula_genero(idpelicula,idgenero)
            if(verify == True):
                sql = 'INSERT INTO peliculas_generos(`id_pelicula`,`id_genero`) VALUES (%s,%s)'
                vals = (idpelicula,idgenero)
                self.cursor.execute(sql,vals)
                self.cnx.commit()
                return True
            if(verify == False):
                return null
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    def read_pelicula_genero(self,idpelicula,idgenero): 
        try:
            sql = 'SELECT peliculas.*, generos.* FROM peliculas_generos JOIN peliculas ON peliculas.id_pelicula = peliculas_generos.id_pelicula AND peliculas_generos.id_pelicula = %s JOIN generos ON generos.id_genero = peliculas_generos.id_genero AND peliculas_generos.id_genero = %s'
            vals = (idpelicula,idgenero)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err
    
    def read_all_peliculas_bygenero(self,genero): 
        try:
            sql = 'SELECT peliculas.*, generos.genero FROM peliculas_generos JOIN peliculas ON peliculas.id_pelicula = peliculas_generos.id_pelicula JOIN generos ON generos.id_genero = peliculas_generos.id_genero AND generos.genero = %s'
            vals = (genero,)
            self.cursor.execute(sql,vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_all_peliculas_generos(self):
        try:
            sql = 'SELECT peliculas.*, generos.* FROM peliculas_generos JOIN peliculas ON peliculas.id_pelicula = peliculas_generos.id_pelicula JOIN generos ON generos.id_genero = peliculas_generos.id_genero'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def update_peliculas_generos(self,fields,vals):
        try:
            sql = 'UPDATE peliculas_generos SET '+','.join(fields)+' WHERE id_pelicula = %s AND id_genero = %s'
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_peliculas_genero(self,idpelicula,idgenero):
        try:
            sql = 'DELETE FROM peliculas_generos WHERE id_pelicula = %s AND id_genero = %s'
            vals = (idpelicula,idgenero)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------* Peliculas_Salas  Methods *--------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    
        #**************************************************************#
        #               * Peliculas_Salas  Methods *                 #
        #**************************************************************#
    def verify_pelicula_sala(self,idpelicula,idsala):
        try:
            sql = "SELECT * FROM peliculas_salas WHERE id_pelicula LIKE " + "'" +idpelicula+ "'" + " AND id_sala LIKE " + "'" +idsala+"';"
            self.cursor.execute(sql)
            record = self.cursor.fetchone()
            if(record == None):
                return 0,True
            else:
                return 1062,False
        except connector.Error as err:
            return err

    def create_new_pelicula_sala(self,idpelicula,idsala):
        try:
            null, verify = self.verify_pelicula_sala(idpelicula,idsala)
            if(verify == True):
                sql = 'INSERT INTO peliculas_salas(`id_pelicula`,`id_sala`) VALUES (%s,%s)'
                vals = (idpelicula,idsala)
                self.cursor.execute(sql,vals)
                self.cnx.commit()
                return True
            if(verify == False):
                return null
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    def read_pelicula_sala(self,idpelicula,idsala): 
        try:
            sql = 'SELECT peliculas.*, salas.* FROM peliculas_salas JOIN peliculas ON peliculas.id_pelicula = peliculas_salas.id_pelicula AND peliculas_salas.id_pelicula = %s JOIN salas ON salas.id_sala = peliculas_salas.id_sala AND peliculas_salas.id_sala = %s'
            vals = (idpelicula,idsala)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err
    
    def read_all_pelisala_by_pelicula_nombre(self,nombre):
        try:
            sql = 'SELECT DISTINCT peliculas_salas.id_pelisala, peliculas.nombre, salas.tipo_sala FROM peliculas_salas JOIN salas ON salas.id_sala = peliculas_salas.id_sala JOIN peliculas ON peliculas.id_pelicula = peliculas_salas.id_pelicula AND peliculas.nombre = %s'
            vals = (nombre,)
            self.cursor.execute(sql,vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_all_peliculas_salas(self):
        try:
            sql = 'SELECT peliculas.*, salas.* FROM peliculas_salas JOIN peliculas ON peliculas.id_pelicula = peliculas_salas.id_pelicula JOIN salas ON salas.id_sala = peliculas_salas.id_sala'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def update_peliculas_salas(self,fields,vals):
        try:
            sql = 'UPDATE peliculas_salas SET '+','.join(fields)+' WHERE id_pelicula = %s AND id_sala = %s'
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_peliculas_sala(self,idpelicula,idsala):
        try:
            sql = 'DELETE FROM peliculas_salas WHERE id_pelicula = %s AND id_sala = %s'
            vals = (idpelicula,idsala)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err
    

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------* Peliculas_Horarios  Methods *--------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



        #**************************************************************#
        #               * Peliculas_Horarios  Methods *                #
        #**************************************************************#

    def verify_pelicula_horario(self,idpelicula,idhorario):
        try:
            sql = "SELECT * FROM peliculas_horarios WHERE id_pelicula LIKE " + "'" +idpelicula+ "'" + " AND id_horario LIKE " + "'" +idhorario+"';"
            self.cursor.execute(sql)
            record = self.cursor.fetchone()
            if(record == None):
                return 0,True
            else:
                return 1062,False
        except connector.Error as err:
            return err
    
    def create_new_pelicula_horario(self,idpelicula,idhorario,precio):
        try:
            null, verify = self.verify_pelicula_horario(idpelicula,idhorario)
            if(verify == True):
                sql = 'INSERT INTO peliculas_horarios(`id_pelicula`,`id_horario`,`precio`) VALUES (%s,%s,%s)'
                vals = (idpelicula,idhorario,precio)
                self.cursor.execute(sql,vals)
                self.cnx.commit()
                return True
            if(verify == False):
                return null
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    def read_pelicula_horario(self,idpelicula,idhorario): 
        try:
            sql = 'SELECT peliculas.*, horarios.*, peliculas_horarios.precio FROM peliculas_horarios JOIN peliculas ON peliculas.id_pelicula = peliculas_horarios.id_pelicula AND peliculas_horarios.id_pelicula = %s JOIN horarios ON horarios.id_horario = peliculas_horarios.id_horario AND peliculas_horarios.id_horario = %s'
            vals = (idpelicula,idhorario)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_all_pelicula_horarios(self):
        try:
            sql = 'SELECT peliculas.*, horarios.*, peliculas_horarios.precio FROM peliculas_horarios JOIN peliculas ON peliculas.id_pelicula = peliculas_horarios.id_pelicula JOIN horarios ON horarios.id_horario = peliculas_horarios.id_horario'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_all_peliculas_byhora(self,hora): 
        try:
            sql = 'SELECT peliculas.*, horarios.dia, horarios.hora, horarios.precio FROM peliculas_horarios JOIN peliculas ON peliculas.id_pelicula = peliculas_horarios.id_pelicula JOIN horarios ON horarios.id_horario = peliculas_horarios.id_horario AND horarios.hora = %s'
            vals = (hora,)
            self.cursor.execute(sql,vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def update_peliculas_horarios(self,fields,vals):
        try:
            sql = 'UPDATE peliculas_horarios SET '+','.join(fields)+' WHERE id_pelicula = %s AND id_horario = %s'
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            print(err)
            self.cnx.rollback()
            return err

    def delete_peliculas_horarios(self,idpelicula,idhorario):
        try:
            sql = 'DELETE FROM peliculas_horarios WHERE id_pelicula = %s AND id_horario = %s'
            vals = (idpelicula,idhorario)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------* Salas_Asientos  Methods *-------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



        #**************************************************************#
        #               * Salas_Asientos  Methods *                    #
        #**************************************************************#

    def verify_sala_asiento(self,idsala,idasiento):
        try:
            sql = "SELECT * FROM salas_asientos WHERE id_sala LIKE " + "'" +idsala+ "'" + " AND id_asiento LIKE " + "'" +idasiento+"';"
            self.cursor.execute(sql)
            record = self.cursor.fetchone()
            if(record == None):
                return 0,True
            else:
                return 1062,False
        except connector.Error as err:
            return err

    def create_new_sala_asiento(self,idsala,idasiento,estado_asiento,disponibilidad_asiento,estado_sala):
        try:
            null, verify = self.verify_sala_asiento(idsala,idasiento)
            if(verify == True):
                sql = 'INSERT INTO salas_asientos(`id_sala`,`id_asiento`,`estado_asiento`,`disponibilidad_asiento`,`estado_sala`) VALUES (%s,%s,%s,%s,%s)'
                vals = (idsala,idasiento,estado_asiento,disponibilidad_asiento,estado_sala)
                self.cursor.execute(sql,vals)
                self.cnx.commit()
                return True
            if(verify == False):
                return null
        except connector.Error as err:
            self.cnx.rollback()
            return err


    def read_sala_asiento(self,idsala,idasiento): 
        try:
            sql = 'SELECT salas.*, asientos.*, salas_asientos.estado_asiento,salas_asientos.disponibilidad_asiento, salas_asientos.estado_sala FROM salas_asientos JOIN salas ON salas.id_sala = salas_asientos.id_sala AND salas_asientos.id_sala = %s JOIN asientos ON asientos.id_asiento = salas_asientos.id_asiento AND salas_asientos.id_asiento = %s'
            vals = (idsala,idasiento)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_sala_by_numeroasientos(self,numeroasientos):
        try:
            sql = 'SELECT DISTINCT salas.* , salas_asientos.estado_sala FROM salas_asientos JOIN salas ON salas.id_sala = salas_asientos.id_sala AND salas.numero_asientos =  %s'
            vals = (numeroasientos,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            print(err)
            return err 

    
    def read_sala_numerosala_for_asientos(self,numerosala): 
        try:
            sql = 'SELECT DISTINCT salas.*, salas_asientos.estado_sala FROM salas_asientos JOIN salas ON salas.id_sala = salas_asientos.id_sala AND salas.numero_sala = %s'
            vals = (numerosala,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err


    def read_all_asientos_by_sala(self,numerosala): 
        try:
            sql = 'SELECT asientos.*, salas_asientos.estado_asiento,salas_asientos.disponibilidad_asiento FROM salas_asientos JOIN asientos ON asientos.id_asiento = salas_asientos.id_asiento JOIN salas ON salas.id_sala = salas_asientos.id_sala AND salas.numero_sala =  %s'
            vals = (numerosala,)
            self.cursor.execute(sql,vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_asientos_disponibles(self, numero_sala):
        try:
            sql = "SELECT asientos.fila,asientos.numero FROM salas_asientos JOIN salas ON salas.id_sala = salas_asientos.id_sala JOIN asientos ON asientos.id_asiento = salas_asientos.id_asiento AND salas_asientos.disponibilidad_asiento LIKE " + "'Disponible'" + "AND salas.numero_sala = %s"
            vals = (numero_sala,)
            self.cursor.execute(sql,vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def update_estado_asiento_ocupado(self,idsala,id_asiento):
        try:
            id_sala_asiento = self.read_sala_asiento_ticket(idsala,id_asiento)
            sql = "UPDATE salas_asientos SET disponibilidad_asiento = " +"'Ocupado'" + " WHERE id_sala_asiento = %s"
            vals = (id_sala_asiento,)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def update_estado_asiento_disponible(self,idsala,id_asiento):
        try:
            id_sala_asiento = self.read_sala_asiento_ticket(idsala,id_asiento)
            sql = "UPDATE salas_asientos SET disponibilidad_asiento = " +"'Disponible'" + " WHERE id_sala_asiento = %s "
            vals = (id_sala_asiento,)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            print(err)
            return err

    def update_salas_asientos(self,fields,vals):
        try:
            sql = 'UPDATE salas_asientos SET '+','.join(fields)+' WHERE id_sala = %s AND id_asiento = %s'
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_asiento_sala(self,idsala,idasiento):
        try:
            sql = 'DELETE FROM salas_asientos WHERE id_sala = %s AND id_asiento = %s'
            vals = (idsala,idasiento)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------* TICKETS  Methods *-----------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        #**************************************************************#
        #                      * TICKETS  Methods *                    #
        #**************************************************************#

    def create_new_ticket(self,id_pelicula_horario,id_sala_asiento):
        try:
            sql = 'INSERT INTO tickets(`id_pelihorario`,`id_sala_asiento`) VALUES (%s,%s)'
            vals = (id_pelicula_horario,id_sala_asiento)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err        

    def read_sala_asiento_ticket(self,idsala,idasiento): 
        try:
            sql = 'SELECT salas_asientos.id_sala_asiento FROM salas_asientos WHERE id_sala = %s AND id_asiento = %s'
            vals = (idsala,idasiento)
            self.cursor.execute(sql, vals)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            if(record == None):
                return None
            return record[0]
        except connector.Error as err:
            return err    

    def read_pelicula_horario_ticket(self,idpelicula,id_horario): 
        try:
            sql = 'SELECT * FROM peliculas_horarios WHERE id_pelicula = %s AND id_horario = %s'
            vals = (idpelicula,id_horario)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            if(record == None):
                return None
            return record[0]
        except connector.Error as err:
            return err    

    def read_all_pelihorarios_ticket(self):
        try:
            sql = 'SELECT peliculas_horarios.id_pelihorario, peliculas.*, horarios.*, peliculas_horarios.precio FROM peliculas_horarios JOIN peliculas ON peliculas.id_pelicula = peliculas_horarios.id_pelicula JOIN horarios ON horarios.id_horario = peliculas_horarios.id_horario'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_ticket(self,idticket): 
        try:
            sql = 'SELECT * FROM tickets WHERE id_ticket = %s'
            vals = (idticket,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err
    
    def read_ticket_by_phsa(self,ph,sa):
        try:
            sql = 'SELECT * FROM tickets WHERE id_pelihorario = %s AND id_sala_asiento = %s'
            vals = (ph,sa)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_ticket_information(self,id_peli_horario,id_sala_asiento): 
        try:
            sql = 'SELECT tickets.id_ticket,peliculas.nombre, horarios.dia, horarios.hora, salas.numero_sala, asientos.fila, asientos.numero, peliculas_horarios.precio FROM tickets JOIN peliculas_horarios ON peliculas_horarios.id_pelihorario = tickets.id_pelihorario AND tickets.id_pelihorario = %s JOIN salas_asientos ON salas_asientos.id_sala_asiento = tickets.id_sala_asiento AND tickets.id_sala_asiento = %s JOIN peliculas ON peliculas.id_pelicula = peliculas_horarios.id_pelicula JOIN horarios ON horarios.id_horario = peliculas_horarios.id_horario JOIN salas ON salas.id_sala = salas_asientos.id_sala JOIN asientos ON asientos.id_asiento = salas_asientos.id_asiento'
            vals = (id_peli_horario,id_sala_asiento)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchone()
            return records
        except connector.Error as err:
            return err
    #MUESTRA TABLA TICKETS CON LAS RELACIONES DIRECTAS ENTRE PELICULAS-HORARIOS Y SALAS-ASIENTOS
    def read_all_tickets(self): 
        try:
            sql = 'SELECT * FROM tickets'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def update_ticket(self,fields,vals):
        try:
            print("SQL")
            sql = 'UPDATE tickets SET '+','.join(fields)+' WHERE id_pelihorario = %s AND id_sala_asiento = %s'
            print(sql)
            print("EXECUTE")
            self.cursor.execute(sql,vals)
            print("COMMIT")
            self.cnx.commit()
            return True
        except connector.Error as err:
            print(err)
            self.cnx.rollback()
            return err

    def delete_ticket(self,id_pelihorario,id_sala_asiento):
        try:
            sql = 'DELETE FROM tickets WHERE id_pelihorario = %s AND id_sala_asiento = %s'
            vals = (id_pelihorario,id_sala_asiento)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------* Compras  Methods *-----------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        #**************************************************************#
        #               * Compras  Methods *                           #
        #**************************************************************#

    def create_new_compra(self,id_ticket,id_usuario):
        try:
            sql = 'INSERT INTO compras(`id_ticket`,`id_usuario`) VALUES (%s,%s)'
            vals = (id_ticket,id_usuario)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_compra(self,idcompra): 
        try:
            sql = 'SELECT * FROM compras WHERE id_compra = %s'
            vals = (idcompra,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_all_compras(self): 
        try:
            sql = 'SELECT * FROM compras'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_compra_byuser_ticket(self,id_ticket,id_usuario):
        try:
            sql = 'SELECT * FROM compras WHERE id_ticket = %s AND id_usuario = %s'
            vals = (id_ticket,id_usuario)
            self.cursor.execute(sql,vals)
            records = self.cursor.fetchone()
            return records[0]
        except connector.Error as err:
            return err

    def read_compra_information(self,i_compra):
        try:    
            sql = 'SELECT compras.id_compra, tickets.id_ticket, peliculas.nombre, horarios.dia, horarios.hora, salas.numero_sala,asientos.fila,asientos.numero,peliculas_horarios.precio FROM compras JOIN tickets ON tickets.id_ticket = compras.id_ticket JOIN peliculas_horarios ON peliculas_horarios.id_pelihorario = tickets.id_pelihorario JOIN salas_asientos ON salas_asientos.id_sala_asiento = tickets.id_sala_asiento JOIN peliculas ON peliculas.id_pelicula = peliculas_horarios.id_pelicula JOIN horarios ON horarios.id_horario = peliculas_horarios.id_horario JOIN salas ON salas.id_sala = salas_asientos.id_sala JOIN asientos ON asientos.id_asiento = salas_asientos.id_asiento AND id_compra = %s'
            vals = (i_compra,)
            self.cursor.execute(sql,vals)
            records = self.cursor.fetchone()
            return records
        except connector.Error as err:
            return err

    def update_compra(self,fields,vals):
        try:
            sql = 'UPDATE compras SET '+','.join(fields)+' WHERE id_ticket = %s AND id_usuario = %s'
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            print(err)
            return err

    def delete_compra(self,idticket,idusuario):
        try:
            sql = 'DELETE FROM compras WHERE id_ticket = %s AND id_usuario = %s'
            vals = (idticket,idusuario)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------* Verification  Methods *----------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        #**************************************************************#
        #               * Verification  Methods *                      #
        #**************************************************************#
    
    def user_verification_user(self,user):
        try:
            sql = 'SELECT * FROM usuarios WHERE usuario LIKE ' + "'" + user + "';"
            self.cursor.execute(sql)
            record = self.cursor.fetchone()
            if(record != None):
                return True       
        except connector.Error as err:
            return err
    
    #VERIFICAMOS QUE TIPO DE USUARIO SE LOGUEA EN EL SISTEMA (ADMIN O USUARIO)
    def user_verification(self,user):
        name_user, this_user = self.read_thisuser_byuser(user)
        name_admin, this_admin = self.read_thisadmin_byadmin(user)
        if(this_user == True):
            return 1,name_user
        elif(this_admin == True):
            return 0,name_admin
        else:
            return ("No se ecuentra este usuario."),False

    #VERIFICAMOS SI LAS CONTRASEÑAS SON IGUALES QUE LAS REGISTRADAS EN LA BASE DE DATOS
    def password_verification(self,user,user_type,password):
        if(user_type == 1):
            pass_verify = self.read_user_byuser(user,password)
            if(pass_verify == True):
                return True
            else:
                return False
        else:
            pass_verify = self.read_admin_byadmin(user,password)
            if(pass_verify == True):
                return True
            else:
                return False

    def password_verification_compra(self,idusuario,password):
        try:
            sql = "SELECT usuarios.pass FROM usuarios WHERE id_usuario = %s"
            vals = (idusuario,)
            self.cursor.execute(sql,vals)
            record = self.cursor.fetchall()
            if(password == str(record[0][0])):
                return True
            else:
                return 'CONTRASEÑA INCORRECTA'
        except connector.Error as err:
            return err

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------* USERS *----------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def cartelera(self):
        try:
            sql = 'SELECT DISTINCT peliculas.nombre, horarios.dia, horarios.hora, peliculas_horarios.precio FROM peliculas_horarios JOIN peliculas ON peliculas.id_pelicula = peliculas_horarios.id_pelicula JOIN horarios ON horarios.id_horario = peliculas_horarios.id_horario ORDER BY peliculas.nombre;'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err


    def read_pelicula_nombre_cartelera(self,nombre):
        try:
            sql = "SELECT DISTINCT peliculas.nombre, horarios.dia, horarios.hora, peliculas_horarios.precio FROM peliculas_horarios JOIN horarios ON horarios.id_horario = peliculas_horarios.id_horario JOIN peliculas ON peliculas.id_pelicula = peliculas_horarios.id_pelicula AND peliculas.nombre LIKE " + "'%" + nombre + "%';"
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_pelicula_genero_cartelera(self,genero):
        try:
            sql = "SELECT DISTINCT peliculas.nombre, horarios.dia, horarios.hora, peliculas_horarios.precio FROM peliculas_horarios JOIN peliculas ON peliculas.id_pelicula = peliculas_horarios.id_pelicula JOIN horarios ON horarios.id_horario = peliculas_horarios.id_horario JOIN peliculas_generos ON peliculas.id_pelicula = peliculas_generos.id_pelicula JOIN generos ON generos.id_genero = peliculas_generos.id_genero AND generos.genero LIKE " + "'" + genero + "' ORDER BY horarios.dia;"
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err
    
    def read_pelicula_nombre_compra(self,nombre):
        try:
            sql = "SELECT DISTINCT * FROM peliculas WHERE nombre LIKE "
            sql += "'%" + nombre + "%';"
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_sala_by_idpelisa(self,id_pelisala):
        try:
            sql = "SELECT peliculas_salas.id_sala FROM peliculas_salas WHERE id_pelisala = %s"
            vals = (id_pelisala,)
            self.cursor.execute(sql,vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_numero_asientos(self,id_sala):
        try:
            sql = "SELECT salas.numero_asientos FROM salas WHERE id_sala = %s AND "
            vals = (id_sala,)
            self.cursor.execute(sql,vals)
            record = self.cursor.fetchone()
            return record[0]
        except connector.Error as err:
            return err
    
    def read_asiento_by_fila_asiento(self,fila,numero):
        try:
            sql = "SELECT asientos.id_asiento FROM asientos WHERE fila = %s AND numero = %s"
            vals = (fila,numero)
            self.cursor.execute(sql,vals)
            record = self.cursor.fetchone()
            return record[0]
        except connector.Error as err:
            return err

    def read_thisuser_byuser_compra(self,user):
        try:
            sql = 'SELECT * FROM usuarios WHERE usuario LIKE ' + "'" + user + "';"
            self.cursor.execute(sql)
            record = self.cursor.fetchone()
            return record[0]       
        except connector.Error as err:
            return err

    def read_pelicula_nombre_cartelera_compra(self,nombre):
        try:
            sql = "SELECT DISTINCT peliculas.nombre, horarios.dia, horarios.hora, peliculas_horarios.precio, peliculas_horarios.id_pelihorario FROM peliculas_horarios JOIN horarios ON horarios.id_horario = peliculas_horarios.id_horario JOIN peliculas ON peliculas.id_pelicula = peliculas_horarios.id_pelicula AND peliculas.nombre LIKE " + "'%" + nombre + "%';"
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_pelicula_by_pelihorario(self,id_pelicula_horario):
        try:
            sql = 'SELECT peliculas_horarios.id_pelicula FROM peliculas_horarios WHERE id_pelihorario = %s'
            vals = (id_pelicula_horario,)
            self.cursor.execute(sql,vals)
            record = self.cursor.fetchone()
            return record[0]         
        except connector.Error as err:
            return err


    def read_boleto_comprado(self,i_compra):
        try:
            sql = 'SELECT compras.id_compra, tickets.id_ticket, peliculas.nombre, horarios.dia, horarios.hora, salas.numero_sala,asientos.fila,asientos.numero,peliculas_horarios.precio, usuarios.* FROM compras JOIN tickets ON tickets.id_ticket = compras.id_ticket JOIN peliculas_horarios ON peliculas_horarios.id_pelihorario = tickets.id_pelihorario JOIN salas_asientos ON salas_asientos.id_sala_asiento = tickets.id_sala_asiento JOIN peliculas ON peliculas.id_pelicula = peliculas_horarios.id_pelicula JOIN horarios ON horarios.id_horario = peliculas_horarios.id_horario JOIN salas ON salas.id_sala = salas_asientos.id_sala JOIN asientos ON asientos.id_asiento = salas_asientos.id_asiento JOIN usuarios ON usuarios.id_usuario = compras.id_usuario AND id_compra = %s'
            vals = (i_compra,)
            self.cursor.execute(sql,vals)
            record = self.cursor.fetchone()
            return record         
        except connector.Error as err:
            return err




