from menus import menuprincipal, submenu, limpiar_pantalla

#-----------------------------------------------------------------------------------------------------------------
def main():
    while True:
        print("Menú Principal")
        #Menú Principal---------(Empleado, curso, tema, video, tema asignado a curso, video asignado a tema)-----
        for a in menuprincipal:
            print(a)
            OpUsuario = 0
        try:
            OpUsuario = int(input("Opción: "))
            limpiar_pantalla()
            if OpUsuario < 1 or OpUsuario > 7:
                print("Opción no válida")
        except:
            limpiar_pantalla()
            print("Opcion no válida")
        #Submenú-----------(Agregar, Eliminar, Modificar, Consultar todo, Consulta especifica)------------
        if OpUsuario > 0 and OpUsuario < 7:
            for b in submenu:
                print(b)
            try:
                OpUsuario2 = int(input("Opción: "))
                limpiar_pantalla()
                if OpUsuario2 < 1 or OpUsuario2 > 5:
                    print("Opción no válida")
            except:
                limpiar_pantalla()
                print("Opcion no válida")


            #Agregar---------------------------------------------
            if OpUsuario2 == 1:
                if OpUsuario == 1:
                    pass

                elif OpUsuario == 2:
                    pass

                elif OpUsuario == 3:
                    pass

                elif OpUsuario == 4:
                    pass
                
                elif OpUsuario == 5:
                    pass

                else:
                    pass


            #Eliminar---------------------------------------------
            elif OpUsuario2 == 2:
                if OpUsuario == 1:
                    pass

                elif OpUsuario == 2:
                    pass

                elif OpUsuario == 3:
                    pass

                elif OpUsuario == 4:
                    pass

                elif OpUsuario == 5:
                    pass

                else:
                    pass


            #Modificar---------------------------------------------
            elif OpUsuario2 == 3:
                if OpUsuario == 1:
                    pass

                elif OpUsuario == 2:
                    pass

                elif OpUsuario == 3:
                    pass

                elif OpUsuario == 4:
                    pass

                elif OpUsuario == 5:
                    pass

                else:
                    pass


            #Consultar todo---------------------------------------
            elif OpUsuario2 == 4:
                if OpUsuario == 1:
                    pass

                elif OpUsuario == 2:
                    pass

                elif OpUsuario == 3:
                    pass

                elif OpUsuario == 4:
                    pass

                elif OpUsuario == 5:
                    pass

                else:
                    pass


            #Información específica--------------------------------
            else:
                if OpUsuario == 1:
                    pass

                elif OpUsuario == 2:
                    pass

                elif OpUsuario == 3:
                    pass

                elif OpUsuario == 4:
                    pass

                elif OpUsuario == 5:
                    pass

                else:
                    pass


        #Opcion para terminar programa--------------------------
        elif OpUsuario == 7:
            break
#-----------------------------------------------------------------------------------------------------       
main()