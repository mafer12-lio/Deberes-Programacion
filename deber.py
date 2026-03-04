Matriz = []

for i in range (5):
    fila =[]
    for j in range (5):
        numero = int(input(f"Ingreso el valor para [{i}] [{j}]: "))
        fila.append(numero)
    Matriz.append(fila) 

print("\n Matriz ingresada: \n")

for fila in Matriz:
    for numero in fila:
        print (numero, end="\t")
    print ()
    