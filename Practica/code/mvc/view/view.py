from model.model import Model

m = Model()

class View:

    """
    """""""""""""""""""""""""""""
    "   A view for a CineDB  "
    """"""""""""""""""""""""""""
    """


    def start(self,user,string):
        print('*'*(len(str(user))+len(user)+24))
        print("¡Bienvenido!".center(len(user)+5),' - ' + str(user) + ' - ' + str(string))
        print('*'*(len(str(user))+len(user)+24))
        

    def end(self):
        print("************************")
        print("*    ¡Hasta pronto!    *")
        print("************************")

    def option(self, last):
        print("Selecciona una opcion (1 - " + last + '): ', end="")
    
    def not_valid_option(self):
        print("¡Opción no valida.!")
    
    def ask(self, output):
        print(output, end="")
    
    def msg(self,output):
        print(output)

    def ok(self, name, op):
        print('+'*(len(str(name))+len(op)+24))
        print('+ ¡'+str(name)+ ' se '+op+' correctamente! + ')
        print('+'*(len(str(name))+len(op)+24))
    

    def ok_double_id(self, id1, id2, op):
        print('+'*(len(str(id1))+len(op)+24))
        print('+ ¡'+str(id1)+ ' y ' + str(id2) + ' se '+op+' correctamente! + ')
        print('+'*(len(str(id1))+len(op)+24))

    def error(self,err):
        print(' ¡ERROR! '.center(len(err)+4,'-'))
        print('- '+err+' -')
        print('-'*(len(err)+4))

    #Menu desplegable si el LOGIN es de un Administrador
    def main_menu_admin(self):
        print("""""""""""""""""""""""""")
        print(" -- Menú Principal   --  ")
        print("""""""""""""""""""""""""")

        print("1. Administrar Usuarios")
        print("2. Administrar Empleados")
        print("3. Administrar Peliculas")
        print("4. Administrar Generos")
        print("5. Administrar Horarios")
        print("6. Administrar Salas")
        print("7. Administrar Asientos")
        print("8. Administrar Peliculas - Horarios")
        print("9. Administrar Peliculas - Generos")
        print("10. Administrar Salas - Asientos")
        print("11. Administrar Peliculas - Salas")
        print("12. Administrar Boletos")
        print("13. Administrar Compras")
        print("14. Salir")
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------View for Users--------------------------------------------------------------------------------------------------------------------------------------------------------

    #******************************************#
    #           View for Users           #
    #******************************************# 

    def users_menu(self):
        print("*************************************")
        print("*     * -- Submenú Usuarios -- *    *")
        print("*************************************")
        print("1. Agregar usuario")
        print("2. Actualizar usuario")
        print("3. Eliminar usuario")
        print("4. Buscar usuario por clave de usuario")
        print("5. Buscar usuario(s) por nombre")
        print("6. Buscar usuario por nombre de usuario")
        print("7. Ver todos los usuarios registrados")
        print("8. Salir")

    def ver_usuario(self,record):
        print("ID Usuario: ", record[0])
        print("Nombre: ", record[1])
        print("Correo: ", record[2])
        print("Tipo de usuario: ", record[3])
        print("Nombre de usuario: ", record[4])
    
    def ver_usuario_header(self, header):
        print(str(header).center(180,'*'))
        print('-'*180)

    def ver_usuario_midder(self):
        print('/'*180)

    def ver_usuario_footer(self):
        print('*'*180)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------View for Admins-------------------------------------------------------------------------------------------------------------------------------------------------------

    #******************************************#
    #           View for Admins           #
    #******************************************# 

    def admin_menu(self):
        print("*************************************")
        print("*     * -- Submenú Empleados -- *    *")
        print("*************************************")
        print("1. Agregar empleado")
        print("2. Actualizar empleado")
        print("3. Eliminar empleado")
        print("4. Buscar empleado por clave de empleado")
        print("5. Buscar empleado(s) por nombre")
        print("6. Buscar empleado por nombre de usuario")
        print("7. Ver todos los empleados")
        print("8. Salir")

    def ver_admin(self,record):
        print("ID Empleado: ", record[0])
        print("Nombre: ", record[1])
        print("Correo: ", record[2])
        print("Dirección: ", record[3])
        print("Teléfono: ", record[4])
        print("Usuario: ", record[5])
    
    def ver_admin_header(self, header):
        print(str(header).center(180,'*'))
        print('-'*180)

    def ver_admin_midder(self):
        print('/'*180)

    def ver_admin_footer(self):
        print('*'*180)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------View for Movies------------------------------------------------------------------------------------------------------------------------------------------------------

    #******************************************#
    #              View for Movies             #
    #******************************************# 
    
    def movies_menu(self):
        print("*************************************")
        print("*    * -- Submenú Peliculas -- *    *")
        print("*************************************")
        print("1. Agregar pelicula")
        print("2. Actualizar pelicula")
        print("3. Eliminar pelicula")
        print("4. Ver todas las peliculas")
        print("5. Buscar pelicula por id")
        print("6. Buscar pelicula por nombre")
        print("7. Regresar al menú principal")

    def ver_movie(self,record):
        print('ID:',record[0])
        print('Nombre:',record[1])
        print('Sipnosis:',record[2])
        print('Lanzamiento:',record[3])

    def ver_movie_header(self, header):
        print(header.center(78,'*'))
        print('-'*78)

    def ver_movie_midder(self):
        print('-'*78)

    def ver_movie_footer(self):
        print('*'*78)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------View for Generos------------------------------------------------------------------------------------------------------------------------------------------------------

    #******************************************#
    #              View for Generos            #
    #******************************************#     

    def generos_menu(self):
        print("*************************************")
        print("*     * -- Submenú Generos -- *     *")
        print("*************************************")
        print("1. Agregar genero")
        print("2. Actualizar genero")
        print("3. Eliminar genero")
        print("4. Buscar genero por clave")
        print("5. Ver todos los generos")
        print("6. Regresar al menú principal")

    def ver_genero(self,record):
        print('ID:',record[0])
        print('Genero:',record[1])


    def ver_genero_header(self, header):
        print(header.center(48,'*'))
        print('-'*48)

    def ver_genero_midder(self):
        print('-'*48)

    def ver_genero_footer(self):
        print('*'*48)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------View for Horarios-----------------------------------------------------------------------------------------------------------------------------------------------------

    #******************************************#
    #              View for Horarios           #
    #******************************************#

    def horarios_menu(self):
        print("*************************************")
        print("*     * -- Submenú Horarios -- *    *")
        print("*************************************")
        print("1. Agregar horario")
        print("2. Actualizar horario")
        print("3. Eliminar horario")
        print("4. Buscar horario por clave")
        print("5. Ver todos los horarios")
        print("6. Regresar al menú principal")

    def ver_horario(self,record):
        print('ID:',record[0])
        print('Fecha:',record[1])
        print('Hora:',record[2])


    def ver_horario_header(self, header):
        print(header.center(48,'*'))
        print('-'*48)

    def ver_horario_midder(self):
        print('-'*48)

    def ver_horario_footer(self):
        print('*'*48)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------View for Salas-------------------------------------------------------------------------------------------------------------------------------------------------------

    #******************************************#
    #              View for Salas              #
    #******************************************#

    def salas_menu(self):
        print("*************************************")
        print("*     * -- Submenú Salas -- *     *")
        print("*************************************")
        print("1. Agregar sala")
        print("2. Actualizar sala")
        print("3. Eliminar sala")
        print("4. Buscar sala por clave")
        print("5. Buscar sala por numero de sala")
        print("6. Ver todas los salas")
        print("7. Regresar al menú principal")

    def ver_sala(self,record):
        print('ID:',record[0])
        print('Numero de sala:',record[1])
        print('Sala tipo:',record[2])
        print('Asientos en la sala:', record[3])

    def ver_sala_header(self, header):
        print(header.center(48,'*'))
        print('-'*48)

    def ver_sala_midder(self):
        print('-'*48)

    def ver_sala_footer(self):
        print('*'*48)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------View for Asientos--------------------------------------------------------------------------------------------------------------------------------------------------

    #******************************************#
    #              View for Asientos           #
    #******************************************#

    def asientos_menu(self):
        print("*************************************")
        print("*     * -- Submenú Asientos -- *    *")
        print("*************************************")
        print("1. Agregar asiento")
        print("2. Actualizar asiento")
        print("3. Eliminar asiento")
        print("4. Buscar asiento por clave")
        print("5. Ver todas los asientos")
        print("6. Regresar al menú principal")

    def ver_asiento(self,record):
        print('ID:',record[0])
        print('Fila de asiento:',record[1])
        print('Numero Asiento:',record[2])

    def ver_asiento_header(self, header):
        print(header.center(48,'*'))
        print('-'*48)

    def ver_asiento_midder(self):
        print('-'*48)

    def ver_asiento_footer(self):
        print('*'*48)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------View for Peliculas-Horarios-----------------------------------------------------------------------------------------------------------------------------------------

    #******************************************#
    #       View for Peliculas-Horarios        #
    #******************************************#

    def pelihorario_menu(self):
        print("***********************************************")
        print("*     * -- Submenú Peliculas-Horarios -- *    *")
        print("***********************************************")
        print("1. Agregar Nueva Pelicula - Horario")
        print("2. Actualizar Pelicula - Horario")
        print("3. Eliminar Pelicula - Horario")
        print("4. Buscar Pelicula - Horario por clave")
        print("5. Ver todas los Peliculas - Horarios")
        print("6. Regresar al menú principal")

    def ver_pelihorario(self,record):
        print('ID Pelicula:',record[0])
        print('ID Horario:',record[4])
        print("Precio: ", record[7])
        print("Datos de la pelicula".center(81,'*'))
        self.ver_movie(record[0:4])
        print("Datos del horario".center(81,'*'))
        self.ver_horario(record[4:7])

    def ver_pelihorario_ticket(self,record):
        print("******************+++*****+***+**")
        print('ID Pelicula - Horario', record[0])
        print("******************+++*****+***+**")
        print('ID Pelicula:',record[1])
        print('ID Horario:',record[5])
        print("Precio: ", record[8])
        print("Datos de la pelicula".center(81,'*'))
        self.ver_movie(record[1:5])
        print("Datos del horario".center(81,'*'))
        self.ver_horario(record[5:8])

    def ver_pelihorario_header(self, header):
        print(header.center(48,'*'))
        print('-'*48)

    def ver_pelihorario_midder(self):
        print('-'*48)

    def ver_pelihorario_footer(self):
        print('*'*48)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------View for Peliculas-Generos------------------------------------------------------------------------------------------------------------------------------------------

    #******************************************#
    #       View for Peliculas-Generos        #
    #******************************************#

    def peligenero_menu(self):
        print("***********************************************")
        print("*     * -- Submenú Peliculas-Generos -- *    *")
        print("***********************************************")
        print("1. Agregar Nueva Pelicula - Genero")
        print("2. Actualizar Pelicula - Genero")
        print("3. Eliminar Pelicula - Genero")
        print("4. Buscar Pelicula - Genero por clave")
        print("5. Ver todas los Peliculas - Generos")
        print("6. Regresar al menú principal")

    def ver_peligenero(self,record):
        print('ID Pelicula:',record[0])
        print('ID Genero:',record[4])
        print("Datos de la pelicula".center(81,'*'))
        self.ver_movie(record[0:4])
        print("Datos del genero".center(81,'*'))
        self.ver_genero(record[4:])

    def ver_peligenero_header(self, header):
        print(header.center(48,'*'))
        print('-'*48)

    def ver_peligenero_midder(self):
        print('-'*48)

    def ver_peligenero_footer(self):
        print('*'*48)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------View for Salas - Asientos-------------------------------------------------------------------------------------------------------------------------------------------

    #******************************************#
    #       View for Salas - Asientos          #
    #******************************************#

    def sala_asiento_menu(self):
        print("*******************************************")
        print("*     * -- Submenú Salas-Asientos -- *    *")
        print("*******************************************")
        print("1. Agregar Nueva Sala - Asiento")
        print("2. Actualizar Sala - Asiento")
        print("3. Actualizar Estado Asiento")
        print("4. Eliminar Sala - Asiento")
        print("5. Buscar Sala - Asiento por clave")
        print("6. Buscar Sala por numero de asientos")
        print("7. Ver todos los asientos de una sala")
        print("8. Regresar al menú principal")

    def ver_sala_asiento(self,record):
        print('ID Sala:',record[0])
        print('ID Asiento:',record[4])
        print("Datos de la Sala".center(81,'*'))
        print('Estado de la Sala: ', record[9])
        self.ver_sala(record[0:4])
        print("Datos de los Asientos".center(81,'*'))
        print('Estado del asiento: ', record[7])
        print('Disponibilidad del Asiento: ',record[8])
        self.ver_asiento(record[4:7])

    def ver_sala_asiento_by_numero_asientos(self,record):
        print("Datos de la Sala".center(81,'*'))
        print('Estado de la Sala: ', record[4])
        self.ver_sala(record[0:4])

    def ver_sala_asiento_asientos_a_sala(self,record):
        print("******************************************")
        print('Estado del asiento: ', record[3])
        print('Disponibilidad del Asiento: ',record[4])
        self.ver_asiento(record[0:3])
        print("******************************************")

    def ver_sala_asientos_byasiento_a_sala(self,record):
        print("Datos de la Sala".center(81,'*'))
        print('ID:',record[0])
        print('Estado de la Sala: ', record[4])
        print('Numero de sala:',record[1])
        print('Sala tipo:',record[2])
        print('Asientos en la sala:', record[3])
        print("Datos de los Asientos".center(81,'*'))



    def ver_sala_asiento_header(self, header):
        print(header.center(48,'*'))
        print('-'*48)

    def ver_sala_asiento_midder(self):
        print('-'*48)

    def ver_sala_asiento_footer(self):
        print('*'*48)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------View for Peliculas - Salas-------------------------------------------------------------------------------------------------------------------------------------------

    #******************************************#
    #       View for Peliculas-Salas           #
    #******************************************#

    def pelisala_menu(self):
        print("***********************************************")
        print("*     * -- Submenú Peliculas- Salas -- *    *")
        print("***********************************************")
        print("1. Agregar Nueva Pelicula - Sala")
        print("2. Actualizar Pelicula - Sala")
        print("3. Eliminar Pelicula - Sala")
        print("4. Buscar Pelicula - Sala por clave")
        print("5. Ver todas los Peliculas - Salas")
        print("6. Regresar al menú principal")

    def ver_pelisala(self,record):
        print('ID Pelicula:',record[0])
        print('ID Sala:',record[4])
        print("Datos de la pelicula".center(81,'*'))
        self.ver_movie(record[0:4])
        print("Datos del Sala".center(81,'*'))
        self.ver_sala(record[4:])

    def ver_pelisala_compra(self,record):
        print("**************************************")
        print("Clave: ",record[0])
        print("Nombre de la pelicula: ",record[1])
        print("Tipo de sala: ", record[2])
        print("**************************************")

    def ver_pelisala_header(self, header):
        print(header.center(48,'*'))
        print('-'*48)

    def ver_pelisala_midder(self):
        print('-'*48)

    def ver_pelisala_footer(self):
        print('*'*48)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------View for Ticekts----------------------------------------------------------------------------------------------------------------------------------------------------

    #******************************************#
    #              View for Tickets            #
    #******************************************#

    def tickets_menu(self):
        print("*************************************")
        print("*     * -- Submenú Boletos -- *    *")
        print("*************************************")
        print("1. Agregar boleto")
        print("2. Actualizar boleto")
        print("3. Eliminar boleto")
        print("4. Buscar boleto detallado por clave")
        print("5. Ver todos los boletos")
        print("6. Regresar al menú principal")

    def ver_ticket(self,record):
        print('ID:',record[0])
        print('Nombre de la pelicula: ',record[1])
        print('Fecha: ',record[2])
        print('Hora: ',record[3])
        print('Sala: ',record[4])
        print('Asiento: ' + str(record[5]) + " " + str(record[6]))
        print('Costo: ',record[7])
        print('*******************************')

    def ver_ticket_header(self, header):
        print(header.center(48,'*'))
        print('-'*48)

    def ver_ticket_midder(self):
        print('-'*48)

    def ver_ticket_footer(self):
        print('*'*48)


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  #Menu desplegable si el LOGIN es de un usuario
    def main_menu_users(self):
        print("""""""""""""""""""""""""")
        print(" -- Menú Principal   --  ")
        print("""""""""""""""""""""""""")

        print("1. Ver cartelera")
        print("2. Buscar una pelicula por nombre")
        print("3. Buscar una pelicula por genero")
        print("4. Comprar boleto")
        print("5. Buscar una compra")
        print("6. Salir")
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------View for Cartelera------------------------------------------------------------------------------------------------------------------------------------------------

    def ver_cartelera(self,record):
        print("************************************************")
        print("Nombre de la pelicula: ", record[0])
        print("Fecha: ", record[1])
        print("Hora: ", record[2])
        print("Precio: ",record[3] )
        print("************************************************")

    def ver_cartelera_compra(self,record):
        print("************************************************")
        print("Clave: ", record[4])
        print("Nombre de la pelicula: ", record[0])
        print("Fecha: ", record[1])
        print("Hora: ", record[2])
        print("Precio: ",record[3] )
        print("************************************************")


    def ver_cartelera_header(self, header):
        print(header.center(48,'*'))
        print('-'*48)

    def ver_cartelera_midder(self):
        print('-'*48)

    def ver_cartelera_footer(self):
        print('*'*48)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------View for Compra------------------------------------------------------------------------------------------------------------------------------------------------

    def compras_menu(self):
        print("*************************************")
        print("*     * -- Submenú Compras -- *    *")
        print("*************************************")
        print("1. Actualizar compra")
        print("2. Eliminar compra")
        print("3. Buscar compras detallada por clave")
        print("4. Ver todos los compras")
        print("5. Regresar al menú principal")


    def ver_compra(self,record):
        print("************************************************")
        print("CLAVE DE COMPRA PARA ENTREGAR AL CINE: ",record[0])
        print("CLAVE DE TICKET: ", record[1])
        print("Nombre de la pelicula: ", record[2])
        print("Fecha: ", record[3])
        print("Hora: ", record[4])
        print("Sala: ", record[5])
        print("Fila: ",record[6], " Asiento: ", record[7])
        print("Usted pago: ", record[8])
        print("************************************************")

    def ver_clave_cine(self,i_compra):
        print("*".center(20,'*'))
        print(i_compra.center(20,'*'))
        print("*".center(20,'*'))

    def ver_compra_header(self, header):
        print(header.center(48,'*'))
        print('-'*48)

    def ver_compra_midder(self):
        print('-'*48)

    def ver_boleto_comprado(self,record):
        print("************************************************")
        print("DATOS DEL USUARIO".center(48,'+'))
        self.ver_usuario(record[8:])
        print("************************************************")
        print("CLAVE DE COMPRA PARA ENTREGAR AL CINE: ",record[0])
        print("CLAVE DE TICKET: ", record[1])
        print("Nombre de la pelicula: ", record[2])
        print("Fecha: ", record[3])
        print("Hora: ", record[4])
        print("Sala: ", record[5])
        print("Fila: ",record[6], " Asiento: ", record[7])
        print("Usted pago: ", record[8])
        print("************************************************")


    def ver_compra_footer(self):
        print('*'*48)