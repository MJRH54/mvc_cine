from model.model import Model
from view.view import View
from datetime import date

class Controller():

      
    #*****************************#
    #  A Controller for a CineDB  #
    #*****************************#

    def __init__(self):
        self.model = Model()
        self.view = View()

    def start(self):
        name, string = self.user_verification()
        while(name == None and string == None):
            name, string = self.user_verification()
        self.view.start(name,string)
        if(string.lower() == 'usuario'):
            self.main_menu_user()
        else:
            self.main_menu_admin()



    def user_verification(self):
        print("Usuario: ")
        user = input()
        verification,name = self.model.user_verification(user)
        if(verification == 1):
            print("Contraseña: ")
            password = input()
            access = self.model.password_verification(user,1,password)
            if(access == True):
                string = 'USUARIO'
                return [name,string]
            else:
                print("Problema de autenticación. Contraseña Incorrecta")
                return None,None
        elif(verification == 0):
            print("Contraseña: ")
            password = input()
            access = self.model.password_verification(user,0,password)
            if(access == True):
                string = 'ADMINISTRADOR'
                return [name,string]
            else:
                print("Problema de autenticación. Contraseña Incorrecta")
                return None,None
        else:
            print(verification)
            return None,None
            




    #*****************************#
    #     General controllers     #
    #*****************************#


    def main_menu_admin(self):
        o  = '0'
        while(o != '14'):
            self.view.main_menu_admin()
            self.view.option('14')
            o = input()
            if (o == '1'):
                self.admin_users_menu()
            elif(o == '2'):
                self.admin_admin_menu()
            elif(o == '3'):
                self.admin_movies_menu()
            elif(o == '4'):
                self.admin_generos_menu()
            elif(o == '5'):
                self.admin_horarios_menu()
            elif(o == '6'):
                self.admin_salas_menu()
            elif(o == '7'):
                self.admin_asientos_menu()
            elif(o == '8'):
                self.admin_peliculas_horarios_menu()
            elif(o == '9'):
                self.admin_peliculas_generos_menu()
            elif(o == '10'):
                self.admin_salas_asientos_menu()
            elif(o == '11'):
                self.admin_peliculas_salas_menu()
            elif(o == '12'):
                self.admin_boletos_menu()
            elif(o == '13'):
                self.admin_compras_menu()
            elif(o == '14'):
                self.view.end()
            else:
                self.view.not_valid_option()
        return
    
    def main_menu_user(self):
        o  = '0'
        while(o != '6'):
            self.view.main_menu_users()
            self.view.option('6')
            o = input()
            if (o == '1'):
                self.ver_cartelera()
            elif(o == '2'):
                self.ver_pelicula_nombre_cartelera()
            elif(o == '3'):
                self.ver_pelicula_genero_cartelera()
            elif(o == '4'):
                self.comprar_boleto()
            elif(o == '5'):
                self.buscar_boleto()
            elif(o == '6'):
                self.view.end()
            else:
                self.view.not_valid_option()
        return
    
    def update_lists(self,fs,vs):
        fields = []
        vals = []
        for f,v in zip(fs,vs):
            if(v!= ''):
                fields.append(f + ' = %s')
                vals.append(v)
        return fields, vals


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------CONTROLLER FOR ADMINS----------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------USERS---------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    #*****************************#
    #      Controller Users       #
    #*****************************#
    
    def admin_users_menu(self):
        o = '0'
        while(o != '8'):
            self.view.users_menu()
            self.view.option('8')
            o = input()
            if (o == '1'):
                self.create_user()
            elif(o == '2'):
                self.update_user()
            elif(o == '3'):
               self.delete_user()
            elif(o == '4'):
               self.read_user_byid()
            elif(o == '5'):
               self.read_user_byname()
            elif(o == '6'):
               self.read_user_byuser()
            elif(o == '7'):
               self.read_all_users()
            elif(o == '8'):
                self.view.end()
            else:
                self.view.not_valid_option()
        return
    
    def ask_user(self):
        self.view.ask('Nombre: ')
        Nombre = input()
        self.view.ask('Correo: ')
        Correo = input()
        self.view.ask('Tipo de usuario: ')
        T_Usuario =  input()
        self.view.ask('Nombre usuario: ')
        N_Usuario =  input()
        self.view.ask('Password: ')
        Password1 = input()
        self.view.ask('Repite password: ')
        Password2 = input()
        while(Password1 != Password2):
            self.view.msg('Las contraseñas no son iguales.')
            self.view.ask('Password: ')
            Password1 = input()
            self.view.ask('Repite password: ')
            Password2 = input()
        return [Nombre,Correo,T_Usuario,N_Usuario,Password1]

    def create_user(self):
        Nombre,Correo,T_Usuario,N_Usuario,Password1 = self.ask_user()
        out = self.model.create_user(Nombre,Correo,T_Usuario,N_Usuario,Password1)
        if(out == True):
            self.view.ok(Nombre, 'agrego')
        else:
            if out == 1062:
                self.view.error('Ya existe este usuario en los usuarios')
            else:
                self.view.error('NO SE PUDO AGREGAR ESTE USUARIO. REVISA OTRA VEZ')
        return

    def update_user(self):
        self.view.ask('INGRESE NOMBRE DE USUARIO A MODIFICAR: ')
        usuario = input()
        user = self.model.read_user_information_byuser(usuario)
        if(type(user) == tuple):
            self.view.ver_usuario_header('Datos del usuario: ' + usuario)
            self.view.ver_usuario(user)
            self.view.ver_usuario_midder()
            self.view.ver_usuario_footer()
        else:
            if user == None:
                self.view.error('EL USUARIO NO EXISTE!')
            else:
                self.view.error('PROBLEMA AL RECUPERAR LOS DATOS DEL USUARIO. REVISA')
            return
        i_user = user[0]
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual):')
        whole_vals = self.ask_user()
        fields, vals = self.update_lists(['nombre','correo','tipo_usuario','usuario','pass'], whole_vals)
        vals.append(i_user)
        vals = tuple(vals)
        out = self.model.update_user(fields,vals)
        if(out == True):
            self.view.ok(i_user,'actualizado')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR EL USUARIO. REVISA')

    def delete_user(self):
        self.view.ask('INGRESE NOMBRE DE USUARIO A ELIMINAR: ')
        usuario = input()
        record = self.model.read_user_information_byuser(usuario)
        if record == None:
            self.view.error('EL USUARIO NO EXISTE!')
            return
        i_user = record[0]
        count = self.model.remove_user(i_user)
        if count != 0:
            self.view.ok(record[1],'elimino')
        else:
            self.view.error("NO SE PUDO ELIMINAR EL USUSARIO. REVISA")

    def read_user_byid(self):
        self.view.ask('ID A BUSCAR: ')
        i_user = input()
        usuario = self.model.read_user(i_user)
        if( type(usuario) == tuple):
            self.view.ver_usuario_header('Datos del usuario ' + i_user + ' ' )
            self.view.ver_usuario(usuario)
            self.view.ver_usuario_midder()
            self.view.ver_usuario_footer()
        else:
            if usuario == None:
                self.view.error('El USUARIO NO EXISTE')
            else:
                self.view.error('ERROR AL RECUPERAR EL USUARIO. ¡Revisa!')
        return

    def read_user_byname(self):
        self.view.ask('Nombre: ')
        Nombre = input()
        usuarios = self.model.read_user_byname(Nombre)
        if(type(usuarios) == list):
            self.view.ver_usuario_header('LISTADO DE USUARIOS POR: ' + Nombre)
            for user in usuarios:
                self.view.ver_usuario(user)
            self.view.ver_usuario_midder()
            self.view.ver_usuario_footer()
        else:
            self.view.error('NO SE PUDO COMPLETAR LA ACCION LEER TODOS LOS USUARIOS.')
        return
    
    def read_user_byuser(self):
        self.view.ask('Usuario: ')
        user = input()
        usuario = self.model.read_user_information_byuser(user)
        if( type(usuario) == tuple):
            self.view.ver_usuario_header('Datos del usuario ' + user + ' ' )
            self.view.ver_usuario(usuario)
            self.view.ver_usuario_midder()
            self.view.ver_usuario_footer()
        else:
            if usuario == None:
                self.view.error('El USUARIO NO EXISTE')
            else:
                self.view.error('ERROR EL RECUPERAR EL USUARIO. ¡Revisa!')
        return
    

    def read_all_users(self):
        usuarios = self.model.read_all_users()
        if(type(usuarios) == list):
            self.view.ver_usuario_header('LISTADO DE USUARIOS')
            for peli in usuarios:
                self.view.ver_usuario(peli)
            self.view.ver_usuario_midder()
            self.view.ver_usuario_footer()
        else:
            self.view.error('NO SE PUDO COMPLETAR LA ACCION LEER TODOS LOS USUARIOS.')
        return
    
  
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------ADMINS---------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


    #*****************************#
    #      Controller Admins       #
    #*****************************#
    
    def admin_admin_menu(self):
        o = '0'
        while(o != '8'):
            self.view.admin_menu()
            self.view.option('8')
            o = input()
            if (o == '1'):
                self.create_admin()
            elif(o == '2'):
                self.update_admin()
            elif(o == '3'):
               self.delete_admin()
            elif(o == '4'):
               self.read_admin_byid()
            elif(o == '5'):
               self.read_admin_byname()
            elif(o == '6'):
               self.read_admin_byuser()
            elif(o == '7'):
               self.read_all_admins()
            elif(o == '8'):
                self.view.end()
            else:
                self.view.not_valid_option()
        return
    
    def ask_admin(self):
        self.view.ask('Nombre: ')
        Nombre = input()
        self.view.ask('Correo: ')
        Correo = input()
        self.view.ask('Direccion: ')
        Direccion =  input()
        self.view.ask('Telefono: ')
        Telefono =  input()
        self.view.ask('Nombre usuario: ')
        N_Usuario =  input()
        self.view.ask('Password: ')
        Password1 = input()
        self.view.ask('Repite password: ')
        Password2 = input()
        while(Password1 != Password2):
            self.view.msg('Las contraseñas no son iguales.')
            self.view.ask('Password: ')
            Password1 = input()
            self.view.ask('Repite password: ')
            Password2 = input()
        return [Nombre,Correo,Direccion,Telefono,N_Usuario,Password1]

    def create_admin(self):
        Nombre,Correo,Direccion,Telefono,N_Usuario,Password1 = self.ask_admin()
        out = self.model.create_admin(Nombre,Correo,Direccion,Telefono,N_Usuario,Password1)
        if(out == True):
            self.view.ok(Nombre, 'agrego')
        else:
            if out == 1062:
                self.view.error('Ya existe este usuario en los administradores')
            else:
                self.view.error('NO SE PUDO AGREGAR ESTE ADMINISTRADOR. REVISA OTRA VEZ')
        return

    def update_admin(self):
        self.view.ask('INGRESE NOMBRE DE USUARIO A MODIFICAR: ')
        usuario = input()
        admin = self.model.read_admin_information_byuser(usuario)
        if(type(admin) == tuple):
            self.view.ver_admin_header('Datos del Administrador: ' + usuario)
            self.view.ver_admin(admin)
            self.view.ver_admin_midder()
            self.view.ver_admin_footer()
        else:
            if admin == None:
                self.view.error('EL ADMINISTRADOR NO EXISTE!')
            else:
                self.view.error('PROBLEMA AL RECUPERAR LOS DATOS DEL ADMINISTRADOR. REVISA')
            return
        i_admin = admin[0]
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual):')
        whole_vals = self.ask_admin()
        fields, vals = self.update_lists(['nombre','correo','tipo_usuario','usuario','pass'], whole_vals)
        vals.append(i_admin)
        vals = tuple(vals)
        out = self.model.update_admin(fields,vals)
        if(out == True):
            self.view.ok(i_admin,'actualizado')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR EL USUARIO. REVISA')

    def delete_admin(self):
        self.view.ask('INGRESE NOMBRE DE USUARIO A ELIMINAR: ')
        usuario = input()
        record = self.model.read_admin_information_byuser(usuario)
        if record == None:
                self.view.error('EL ADMINISTRADOR NO EXISTE!')
                return
        i_admin = record[0]
        if(str(i_admin) == '1'):
            self.view.msg("Este administrador no se puede eliminar. Es el dueño.")
            return
        count = self.model.remove_admin(i_admin)
        if count != 0:
            self.view.ok(record[1],'elimino')
        else:
            self.view.error("NO SE PUDO ELIMINAR EL ADMINISTRADOR. REVISA")

    def read_admin_byid(self):
        self.view.ask('ID A BUSCAR: ')
        i_admin = input()
        admin = self.model.read_admin(i_admin)
        if( type(admin) == tuple):
            self.view.ver_admin_header('Datos del admin ' + i_admin + ' ' )
            self.view.ver_admin(admin)
            self.view.ver_admin_midder()
            self.view.ver_admin_footer()
        else:
            if admin == None:
                self.view.error('El ADMINISTRADOR NO EXISTE')
            else:
                self.view.error('ERROR AL RECUPERAR EL ADMINISTRADOR. ¡Revisa!')
        return

    def read_admin_byname(self):
        self.view.ask('Nombre: ')
        Nombre = input()
        admins = self.model.read_admin_byname(Nombre)
        if(type(admins) == list):
            self.view.ver_admin_header('LISTADO DE ADMINISTRADORES POR: ' + Nombre)
            for admin in admins:
                self.view.ver_admin(admin)
            self.view.ver_admin_midder()
            self.view.ver_admin_footer()
        else:
            self.view.error('NO SE PUDO COMPLETAR LA ACCION LEER TODOS LOS ADMINISTRADORES.')
        return
    
    def read_admin_byuser(self):
        self.view.ask('Usuario: ')
        user = input()
        admin = self.model.read_admin_information_byuser(user)
        if( type(admin) == tuple):
            self.view.ver_admin_header('Datos del admin ' + user + '         ' )
            self.view.ver_admin(admin)
            self.view.ver_admin_midder()
            self.view.ver_admin_footer()
        else:
            if admin == None:
                self.view.error('El ADMINISTRADOR NO EXISTE')
            else:
                self.view.error('ERROR EL RECUPERAR EL ADMINISTRADOR. ¡Revisa!')
        return
    

    def read_all_admins(self):
        admins = self.model.read_all_admin()
        if(type(admins) == list):
            self.view.ver_admin_header('LISTADO DE ADMINISTRADORES')
            for admin in admins:
                self.view.ver_admin(admin)
            self.view.ver_admin_midder()
            self.view.ver_admin_footer()
        else:
            self.view.error('NO SE PUDO COMPLETAR LA ACCION LEER TODOS LOS ADMINISTRADORES.')
        return
    
    
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------MOVIES----------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


    #*****************************#
    #      Controller Peliculas   #
    #*****************************#
    
    def admin_movies_menu(self):
        o = '0'
        while(o != '7'):
            self.view.movies_menu()
            self.view.option('7')
            o = input()
            if (o == '1'):
                self.create_movie()
            elif(o == '2'):
                self.update_movie()
            elif(o == '3'):
               self.delete_movie()
            elif(o == '4'):
               self.read_all_movies()
            elif(o == '5'):
               self.read_movie_byid()
            elif(o == '6'):
               self.read_movie_byname()
            elif(o == '7'):
                self.view.end()
            else:
                self.view.not_valid_option()
        return
    
    def ask_movie(self):
        self.view.ask('Nombre: ')
        Nombre = input()
        self.view.ask('Sipnosis: ')
        Sipnosis = input()
        self.view.ask('Lanzamiento: ')
        FLanzamiento =  input()
        return [Nombre,Sipnosis,FLanzamiento]

    def create_movie(self):
        Nombre,Sipnosis,FLanzamiento = self.ask_movie()
        out = self.model.create_pelicula(Nombre,Sipnosis,FLanzamiento)
        if(out == True):
            self.view.ok(Nombre, 'agrego')
        else:
            if out.errno == 1062:
                self.view.error('Ya existe este id en las peliculas')
            else:
                self.view.error('NO SE PUDO AGREGAR ESTA PELICULA. REVISA OTRA VEZ')
        return

    def update_movie(self):
        self.view.msg('Se recomienda saber la clave (ID) de la pelicula para modificarla.')
        self.view.msg('Ingrese OK para continuar o cualquier tecla para cancelar y volver al menú anterior.')
        resp = input()
        if(resp.upper() != 'OK'):
            return
        self.view.ask('ID MODIFICAR: ')
        i_pelicula = input()
        pelicula = self.model.read_pelicula(i_pelicula)
        if(type(pelicula) == tuple):
            self.view.ver_movie_header('Datos de la Pelicula ' + i_pelicula)
            self.view.ver_movie(pelicula)
            self.view.ver_movie_midder()
            self.view.ver_movie_footer()
        else:
            if pelicula == None:
                self.view.error('LA PELICULA NO EXISTE!')
            else:
                self.view.error('PROBLEMA AL RECUPERAR LOS DATOS DE LA PELICULA. REVISA')
            return

        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual):')
        whole_vals = self.ask_movie()
        fields, vals = self.update_lists(['nombre','sipnosis','FLanzamiento'], whole_vals)
        vals.append(i_pelicula)
        vals = tuple(vals)
        out = self.model.update_pelicula(fields,vals)
        if(out == True):
            self.view.ok(i_pelicula,'actualizado')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR LA PELICULA. REVISA')

    def delete_movie(self):
        self.view.msg('Se recomienda saber la clave (ID) de la pelicula para eliminarla.')
        self.view.msg('Ingrese OK para continuar o cualquier tecla para cancelar y volver al menú anterior.')
        resp = input()
        if(resp.upper() != 'OK'):
            return
        self.view.ask('ID a eliminar: ')
        i_pelicula = input()
        count = self.model.delete_pelicula(i_pelicula)
        if count != 0:
            self.view.ok(i_pelicula,'elimino')
        else:
            self.view.error("NO SE PUDO ELIMINAR LA PELICULA. REVISA")

    def read_movie_byid(self):
        self.view.ask('ID A BUSCAR: ')
        i_pelicula = input()
        pelicula = self.model.read_pelicula(i_pelicula)
        if( type(pelicula) == tuple):
            self.view.ver_movie_header('Datos de la pelicula ' + i_pelicula + ' ' )
            self.view.ver_movie(pelicula)
            self.view.ver_movie_midder()
            self.view.ver_movie_footer()
        else:
            if pelicula == None:
                self.view.error('LA PELICULA NO EXISTE')
            else:
                self.view.error('ERROR EL RECUPERAR LA PELICULA. ¡Revisa!')
        return

    def read_movie_byname(self):
        self.view.ask('Nombre: ')
        Nombre = input()
        peliculas = self.model.read_pelicula_nombre(Nombre)
        if(type(peliculas) == list):
            self.view.ver_movie_header('LISTADO DE PELICULAS')
            for peli in peliculas:
                self.view.ver_movie(peli)
            self.view.ver_movie_midder()
            self.view.ver_movie_footer()
        else:
            self.view.error('NO SE PUDO COMPLETAR LA ACCION LEER TODAS LAS PELICULAS.')
        return


    def read_all_movies(self):
        peliculas = self.model.read_all_pelicula()
        if(type(peliculas) == list):
            self.view.ver_movie_header('LISTADO DE PELICULAS')
            for peli in peliculas:
                self.view.ver_movie(peli)
            self.view.ver_movie_midder()
            self.view.ver_movie_footer()
        else:
            self.view.error('NO SE PUDO COMPLETAR LA ACCION LEER TODAS LAS PELICULAS.')
        return
    
    
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------GENEROS----------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


    #******************************
    #*  Controller  Generos       *
    #******************************

    def admin_generos_menu(self):
        o = '0'
        while(o != '6'):
            self.view.generos_menu()
            self.view.option('6')
            o = input()
            if (o == '1'):
                self.create_genero()
            elif(o == '2'):
                self.update_genero()
            elif(o == '3'):
                self.remove_genero()
            elif(o == '4'):
                self.read_genero_id()
            elif(o == '5'):
                self.read_all_generos()
            elif(o == '6'):
                self.view.end()
            else:
                self.view.not_valid_option()
        return
    
    def ask_genero(self):
        self.view.ask('ID Genero: ')#Creado porque la tabla generos no es auto-increment
        i_Genero = input()
        self.view.ask('Genero: ')
        Genero = input()
        return [i_Genero,Genero]

    def ask_genero_update(self): 
        self.view.ask('Genero: ')
        Genero = input()
        return [Genero]

    def create_genero(self):
        i_Genero,Genero = self.ask_genero()
        out = self.model.create_newgenero(i_Genero,Genero)
        if(out == True):
            self.view.ok(Genero, 'agrego')
        else:
            if out == 1062:
                self.view.error('Ya existe este genero registrado')
            elif out.errno == 1062:
                self.view.error('Ya existe ID registrado')
            else:
                self.view.error('NO SE PUDO AGREGAR ESTE GENERO. REVISA OTRA VEZ')
        return


    def update_genero(self):
        self.view.msg('Se recomienda saber la clave (ID) de genero para modificarlo.')
        self.view.msg('Ingrese OK para continuar o cualquier tecla para cancelar y volver al menú anterior.')
        resp = input()
        if(resp.upper() != 'OK'):
            return
        self.view.ask('ID MODIFICAR: ')
        i_genero = input()
        genero = self.model.read_genero(i_genero)
        if(type(genero) == tuple):
            self.view.ver_genero_header('Datos del genero ' + i_genero)
            self.view.ver_genero(genero)
            self.view.ver_genero_midder()
            self.view.ver_genero_footer()
        else:
            if genero == None:
                self.view.error('EL GENERO NO EXISTE!')
            else:
                self.view.error('PROBLEMA AL RECUPERAR LOS DATOS DEL GENERO. REVISA')
            return

        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual):')
        whole_vals = self.ask_genero_update()
        fields, vals = self.update_lists(['genero'], whole_vals)
        vals.append(i_genero)
        vals = tuple(vals)
        out = self.model.update_genero(fields,vals)
        if(out == True):
            self.view.ok(i_genero,'actualizado')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR EL GENERO. REVISA')

    def remove_genero(self):
        self.view.msg('Se recomienda saber la clave (ID) del genero para eliminarlo.')
        self.view.msg('Ingrese OK para continuar o cualquier tecla para cancelar y volver al menú anterior.')
        resp = input()
        if(resp.upper() != 'OK'):
            return
        self.view.ask('ID a eliminar: ')
        i_genero = input()
        count = self.model.delete_genero(i_genero)
        if count != 0:
            self.view.ok(i_genero,'elimino')
        else:
            self.view.error("NO SE PUDO ELIMINAR EL GENERO. REVISA")

    def read_all_generos(self):
        generos = self.model.read_all_generos()
        if(type(generos) == list):
            self.view.ver_genero_header('LISTADO DE GENEROS')
            for genero in generos:
                self.view.ver_genero(genero)
            self.view.ver_genero_midder()
            self.view.ver_genero_footer()
        else:
            self.view.error('NO SE PUDO COMPLETAR LA ACCION LEER TODOS LOS GENEROS.')
        return
    
    def read_genero_id(self):
        self.view.ask('ID A BUSCAR: ')
        i_genero = input()
        genero = self.model.read_genero(i_genero)
        if( type(genero) == tuple):
            self.view.ver_genero_header('Datos del genero ' + i_genero + ' ' )
            self.view.ver_genero(genero)
            self.view.ver_genero_midder()
            self.view.ver_genero_footer()
        else:
            if genero == None:
                self.view.error('EL GENERO NO EXISTE')
            else:
                self.view.error('ERROR AL RECUPERAR EL GENERO. ¡Revisa!')
        return

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------HORARIOS----------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


    #******************************
    #*  Controller  Horarios       *
    #******************************

    def admin_horarios_menu(self):
        o = '0'
        while(o != '6'):
            self.view.horarios_menu()
            self.view.option('6')
            o = input()
            if (o == '1'):
                self.create_horario()
            elif(o == '2'):
                self.update_horario()
            elif(o == '3'):
                self.remove_horario()
            elif(o == '4'):
                self.read_horario_id()
            elif(o == '5'):
                self.read_all_horarios()
            elif(o == '6'):
                self.view.end()
            else:
                self.view.not_valid_option()
        return
    
    def ask_horario(self):
        self.view.ask('Fecha [AAAA-MM-DD]: ')
        Dia = input()
        self.view.ask('Hora [00:00 FORMATO 24 HRS]: ')
        Hora = input()
        return [Dia,Hora]

    def create_horario(self):
        dia,hora = self.ask_horario()
        out = self.model.create_newhorario(dia,hora)
        if(out == True):
            self.view.ok_double_id(dia,hora, 'agrego')
        else:
            if out == 1062:
                self.view.error('Ya existe este horario registrado')
            elif(out.errno == 1062):
                self.view.error('Ya existe un id asociado')
            else:
                self.view.error('NO SE PUDO AGREGAR ESTE HORARIO. REVISA OTRA VEZ')
        return


    def update_horario(self):
        self.view.msg('Se recomienda saber la clave (ID) del horario para modificarlo.')
        self.view.msg('Ingrese OK para continuar o cualquier tecla para cancelar y volver al menú anterior.')
        resp = input()
        if(resp.upper() != 'OK'):
            return
        self.view.ask('ID MODIFICAR: ')
        i_horario = input()
        horario = self.model.read_horario(i_horario)
        if(type(horario) == tuple):
            self.view.ver_horario_header('Datos del horario ' + i_horario)
            self.view.ver_horario(horario)
            self.view.ver_horario_midder()
            self.view.ver_horario_footer()
        else:
            if horario == None:
                self.view.error('EL HORARIO NO EXISTE!')
            else:
                self.view.error('PROBLEMA AL RECUPERAR LOS DATOS DEL HORARIO. REVISA')
            return

        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual):')
        whole_vals = self.ask_horario()
        fields, vals = self.update_lists(['dia','hora'], whole_vals)
        vals.append(i_horario)
        vals = tuple(vals)
        out = self.model.update_horario(fields,vals)
        if(out == True):
            self.view.ok(i_horario,'actualizado')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR EL HORARIO. REVISA')

    def remove_horario(self):
        self.view.msg('Se recomienda saber la clave (ID) del horario para eliminarlo.')
        self.view.msg('Ingrese OK para continuar o cualquier tecla para cancelar y volver al menú anterior.')
        resp = input()
        if(resp.upper() != 'OK'):
            return
        self.view.ask('ID a eliminar: ')
        i_horario = input()
        count = self.model.delete_horario(i_horario)
        if count != 0:
            self.view.ok(i_horario,'elimino')
        else:
            self.view.error("NO SE PUDO ELIMINAR EL HORARIO. REVISA")

    def read_all_horarios(self):
        horarios = self.model.read_all_horarios()
        if(type(horarios) == list):
            self.view.ver_horario_header('LISTADO DE HORARIOS')
            for horario in horarios:
                self.view.ver_horario(horario)
            self.view.ver_horario_midder()
            self.view.ver_horario_footer()
        else:
            self.view.error('NO SE PUDO COMPLETAR LA ACCION LEER TODOS LOS HORARIOS.')
        return
    
    def read_horario_id(self):
        self.view.ask('ID A BUSCAR: ')
        i_horario = input()
        horario = self.model.read_horario(i_horario)
        if( type(horario) == tuple):
            self.view.ver_horario_header('Datos del horario ' + i_horario + ' ' )
            self.view.ver_horario(horario)
            self.view.ver_horario_midder()
            self.view.ver_horario_footer()
        else:
            if horario == None:
                self.view.error('EL HORARIO NO EXISTE')
            else:
                self.view.error('ERROR AL RECUPERAR EL HORARIO. ¡Revisa!')
        return


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------SALAS-------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


    #*****************************#
    #      Controller Salas       #
    #*****************************#
    
    def admin_salas_menu(self):
        o = '0'
        while(o != '7'):
            self.view.salas_menu()
            self.view.option('7')
            o = input()
            if (o == '1'):
                self.create_sala()
            elif(o == '2'):
                self.update_sala()
            elif(o == '3'):
                self.delete_sala()
            elif(o == '4'):
                self.read_sala_byid()
            elif(o == '5'):
                self.read_sala_bynumero()
            elif(o == '6'):
                self.read_all_salas()
            elif(o == '7'):
                self.view.end()
            else:
                self.view.not_valid_option()
        return
    
    def ask_sala(self):
        self.view.ask('Numero Sala: ')
        Nombre = input()
        self.view.ask('Tipo de Sala: ')
        T_sala = input()
        self.view.ask('Numero de asientos: ')
        N_sala =  input()
        return [Nombre,T_sala,N_sala]

    def create_sala(self):
        Nombre,T_sala,N_sala = self.ask_sala()
        out = self.model.create_newsala(Nombre,T_sala,N_sala)
        if(out == True):
            self.view.ok(Nombre, 'agrego')
        else:
            if(out == 1062):
                self.view.error('Ya existe esta sala')
            elif out.errno == 1062:
                self.view.error('Ya existe este id en las salas')
            else:
                self.view.error('NO SE PUDO AGREGAR ESTA PELICULA. REVISA OTRA VEZ')
        return

    def update_sala(self):
        self.view.msg('Se recomienda saber la clave (ID) de la sala para modificarla.')
        self.view.msg('Ingrese OK para continuar o cualquier tecla para cancelar y volver al menú anterior.')
        resp = input()
        if(resp.upper() != 'OK'):
            return
        self.view.ask('ID MODIFICAR: ')
        i_sala = input()
        sala = self.model.read_sala(i_sala)
        if(type(sala) == tuple):
            self.view.ver_sala_header('Datos de la Sala ' + i_sala)
            self.view.ver_sala(sala)
            self.view.ver_sala_midder()
            self.view.ver_sala_footer()
        else:
            if sala == None:
                self.view.error('LA SALA NO EXISTE!')
            else:
                self.view.error('PROBLEMA AL RECUPERAR LOS DATOS DE LA SALA. REVISA')
            return

        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual):')
        whole_vals = self.ask_sala()
        fields, vals = self.update_lists(['numero_sala','tipo_sala','numero_asientos'], whole_vals)
        vals.append(i_sala)
        vals = tuple(vals)
        out = self.model.update_sala(fields,vals)
        if(out == True):
            self.view.ok(i_sala,'actualizado')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR LA SALA. REVISA')

    def delete_sala(self):
        self.view.msg('Se recomienda saber la clave (ID) de la pelicula para eliminarla.')
        self.view.msg('Ingrese OK para continuar o cualquier tecla para cancelar y volver al menú anterior.')
        resp = input()
        if(resp.upper() != 'OK'):
            return
        self.view.ask('ID a eliminar: ')
        i_sala = input()
        count = self.model.delete_sala(i_sala)
        if count != 0:
            self.view.ok(i_sala,'elimino')
        else:
            self.view.error("NO SE PUDO ELIMINAR LA PELICULA. REVISA")

    def read_sala_byid(self):
        self.view.ask('ID A BUSCAR: ')
        i_sala = input()
        sala = self.model.read_sala(i_sala)
        if( type(sala) == tuple):
            self.view.ver_sala_header('Datos de la sala ' + i_sala + ' ' )
            self.view.ver_sala(sala)
            self.view.ver_sala_midder()
            self.view.ver_sala_footer()
        else:
            if sala == None:
                self.view.error('LA SALA NO EXISTE')
            else:
                self.view.error('ERROR EL RECUPERAR LA SALA. ¡Revisa!')
        return

    def read_sala_bynumero(self):
        self.view.ask('Numero: ')
        Numero = input()
        sala = self.model.read_sala_numerosala(Numero)
        if( type(sala) == tuple):
            self.view.ver_sala_header('Datos de la sala ' + Numero + ' ' )
            self.view.ver_sala(sala)
            self.view.ver_sala_midder()
            self.view.ver_sala_footer()
        else:
            if sala == None:
                self.view.error('LA SALA NO EXISTE')
            else:
                self.view.error('ERROR EL RECUPERAR LA SALA. ¡Revisa!')
        return


    def read_all_salas(self):
        salas = self.model.read_all_sala()
        if(type(salas) == list):
            self.view.ver_sala_header('LISTADO DE SALAS')
            for sala in salas:
                self.view.ver_sala(sala)
            self.view.ver_sala_midder()
            self.view.ver_sala_footer()
        else:
            self.view.error('NO SE PUDO COMPLETAR LA ACCION LEER TODAS LAS SALAS.')
        return


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------ASIENTOS-----------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    

    #******************************
    #*  Controller  Asientos      *
    #******************************

    def admin_asientos_menu(self):
        o = '0'
        while(o != '6'):
            self.view.asientos_menu()
            self.view.option('6')
            o = input()
            if (o == '1'):
                self.create_asiento()
            elif(o == '2'):
                self.update_asiento()
            elif(o == '3'):
                self.remove_asiento()
            elif(o == '4'):
                self.read_asiento_id()
            elif(o == '5'):
                self.read_all_asientos()
            elif(o == '6'):
                self.view.end()
            else:
                self.view.not_valid_option()
        return
    
    def ask_asiento(self):
        self.view.ask('Fila Asiento: ')
        Fila = input()
        self.view.ask('Numero Asiento: ')
        Asiento = input()
        return [Fila,Asiento]

    def create_asiento(self):
        fila,asiento = self.ask_asiento()
        out = self.model.create_newasiento(fila,asiento)
        if(out == True):
            self.view.ok_double_id(fila,asiento, 'agrego')
        else:
            if out == 1062:
                self.view.error('Ya existe este asiento registrado')
            elif(out.errno == 1062):
                self.view.error('Ya existe un id asociado')
            else:
                self.view.error('NO SE PUDO AGREGAR ESTE ASIENTO. REVISA OTRA VEZ')
        return


    def update_asiento(self):
        self.view.msg('Se recomienda saber la clave (ID) del asiento para modificarlo.')
        self.view.msg('Ingrese OK para continuar o cualquier tecla para cancelar y volver al menú anterior.')
        resp = input()
        if(resp.upper() != 'OK'):
            return
        self.view.ask('ID MODIFICAR: ')
        i_asiento = input()
        asiento = self.model.read_asiento(i_asiento)
        if(type(asiento) == tuple):
            self.view.ver_asiento_header('Datos del asiento ' + i_asiento)
            self.view.ver_asiento(asiento)
            self.view.ver_asiento_midder()
            self.view.ver_asiento_footer()
        else:
            if asiento == None:
                self.view.error('EL ASIENTO NO EXISTE!')
            else:
                self.view.error('PROBLEMA AL RECUPERAR LOS DATOS DEL ASIENTO. REVISA')
            return

        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual):')
        whole_vals = self.ask_asiento()
        fields, vals = self.update_lists(['fila','numero'], whole_vals)
        vals.append(i_asiento)
        vals = tuple(vals)
        out = self.model.update_asiento(fields,vals)
        if(out == True):
            self.view.ok(i_asiento,'actualizado')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR EL ASIENTO. REVISA')

    def remove_asiento(self):
        self.view.msg('Se recomienda saber la clave (ID) del asiento para eliminarlo.')
        self.view.msg('Ingrese OK para continuar o cualquier tecla para cancelar y volver al menú anterior.')
        resp = input()
        if(resp.upper() != 'OK'):
            return
        self.view.ask('ID a eliminar: ')
        i_asiento = input()
        count = self.model.delete_asiento(i_asiento)
        if count != 0:
            self.view.ok(i_asiento,'elimino')
        else:
            self.view.error("NO SE PUDO ELIMINAR EL ASIENTO. REVISA")

    def read_all_asientos(self):
        asientos = self.model.read_all_asientos()
        if(type(asientos) == list):
            self.view.ver_asiento_header('LISTADO DE ASIENTOS')
            for asiento in asientos:
                self.view.ver_asiento(asiento)
            self.view.ver_asiento_midder()
            self.view.ver_asiento_footer()
        else:
            self.view.error('NO SE PUDO COMPLETAR LA ACCION LEER TODOS LOS HORARIOS.')
        return
    
    def read_asiento_id(self):
        self.view.ask('ID A BUSCAR: ')
        i_asiento = input()
        asiento = self.model.read_asiento(i_asiento)
        if( type(asiento) == tuple):
            self.view.ver_asiento_header('Datos del asiento ' + i_asiento + ' ' )
            self.view.ver_asiento(asiento)
            self.view.ver_asiento_midder()
            self.view.ver_asiento_footer()
        else:
            if asiento == None:
                self.view.error('EL ASIENTO NO EXISTE')
            else:
                self.view.error('ERROR AL RECUPERAR EL ASIENTO. ¡Revisa!')
        return


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------Peliculas-Horarios---------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    

    #*************************************
    #*  Controller  Peliculas-Horarios   *
    #*************************************

    def admin_peliculas_horarios_menu(self):
        o = '0'
        while(o != '6'):
            self.view.pelihorario_menu()
            self.view.option('6')
            o = input()
            if (o == '1'):
                self.create_pelihorario()
            elif(o == '2'):
                self.update_pelihorario()
            elif(o == '3'):
                self.remove_pelihorario()
            elif(o == '4'):
                self.read_pelihorario_id()
            elif(o == '5'):
                self.read_all_pelihorarios()
            elif(o == '6'):
                self.view.end()
            else:
                self.view.not_valid_option()
        return
    
    def ask_pelihorario(self):
        self.view.ask('ID Pelicula: ')
        Pelicula = input()
        self.view.ask('ID Horario: ')
        Horario = input()
        self.view.ask('Precio: ')
        Precio = input()
        return [Pelicula,Horario,Precio]

    def create_pelihorario(self):
        i_pelicula,i_horario,precio = self.ask_pelihorario()
        out = self.model.create_new_pelicula_horario(i_pelicula,i_horario,precio)
        if(out == True):
            self.view.ok_double_id(i_pelicula,i_horario, 'agrego')
        else:
            if out == 1062:
                self.view.error('Ya existe esta pelicula y horario registrados')
            elif(out.errno == 1062):
                self.view.error('Ya existe un id asociado')
            else:
                self.view.error('NO SE PUDO AGREGAR. REVISA OTRA VEZ')
        return


    def update_pelihorario(self):
        self.view.msg('Se recomienda saber las claves (ID) para modificar.')
        self.view.msg('Ingrese OK para continuar o cualquier tecla para cancelar y volver al menú anterior.')
        resp = input()
        if(resp.upper() != 'OK'):
            return
        self.view.ask('ID PELICULA: ')
        i_pelicula = input()
        self.view.ask('ID HORARIO: ')
        i_horario = input()
        pelihorario = self.model.read_pelicula_horario(i_pelicula,i_horario)
        if(type(pelihorario) == tuple):
            self.view.ver_pelihorario_header('Datos pelicula ' + i_pelicula + ' y horario ' + i_horario)
            self.view.ver_pelihorario(pelihorario)
            self.view.ver_pelihorario_midder()
            self.view.ver_pelihorario_footer()
        else:
            if pelihorario == None:
                self.view.error('EL REGISTRO NO EXISTE!')
            else:
                self.view.error('PROBLEMA AL RECUPERAR LOS DATOS. REVISA')
            return

        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual):')
        whole_vals = self.ask_pelihorario()
        fields, vals = self.update_lists(['id_pelicula','id_horario','precio'], whole_vals)
        vals.append(i_pelicula)
        vals.append(i_horario)
        vals = tuple(vals)
        out = self.model.update_peliculas_horarios(fields,vals)
        if(out == True):
            self.view.ok_double_id(i_pelicula,i_horario,'actualizado')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR. REVISA')
    
    def remove_pelihorario(self):
        self.view.msg('Se recomienda saber las claves (ID)  para eliminarlo.')
        self.view.msg('Ingrese OK para continuar o cualquier tecla para cancelar y volver al menú anterior.')
        resp = input()
        if(resp.upper() != 'OK'):
            return
        self.view.ask('ID PELICULA: ')
        i_pelicula = input()
        self.view.ask('ID HORARIO: ')
        i_horario = input()
        count = self.model.delete_peliculas_horarios(i_pelicula,i_horario)
        if count != 0:
            self.view.ok_double_id(i_pelicula,i_horario,'elimino')
        else:
            self.view.error("NO SE PUDO ELIMINAR. REVISA")


    def read_all_pelihorarios(self):
        pelihorarios = self.model.read_all_pelicula_horarios()
        if(type(pelihorarios) == list):
            self.view.ver_pelihorario_header('LISTADO DE PELICULAS - HORARIOS')
            for ph in pelihorarios:
                self.view.ver_pelihorario(ph)
            self.view.ver_pelihorario_midder()
            self.view.ver_pelihorario_footer()
        else:
            self.view.error('NO SE PUDO COMPLETAR LA ACCION LEER TODOS LAS PELICULAS - HORARIOS.')
        return

    def read_pelihorario_id(self):
        self.view.ask('ID PELICULA: ')
        i_pelicula = input()
        self.view.ask('ID HORARIO: ')
        i_horario = input()
        pelihorario = self.model.read_pelicula_horario(i_pelicula,i_horario)
        if( type(pelihorario) == tuple):
            self.view.ver_pelihorario_header('Datos de la pelicula ' + i_pelicula + ' y horario ' +i_horario )
            self.view.ver_pelihorario(pelihorario)
            self.view.ver_pelihorario_midder()
            self.view.ver_pelihorario_footer()
        else:
            if pelihorario == None:
                self.view.error('NO EXISTE REGISTRO')
            else:
                self.view.error('ERROR AL RECUPERAR LOS DATOS. ¡Revisa!')
        return


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------Peliculas-Generos------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    

    #*************************************
    #*  Controller  Peliculas-Generos    *
    #*************************************

    def admin_peliculas_generos_menu(self):
        o = '0'
        while(o != '6'):
            self.view.peligenero_menu()
            self.view.option('6')
            o = input()
            if (o == '1'):
                self.create_peligenero()
            elif(o == '2'):
                self.update_peligenero()
            elif(o == '3'):
                self.remove_peligenero()
            elif(o == '4'):
                self.read_peligenero_id()
            elif(o == '5'):
                self.read_all_peligeneros()
            elif(o == '6'):
                self.view.end()
            else:
                self.view.not_valid_option()
        return
    
    def ask_peligenero(self):
        self.view.ask('ID Pelicula: ')
        Pelicula = input()
        self.view.ask('ID Genero: ')
        Genero = input()
        return [Pelicula,Genero]

    def create_peligenero(self):
        i_pelicula,i_genero = self.ask_peligenero()
        out = self.model.create_new_pelicula_genero(i_pelicula,i_genero)
        if(out == True):
            self.view.ok_double_id(i_pelicula,i_genero, 'agrego')
        else:
            if out == 1062:
                self.view.error('Ya existe esta pelicula y genero registrados')
            elif(out.errno == 1062):
                self.view.error('Ya existe un id asociado')
            else:
                self.view.error('NO SE PUDO AGREGAR. REVISA OTRA VEZ')
        return


    def update_peligenero(self):
        self.view.msg('Se recomienda saber las claves (ID) para modificar.')
        self.view.msg('Ingrese OK para continuar o cualquier tecla para cancelar y volver al menú anterior.')
        resp = input()
        if(resp.upper() != 'OK'):
            return
        self.view.ask('ID PELICULA: ')
        i_pelicula = input()
        self.view.ask('ID GENERO: ')
        i_genero = input()
        peligenero = self.model.read_pelicula_genero(i_pelicula,i_genero)
        if(type(peligenero) == tuple):
            self.view.ver_peligenero_header('Datos pelicula ' + i_pelicula + ' y genero ' + i_genero)
            self.view.ver_peligenero(peligenero)
            self.view.ver_peligenero_midder()
            self.view.ver_peligenero_footer()
        else:
            if peligenero == None:
                self.view.error('EL REGISTRO NO EXISTE!')
            else:
                self.view.error('PROBLEMA AL RECUPERAR LOS DATOS. REVISA')
            return

        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual):')
        whole_vals = self.ask_peligenero()
        fields, vals = self.update_lists(['id_pelicula','id_genero'], whole_vals)
        vals.append(i_pelicula)
        vals.append(i_genero)
        vals = tuple(vals)
        out = self.model.update_peliculas_generos(fields,vals)
        if(out == True):
            self.view.ok_double_id(i_pelicula,i_genero,'actualizado')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR. REVISA')
    
    def remove_peligenero(self):
        self.view.msg('Se recomienda saber las claves (ID)  para eliminarlo.')
        self.view.msg('Ingrese OK para continuar o cualquier tecla para cancelar y volver al menú anterior.')
        resp = input()
        if(resp.upper() != 'OK'):
            return
        self.view.ask('ID PELICULA: ')
        i_pelicula = input()
        self.view.ask('ID GENERO: ')
        i_genero = input()
        count = self.model.delete_peliculas_genero(i_pelicula,i_genero)
        if count != 0:
            self.view.ok_double_id(i_pelicula,i_genero,'elimino')
        else:
            self.view.error("NO SE PUDO ELIMINAR. REVISA")


    def read_all_peligeneros(self):
        peligeneros = self.model.read_all_peliculas_generos()
        if(type(peligeneros) == list):
            self.view.ver_peligenero_header('LISTADO DE PELICULAS - GENEROS')
            for pg in peligeneros:
                self.view.ver_peligenero(pg)
            self.view.ver_peligenero_midder()
            self.view.ver_peligenero_footer()
        else:
            self.view.error('NO SE PUDO COMPLETAR LA ACCION LEER TODOS LAS PELICULAS - GENEROS.')
        return

    def read_peligenero_id(self):
        self.view.ask('ID PELICULA: ')
        i_pelicula = input()
        self.view.ask('ID GENERO: ')
        i_genero = input()
        peligenero = self.model.read_pelicula_genero(i_pelicula,i_genero)
        if( type(peligenero) == tuple):
            self.view.ver_peligenero_header('Datos de la pelicula ' + i_pelicula + ' y genero ' +i_genero )
            self.view.ver_peligenero(peligenero)
            self.view.ver_peligenero_midder()
            self.view.ver_peligenero_footer()
        else:
            if peligenero == None:
                self.view.error('NO EXISTE REGISTRO')
            else:
                self.view.error('ERROR AL RECUPERAR LOS DATOS. ¡Revisa!')
        return


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------Peliculas-Salas------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


    #*************************************
    #*  Controller  Peliculas-Salas    *
    #*************************************

    def admin_peliculas_salas_menu(self):
        o = '0'
        while(o != '6'):
            self.view.pelisala_menu()
            self.view.option('6')
            o = input()
            if (o == '1'):
                self.create_pelisala()
            elif(o == '2'):
                self.update_pelisala()
            elif(o == '3'):
                self.remove_pelisala()
            elif(o == '4'):
                self.read_pelisala_id()
            elif(o == '5'):
                self.read_all_pelisalas()
            elif(o == '6'):
                self.view.end()
            else:
                self.view.not_valid_option()
        return
    
    def ask_pelisala(self):
        self.view.ask('ID Pelicula: ')
        Pelicula = input()
        self.view.ask('ID Sala: ')
        Sala = input()
        return [Pelicula,Sala]

    def create_pelisala(self):
        i_pelicula,i_sala = self.ask_pelisala()
        out = self.model.create_new_pelicula_sala(i_pelicula,i_sala)
        if(out == True):
            self.view.ok_double_id(i_pelicula,i_sala, 'agrego')
        else:
            if out == 1062:
                self.view.error('Ya existe esta pelicula y sala registrados')
            elif(out.errno == 1062):
                self.view.error('Ya existe un id asociado')
            else:
                self.view.error('NO SE PUDO AGREGAR. REVISA OTRA VEZ')
        return


    def update_pelisala(self):
        self.view.msg('Se recomienda saber las claves (ID) para modificar.')
        self.view.msg('Ingrese OK para continuar o cualquier tecla para cancelar y volver al menú anterior.')
        resp = input()
        if(resp.upper() != 'OK'):
            return
        self.view.ask('ID PELICULA: ')
        i_pelicula = input()
        self.view.ask('ID SALA: ')
        i_sala = input()
        pelisala = self.model.read_pelicula_sala(i_pelicula,i_sala)
        if(type(pelisala) == tuple):
            self.view.ver_pelisala_header('Datos pelicula ' + i_pelicula + ' y sala ' + i_sala)
            self.view.ver_pelisala(pelisala)
            self.view.ver_pelisala_midder()
            self.view.ver_pelisala_footer()
        else:
            if pelisala == None:
                self.view.error('EL REGISTRO NO EXISTE!')
            else:
                self.view.error('PROBLEMA AL RECUPERAR LOS DATOS. REVISA')
            return

        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual):')
        whole_vals = self.ask_pelisala()
        fields, vals = self.update_lists(['id_pelicula','id_sala'], whole_vals)
        vals.append(i_pelicula)
        vals.append(i_sala)
        vals = tuple(vals)
        out = self.model.update_peliculas_salas(fields,vals)
        if(out == True):
            self.view.ok_double_id(i_pelicula,i_sala,'actualizado')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR. REVISA')
    
    def remove_pelisala(self):
        self.view.msg('Se recomienda saber las claves (ID)  para eliminarlo.')
        self.view.msg('Ingrese OK para continuar o cualquier tecla para cancelar y volver al menú anterior.')
        resp = input()
        if(resp.upper() != 'OK'):
            return
        self.view.ask('ID PELICULA: ')
        i_pelicula = input()
        self.view.ask('ID SALA: ')
        i_sala = input()
        count = self.model.delete_peliculas_sala(i_pelicula,i_sala)
        if count != 0:
            self.view.ok_double_id(i_pelicula,i_sala,'elimino')
        else:
            self.view.error("NO SE PUDO ELIMINAR. REVISA")


    def read_all_pelisalas(self):
        pelisalas = self.model.read_all_peliculas_salas()
        if(type(pelisalas) == list):
            self.view.ver_pelisala_header('LISTADO DE PELICULAS - SALAS')
            for ps in pelisalas:
                self.view.ver_pelisala(ps)
            self.view.ver_pelisala_midder()
            self.view.ver_pelisala_footer()
        else:
            self.view.error('NO SE PUDO COMPLETAR LA ACCION LEER TODOS LAS PELICULAS - GENEROS.')
        return

    def read_pelisala_id(self):
        self.view.ask('ID PELICULA: ')
        i_pelicula = input()
        self.view.ask('ID SALA: ')
        i_sala = input()
        pelisala = self.model.read_pelicula_sala(i_pelicula,i_sala)
        if( type(pelisala) == tuple):
            self.view.ver_pelisala_header('Datos de la pelicula ' + i_pelicula + ' y sala ' +i_sala )
            self.view.ver_pelisala(pelisala)
            self.view.ver_pelisala_midder()
            self.view.ver_pelisala_footer()
        else:
            if pelisala == None:
                self.view.error('NO EXISTE REGISTRO')
            else:
                self.view.error('ERROR AL RECUPERAR LOS DATOS. ¡Revisa!')
        return



#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------Salas-Asientos---------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    

    #*************************************
    #*  Controller  Salas-Asientos       *
    #*************************************

    def admin_salas_asientos_menu(self):
        o = '0'
        while(o != '8'):
            self.view.sala_asiento_menu()
            self.view.option('8')
            o = input()
            if (o == '1'):
                self.create_sala_asiento()
            elif(o == '2'):
                self.update_sala_asiento()
            elif(o == '3'):
                self.update_estatado_asiento()
            elif(o == '4'):
                self.remove_sala_asiento()
            elif(o == '5'):
                self.read_sala_asiento_id()
            elif(o == '6'):
                self.read_all_salas_bynumeroasientos()
            elif(o == '7'):
                self.read_all_asientos_bynumero_sala()
            elif(o == '8'):
                self.view.end()
            else:
                self.view.not_valid_option()
        return
    
    def ask_sala_asiento(self):
        self.view.ask('ID Sala: ')
        i_sala = input()
        self.view.ask('ID Asiento: ')
        i_asiento = input()
        self.view.ask('Estado Asiento: ')
        E_asiento = input()
        self.view.ask('Disponibilidad Asiento: ')
        D_asiento = input()
        self.view.ask('Estado Sala: ')
        E_sala = input()
        return [i_sala,i_asiento,E_asiento,D_asiento,E_sala]

    def ask_update_estado_asiento(self):
        self.view.ask("Numero Sala: ")
        n_sala = input()
        self.view.ask("Fila: ")
        fila = input()
        self.view.ask("Asiento: ")
        asiento = input()
        r_sala = self.model.read_sala_numerosala(n_sala)
        i_sala = r_sala[0]
        i_asiento = self.model.read_asiento_by_fila_asiento(fila,asiento)
        return [i_sala,i_asiento]

    def create_sala_asiento(self):
        i_sala,i_asiento,E_asiento,D_asiento,E_sala = self.ask_sala_asiento()
        out = self.model.create_new_sala_asiento(i_sala,i_asiento,E_asiento,D_asiento,E_sala)
        if(out == True):
            self.view.ok_double_id(i_sala,i_asiento, 'agrego')
        else:
            if out == 1062:
                self.view.error('Ya existe esta sala y asiento registrados')
            elif(out.errno == 1062):
                self.view.error('Ya existe un id asociado')
            else:
                self.view.error('NO SE PUDO AGREGAR. REVISA OTRA VEZ')
        return


    def update_sala_asiento(self):
        self.view.msg('Se recomienda saber las claves (ID) para modificar.')
        self.view.msg('Ingrese OK para continuar o cualquier tecla para cancelar y volver al menú anterior.')
        resp = input()
        if(resp.upper() != 'OK'):
            return
        self.view.ask('ID SALA: ')
        i_sala = input()
        self.view.ask('ID ASIENTO: ')
        i_asiento = input()
        sala_asiento = self.model.read_sala_asiento(i_sala,i_asiento)
        if(type(sala_asiento) == tuple):
            self.view.ver_sala_asiento_header('Datos de la sala ' + i_sala + ' y asiento ' + i_asiento)
            self.view.ver_sala_asiento(sala_asiento)
            self.view.ver_sala_asiento_midder()
            self.view.ver_sala_asiento_footer()
        else:
            if sala_asiento == None:
                self.view.error('EL REGISTRO NO EXISTE!')
            else:
                self.view.error('PROBLEMA AL RECUPERAR LOS DATOS. REVISA')
            return

        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual):')
        whole_vals = self.ask_sala_asiento()
        fields, vals = self.update_lists(['id_sala','id_asiento','estado_asiento','disponibilidad_asiento','estado_sala'], whole_vals)
        vals.append(i_sala)
        vals.append(i_asiento)
        vals = tuple(vals)
        out = self.model.update_salas_asientos(fields,vals)
        if(out == True):
            self.view.ok_double_id(i_sala,i_asiento,'actualizado')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR. REVISA')
    

    def update_estatado_asiento(self):
        i_sala, i_asiento = self.ask_update_estado_asiento()
        if(i_sala == None or i_asiento == None):
            self.view.error("NO SE PUEDE ACTUALIZAR. REVISA")
            return
        verify = self.model.update_estado_asiento_disponible(i_sala,i_asiento)
        if(verify == True):
            self.view.ok_double_id(i_sala,i_asiento,'actualizo el estado del asiento a Disponible')
            return
        else:
            self.view.error("NO SE PUEDE ACTUALIZAR. REVISA")


    def remove_sala_asiento(self):
        self.view.msg('Se recomienda saber las claves (ID)  para eliminarlo.')
        self.view.msg('Ingrese OK para continuar o cualquier tecla para cancelar y volver al menú anterior.')
        resp = input()
        if(resp.upper() != 'OK'):
            return
        self.view.ask('ID SALA: ')
        i_sala = input()
        self.view.ask('ID ASIENTO: ')
        i_asiento = input()
        count = self.model.delete_asiento_sala(i_sala,i_asiento)
        if count != 0:
            self.view.ok_double_id(i_sala,i_asiento,'elimino')
        else:
            self.view.error("NO SE PUDO ELIMINAR. REVISA")

    def read_all_asientos_bynumero_sala(self):
        self.view.ask("Numero de Sala: ")
        n_sala = input()
        enc_sala = self.model.read_sala_numerosala_for_asientos(n_sala)
        if (enc_sala == None):
            self.view.error("LA SALA NO EXISTE")
            return   
        asientos = self.model.read_all_asientos_by_sala(n_sala)
        if(type(asientos) == list):
            self.view.ver_sala_asiento_header('LISTADO DE ASIENTOS DE LA SALA: ' + n_sala)
            self.view.ver_sala_asientos_byasiento_a_sala(enc_sala)
            for asiento in asientos:
                self.view.ver_sala_asiento_asientos_a_sala(asiento)
            self.view.ver_sala_asiento_midder()
            self.view.ver_sala_asiento_footer()
        else:
            self.view.error('NO SE PUDO COMPLETAR LA ACCION LEER TODOS LAS PELICULAS - GENEROS.')
        return


    def read_all_salas_bynumeroasientos(self):
        self.view.ask("Numero de asientos: ")
        n_asientos = input()
        salas = self.model.read_sala_by_numeroasientos(n_asientos)
        if(type(salas) == list):
            self.view.ver_sala_asiento_header('LISTADO DE SALAS CON: ' + n_asientos + ' ASIENTOS')
            for sala in salas:
                self.view.ver_sala_asiento_by_numero_asientos(sala)
            self.view.ver_sala_asiento_midder()
            self.view.ver_sala_asiento_footer()
        else:
            self.view.error('NO SE PUDO COMPLETAR LA ACCION LEER TODOS LAS PELICULAS - GENEROS.')
        return


    def read_sala_asiento_id(self):
        self.view.ask('ID SALA: ')
        i_sala = input()
        self.view.ask('ID ASIENTO: ')
        i_aisento = input()
        sala_asiento = self.model.read_sala_asiento(i_sala,i_aisento)
        if( type(sala_asiento) == tuple):
            self.view.ver_sala_asiento_header('Datos de la sala ' + i_sala + ' y asiento ' +i_aisento )
            self.view.ver_sala_asiento(sala_asiento)
            self.view.ver_sala_asiento_midder()
            self.view.ver_sala_asiento_footer()
        else:
            if sala_asiento == None:
                self.view.error('NO EXISTE REGISTRO')
            else:
                self.view.error('ERROR AL RECUPERAR LOS DATOS. ¡Revisa!')
        return


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------Tickets---------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    #*************************************
    #*       Controller  Tickets         *
    #*************************************

    def admin_boletos_menu(self):
        o = '0'
        while(o != '6'):
            self.view.tickets_menu()
            self.view.option('6')
            o = input()
            if (o == '1'):
                self.create_ticket()
            elif(o == '2'):
                self.update_ticket()
            elif(o == '3'):
                self.remove_ticket()
            elif(o == '4'):
                self.read_ticket_id()
            elif(o == '5'):
                self.read_all_tickets()
            elif(o == '6'):
                self.view.end()
            else:
                self.view.not_valid_option()
        return
    
    def ask_ticket(self):
        self.view.ask('ID Pelicula: ')
        i_pelicula = input()
        self.view.ask('ID Horario: ')
        i_horario = input()
        self.view.ask('ID Sala: ')
        i_sala = input()
        self.view.ask('ID Asiento: ')
        i_asiento = input()
        return [i_pelicula,i_horario,i_sala,i_asiento]

    def read_all_pelihorarios_ticket(self):
        pelihorarios = self.model.read_all_pelihorarios_ticket()
        if(type(pelihorarios) == list):
            self.view.ver_pelihorario_header('LISTADO DE PELICULAS - HORARIOS')
            for ph in pelihorarios:
                self.view.ver_pelihorario_ticket(ph)
            self.view.ver_pelihorario_midder()
            self.view.ver_pelihorario_footer()
        else:
            self.view.error('NO SE PUDO COMPLETAR LA ACCION LEER TODOS LAS PELICULAS - HORARIOS.')
        return

    def ask_ticket_update(self):
        self.view.ask("¿Ver Peliculas Horarios? Y/N : ")
        r_ph = input()
        if(r_ph.upper() == 'Y'):
            self.read_all_pelihorarios_ticket()
        self.view.ask('ID Pelicula - Horario: ')
        i_peli_horario = input()
        self.view.ask("¿Registrar por sala y asiento? Y/N : ")
        r_sa = input()
        if(r_sa.upper() == 'Y'):
            self.view.ask("ID Sala: ")
            i_sala = input()
            self.view.ask("ID Asiento: ")
            i_asiento = input()
            i_sala_asiento = self.model.read_sala_asiento_ticket(i_sala,i_asiento)
        else:
            self.view.ask('ID Sala - Asiento: ')
            i_sala_asiento = input()
        print(i_peli_horario,i_sala_asiento)
        return [i_peli_horario,i_sala_asiento]

    def create_ticket(self):
        i_pelicula,i_horario,i_sala,i_asiento = self.ask_ticket()
        i_peli_horario = self.model.read_pelicula_horario_ticket(i_pelicula,i_horario)
        i_sala_asiento = self.model.read_sala_asiento_ticket(i_sala,i_asiento)
        if(i_peli_horario == None or i_sala_asiento == None):
            print("ERROR EN ALGUNA DE LAS CLAVES. REVISA")
            return
        out = self.model.create_new_ticket(i_peli_horario,i_sala_asiento)
        if(out == True):
            self.view.ok_double_id(i_peli_horario,i_sala_asiento, 'agrego')
        else:
            if(out.errno == 1062):
                self.view.error('Ya existe un id asociado')
            else:
                self.view.error('NO SE PUDO AGREGAR. REVISA OTRA VEZ')
        return


    def update_ticket(self):
        self.view.msg('Se recomienda saber la clave (ID) para modificar un ticket.')
        self.view.msg('Ingrese OK para continuar o cualquier tecla para cancelar y volver al menú anterior.')
        resp = input()
        if(resp.upper() != 'OK'):
            return
        self.view.ask('ID TICKET: ')
        i_ticket = input()
        ticket = self.model.read_ticket(i_ticket)
        i_peli_horario = ticket[1]
        i_sala_asiento = ticket[2]
        r_ticket = self.model.read_ticket_information(i_peli_horario,i_sala_asiento)
        if(type(r_ticket) == tuple):
            self.view.ver_ticket_header('Datos del ticket ' + i_ticket)
            self.view.ver_ticket(r_ticket)
            self.view.ver_ticket_midder()
            self.view.ver_ticket_footer()
        else:
            if r_ticket == None:
                self.view.error('EL TICKET NO EXISTE!')
            else:
                self.view.error('PROBLEMA AL RECUPERAR LOS DATOS. REVISA')
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual):')
        whole_vals = self.ask_ticket_update()
        fields, vals = self.update_lists(['id_pelihorario','id_sala_asiento'], whole_vals)
        vals.append(i_peli_horario)
        vals.append(i_sala_asiento)
        vals = tuple(vals)
        out = self.model.update_ticket(fields,vals)
        if(out == True):
            self.view.ok(i_ticket,'actualizado')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR. REVISA')
    
    def remove_ticket(self):
        self.view.msg('Se recomienda saber la clave (ID)  para eliminarlo.')
        self.view.msg('Ingrese OK para continuar o cualquier tecla para cancelar y volver al menú anterior.')
        resp = input()
        if(resp.upper() != 'OK'):
            return
        self.view.ask('ID TICKET: ')
        i_ticket = input()
        r_ticket = self.model.read_ticket(i_ticket)
        if (r_ticket == None):
            self.view.error('EL TICKET NO EXISTE!')
            return
        i_ph = r_ticket[1]
        i_sa = r_ticket[2]
        count = self.model.delete_ticket(i_ph,i_sa)
        if count != 0:
            self.view.ok(i_ticket,'elimino')
        else:
            self.view.error("NO SE PUDO ELIMINAR. REVISA")


    def read_all_tickets(self):
        tickets = self.model.read_all_tickets()
        if(type(tickets) == list):
            self.view.ver_ticket_header('LISTADO DE TICKETS')
            for record in tickets:
                r_ticket = self.model.read_ticket_information(record[1],record[2])
                self.view.ver_ticket(r_ticket)
            self.view.ver_ticket_midder()
            self.view.ver_ticket_footer()
        else:
            self.view.error('NO SE PUDO COMPLETAR LA ACCION LEER TODOS LOS TICKETS')
        return

    def read_ticket_id(self):
        self.view.ask('ID TICKET: ')
        i_ticket = input()
        r_ticket = self.model.read_ticket(i_ticket)
        i_ph = r_ticket[1]
        i_sa = r_ticket[2]
        ticket = self.model.read_ticket_information(i_ph,i_sa)
        if( type(ticket) == tuple):
            self.view.ver_ticket_header('Datos del ticket ' + i_ticket)
            self.view.ver_ticket(ticket)
            self.view.ver_ticket_midder()
            self.view.ver_ticket_footer()
        else:
            if ticket == None:
                self.view.error('NO EXISTE REGISTRO')
            else:
                self.view.error('ERROR AL RECUPERAR LOS DATOS. ¡Revisa!')
        return

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------COMPRAS----------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    
    #*************************************
    #*       Controller  Compras         *
    #*************************************

    def admin_compras_menu(self):
        o = '0'
        while(o != '6'):
            self.view.compras_menu()
            self.view.option('6')
            o = input()
            if (o == '1'):
                self.update_compra()
            elif(o == '2'):
                self.delete_compra()
            elif(o == '3'):
                self.read_compra()
            elif(o == '4'):
                self.read_all_compras()
            elif(o == '5'):
                self.view.end()
            else:
                self.view.not_valid_option()
        return
    
    def ask_compra(self):
        self.view.ask('ID ticket: ')
        i_ticket = input()
        self.view.ask('ID usuario: ')
        i_user = input()
        return [i_ticket,i_user]

    def read_all_compras(self):
        compras = self.model.read_all_compras()
        if(type(compras) == list):
            self.view.ver_compra_header('LISTADO DE COMPRAS')
            for compra in compras:
                self.view.ver_usuario_header("Datos del Usuario")
                usuario = self.model.read_user(compra[2])
                self.view.ver_usuario(usuario)
                self.view.ver_compra_header('Datos de la compra')
                record = self.model.read_compra_information(compra[0])
                self.view.ver_compra(record)
            self.view.ver_compra_midder()
            self.view.ver_compra_footer()
        else:
            self.view.error('NO SE PUDO COMPLETAR LA ACCION LEER TODOS LAS COMPRAS.')
        return


    def update_compra(self):
        self.view.msg('Se recomienda saber la clave (ID) para modificar un ticket.')
        self.view.msg('Ingrese OK para continuar o cualquier tecla para cancelar y volver al menú anterior.')
        resp = input()
        if(resp.upper() != 'OK'):
            return
        self.view.ask('ID COMPRA: ')
        i_compra = input()
        compra = self.model.read_compra(i_compra)
        i_ticket = compra[1]
        i_user = compra[2]
        r_compra = self.model.read_compra_information(i_compra)
        if(type(r_compra) == tuple):
            self.view.ver_compra_header('Datos del compra ' + i_compra)
            self.view.ver_compra(r_compra)
            self.view.ver_compra_midder()
            self.view.ver_compra_footer()
        else:
            if r_compra == None:
                self.view.error('EL COMPRA NO EXISTE!')
            else:
                self.view.error('PROBLEMA AL RECUPERAR LOS DATOS. REVISA')
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual):')
        whole_vals = self.ask_compra()
        fields, vals = self.update_lists(['id_ticket','id_usuario'], whole_vals)
        vals.append(i_ticket)
        vals.append(i_user)
        vals = tuple(vals)
        out = self.model.update_compra(fields,vals)
        if(out == True):
            self.view.ok(i_compra,'actualizado')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR. REVISA')
    
    def delete_compra(self):
        self.view.msg('Se recomienda saber la clave (ID)  para eliminarlo.')
        self.view.msg('Ingrese OK para continuar o cualquier tecla para cancelar y volver al menú anterior.')
        resp = input()
        if(resp.upper() != 'OK'):
            return
        i_ticket, i_user =  self.ask_compra()
        count = self.model.delete_compra(i_ticket,i_user)
        if count != 0:
            self.view.ok_double_id(i_ticket,i_user,'elimino')
        else:
            self.view.error("NO SE PUDO ELIMINAR. REVISA")


    def read_compra(self):
        self.view.ask('ID COMPRA: ')
        i_compra = input()
        compra = self.model.read_compra(i_compra)
        if( type(compra) == tuple):
            r_compra = self.model.read_compra_information(i_compra)
            usuario = self.model.read_user(compra[2])
            self.view.ver_usuario_header("DATOS DEL USUARIO")
            self.view.ver_usuario(usuario)
            self.view.ver_compra_header('Datos del compra ' + i_compra)
            self.view.ver_compra(r_compra)
            self.view.ver_compra_midder()
            self.view.ver_compra_footer()
        else:
            if compra == None:
                self.view.error('NO EXISTE REGISTRO')
            else:
                self.view.error('ERROR AL RECUPERAR LOS DATOS. ¡Revisa!')
        return




#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------CONTROLLER FOR USERS-----------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def ver_cartelera(self):
        records = self.model.cartelera()
        if(type(records) == list):
            self.view.ver_cartelera_header('CARTELERA CINE')
            for record in records:
                self.view.ver_cartelera(record)
            self.view.ver_cartelera_midder()
            self.view.ver_cartelera_footer()
        else:
            print("ERROR AL CARGAR LA CARTELERA. POR FAVOR INTENTELO MAS TARDE")

    def ver_pelicula_nombre_cartelera(self):
        self.view.ask("Nombre de la pelicula: ")
        Nombre = input()
        records = self.model.read_pelicula_nombre_cartelera(Nombre)
        if(type(records) == list):
            self.view.ver_cartelera_header('CARTELERA CINE POR: ' + Nombre)
            for record in records:
                self.view.ver_cartelera(record)
            self.view.ver_cartelera_midder()
            self.view.ver_cartelera_footer()
        else:
            print("ERROR AL CARGAR LA CARTELERA. POR FAVOR INTENTELO MAS TARDE")

    def ver_pelicula_genero_cartelera(self):
        self.view.ask("Genero de la pelicula: ")
        Genero = input()
        records = self.model.read_pelicula_genero_cartelera(Genero)
        if(type(records) == list):
            self.view.ver_cartelera_header('CARTELERA CINE POR: ' + Genero)
            for record in records:
                self.view.ver_cartelera(record)
            self.view.ver_cartelera_midder()
            self.view.ver_cartelera_footer()
        else:
            print("ERROR AL CARGAR LA CARTELERA. POR FAVOR INTENTELO MAS TARDE")


    def elegirsala(self,nombre):
        records_pelisalas = self.model.read_all_pelisala_by_pelicula_nombre(nombre)
        list_salas = []
        if(type(records_pelisalas) == list):
            self.view.ver_pelisala_header("Elija el tipo de sala (Tradicional, 3D, VIP) seleccionando la clave.")
            for ps in records_pelisalas:
                list_salas.append(str(ps[0]))
                self.view.ver_pelisala_compra(ps)
            self.view.ver_pelisala_midder()
            self.view.ver_pelisala_footer()
            self.view.ask("INGRESE LA CLAVE: ")
            i_pelisala = input()
            if(i_pelisala in list_salas):
                return i_pelisala
            else:
                return None
        else:
            print("LA PELICULA AUN NO LLEGA AL CINE")
            return None


    def elegirasiento(self,i_sala):
        self.view.ask("Seleccione un asiento\n")
        n_sala = self.model.read_sala(i_sala)
        n_sala = n_sala[1]
        c = 0
        record_asientos = self.model.read_asientos_disponibles(n_sala)
        for i in range(len(record_asientos)-1):
            c += 1
            fila = record_asientos[i][0]
            asiento = record_asientos[i][1]
            print(fila,"",asiento, end="    ")
            if(record_asientos[i][0] != record_asientos[i+1][0]):
                print("\n")
        fila = record_asientos[c][0]
        asiento = record_asientos[c][1]
        print(fila,"",asiento)
        print("\n")
        n_fila = input("FILA: ")
        n_asiento = input("ASIENTO: ")
        i_asiento = self.model.read_asiento_by_fila_asiento(n_fila,n_asiento)
        verify = self.model.update_estado_asiento_ocupado(i_sala,i_asiento)
        if(verify == True):
            return [i_asiento]
        else:
            self.view.error("EL ASIENTO ESTA OCUPADO")
            return None

    def comprar_boleto(self):
        self.view.ask("Ingrese su nombre de usuario para realizar una compra: ")
        N_Usuario = input()
        verify = self.model.user_verification_user(N_Usuario)
        if(verify != True):
            self.view.error("USUARIO INCORRECTO")
            return
        i_user = self.model.read_thisuser_byuser_compra(N_Usuario)
        if(i_user == None):
            self.view.error("EL USUARIO ES INCORRECTO")
        self.view.ask("Ingrese el Nombre de la pelicula: ")
        Nombre = input()
        records_peliculas = self.model.read_pelicula_nombre_cartelera_compra(Nombre)
        if(type(records_peliculas) == list and records_peliculas!=[]):
            self.view.ver_cartelera_header('CARTELERA CINE POR: ' + Nombre)
            for record in records_peliculas:
                self.view.ver_cartelera_compra(record)
            self.view.ver_cartelera_midder()
            self.view.ver_cartelera_footer()
        else:
            self.view.error("NO EXISTE LA PELICULA")
            return
        self.view.ask("INGRESE LA CLAVE: ")
        i_pelihorario = input()
        i_pelicula = self.model.read_pelicula_by_pelihorario(i_pelihorario)
        pelicula = self.model.read_pelicula(i_pelicula)
        i_pelisala = self.elegirsala(pelicula[1])
        if(i_pelisala == None):
            self.view.error("LA SALA QUE ELEGISTE NO EXISTE.")
            return
        i_sala = self.model.read_sala_by_idpelisa(i_pelisala)
        if(i_sala == None):
            self.view.error("LA SALA NO EXISTE")
            return
        i_sala = i_sala[0]
        i_asiento = self.elegirasiento(i_sala)
        if(i_asiento == None):
            return
        i_asiento = i_asiento[0]
        i_sala_asiento = self.model.read_sala_asiento_ticket(i_sala,i_asiento)
        self.view.ask("TU COMPRA ESTA PREPARADA. INGRESA TU CONTRASEÑA PARA CONFIRNMAR TU COMPRA O CANCELALA CON 'C' \n")
        password = input()
        if(password.upper() == 'C'):
            self.view.end()
            return
        else:
            i_user = str(i_user)
            v_user = self.model.password_verification_compra(i_user,password)
            if(v_user == True):
                b_ticket = self.model.create_new_ticket(i_pelihorario,i_sala_asiento)
                if(b_ticket == True):
                    r_ticket = self.model.read_ticket_by_phsa(i_pelihorario,i_sala_asiento)
                    b_compra = self.model.create_new_compra(r_ticket[0],i_user)
                    if(b_compra == True):
                        print("LA COMPRA SE REALIZO CORRECTAMENTE")
                        self.view.ask("VER DETALLES DE LA COMPRA Y/N: ")
                        resp = input()
                        i_compra = self.model.read_compra_byuser_ticket(r_ticket[0],i_user)
                        if(resp.upper() == 'Y'):
                            r_compra = self.model.read_compra_information(i_compra)
                            if(type(r_compra) == tuple):
                                self.view.ver_compra_header("DETALLES DE LA COMPRA")
                                self.view.ver_compra(r_compra)
                                self.view.ver_compra_midder()
                                self.view.ver_compra_footer()
                                return
                            else:
                                self.view.error("HUBO UN PROBLEMA AL CARGAR TUS DATOS, COMUNICATE CON UN ADMINISTRADOR Y ENTREGA LA CLAVE DE COMPRA" + str(i_compra))
                        else:
                            self.view.msg("CLAVE PARA ENTREGAR AL CINE: ")
                            self.view.ver_clave_cine(str(i_compra))
                            return
                else:
                    self.view.error("NO SE PUDO REALIZAR TU COMPRA. INTENTALO DE NUEVO")
                    return
            else:
                print(v_user)
                return

    def buscar_boleto(self):
        self.view.ask("Ingrese la clave de compra: ")
        i_compra = input()
        record = self.model.read_boleto_comprado(i_compra)
        if(type(record) == tuple):
            self.view.ver_compra_header("DETALLES DE LA COMPRA")
            self.view.ver_boleto_comprado(record)
            self.view.ver_compra_midder()
            self.view.ver_compra_footer()
            return
        else:
            self.view.error("LA COMPRA NO EXISTE")


