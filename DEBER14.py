
def calcular_promedio (nota_1, nota_2, nota_3):
    total = (nota_1 + nota_2 + nota_3) / 3
    return total
n1 = float(input("Ingresa la primera nota: "))
n2 = float(input("Ingresa la segunda nota: "))
n3 = float(input("Ingresa la tercera nota: "))

resultado = calcular_promedio (n1, n2, n3) 

print (f"el promedio es: {resultado:.2f}")

