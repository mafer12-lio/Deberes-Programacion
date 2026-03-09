asientos = [[0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
            ]
f = int(input("INGRESA FILA (0 a 2): "))
c = int(input("INGRESA COLUMNA (0 a 3): "))

asientos[f][c]  = 1

for i in range(3):
    for j in range(4):
        print(asientos[i][j], end= " ")
        print ()