estudiantes = []
for i in range(3) :
    nombre = input("Ingrese un nombre: ")
    estudiantes.append(nombre)
    print("\n Lista de estudiantes:")
    for estudiante in estudiantes:
        print(estudiante)
eliminar = input ("\n Ingrese el nombre a eliminar: ")
if eliminar in estudiantes:
    estudiantes. remove(eliminar)
    print("Estudiante eliminado.")
else:
    print("No se encuentra el estudiante. ")
print("\nlista final: ")
for estudiante in estudiantes:
    print(estudiante)
    