menuprincipal = ["1. Empleados","2. Cursos","3. Temas","4. Vídeos","5. Temas asignados a un curso","6. Vídeos asignados a un tema", "7. Salir"]

submenu = ["1. Agregar","2. Eliminar","3. Modificar","4. Consultar todo","5. Ver información específica"]

from os import system,name
def limpiar_pantalla():
    if name == "nt":
        system("cls")
    else:
        system("clear")

from video import *
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

            if OpUsuario == 4:
                Video.OpcionDeVideo(OpUsuario2)
                print("-"*40)


        elif OpUsuario == 7:
            print("Programa Terminado")
            break
main()    