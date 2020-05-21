menuprincipal = ["1. Empleados","2. Cursos","3. Temas","4. Vídeos","5. Temas asignados a un curso","6. Vídeos asignados a un tema", "7. Salir"]

submenu = ["1. Agregar","2. Eliminar","3. Modificar","4. Consultar todo","5. Ver información específica"]

from os import system,name
def limpiar_pantalla():
    if name == "nt":
        system("cls")
    else:
        system("clear")