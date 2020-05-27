from os import system,name
def limpiar_pantalla():
    if name == "nt":
        system("cls")
    else:
        system("clear")
menuprincipal = ["1. Empleados","2. Cursos","3. Temas","4. Vídeos","5. Temas asignados a un curso","6. Vídeos asignados a un tema", "7. Salir","-----------------------------------"]

submenu = ["-----------------------------------","            [SubMenu]","-----------------------------------","1. Agregar","2. Eliminar","3. Modificar","4. Consultar todo","5. Ver información específica","-----------------------------------"]

limpiar_pantalla()

from video import *
from temas import *
from empleado import Empleado
from curso_tema import *
from cursos import *
from curso_tema_video import *

#-----------------------------------------------------------------------------------------------------------------
def main():
    while True:
        print("-----------------------------------\n         [Menú Principal]\n-----------------------------------\nEliga la Base de Datos a manipular:\n")
        #Menú Principal---------(Empleado, curso, tema, video, tema asignado a curso, video asignado a tema)-----
        for a in menuprincipal:
            print(a)
            OpUsuario = 0
        try:
            OpUsuario = int(input("Opción: "))
            limpiar_pantalla()
            if OpUsuario < 1 or OpUsuario > 7:
                print("Opción no válida")
                print("-"*35)
            elif OpUsuario == 7:
                print("Programa Terminado")
                break
            #Submenú-----------(Agregar, Eliminar, Modificar, Consultar todo, Consulta especifica)------------
            elif OpUsuario > 0 and OpUsuario < 7:
                for b in submenu:
                    print(b)
                try:
                    OpUsuario2 = int(input("Opción: "))
                    limpiar_pantalla()
                    if OpUsuario2 < 1 or OpUsuario2 > 5:
                        print("Opción no válida")
                        print("-"*35)
                    else:
                    
                        if OpUsuario == 1:
                            Empleado.OpciondeEmpleado(OpUsuario2)
                            print("-"*35)
                        elif OpUsuario == 2:
                            Curso.gestion_cursos(OpUsuario2)
                            print("-"*35)

                        elif OpUsuario == 3:
                            TEMAS.Opciones(OpUsuario2)
                            print("-"*35)
                    
                        elif OpUsuario == 4:
                            Video.OpcionDeVideo(OpUsuario2)
                            print("-"*35)

                        elif OpUsuario == 5:
                            Curso_Tema.opcionct(OpUsuario2)
                            print("-"*35)

                        elif OpUsuario == 6:
                            CursoTemaVideo.OpcionCTV(OpUsuario2)
                            print("-"*35)
                except:
                    limpiar_pantalla()
                    print("Opcion no válida")
                    print("-"*35)
            
        except:
            limpiar_pantalla()
            print("Opcion no válida")
            print("-"*35)
main()    