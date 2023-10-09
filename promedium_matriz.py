# Escribe una función para encontrar el promedio de los elementos en una matriz de números flotantes

# CASE ONE 1
matriz_b  = [
    [2.1,4.5,3.4],
    [3.8,4.4,3.2],
    [8.2,3.3,1.8]
    ]

join_arrays_b= matriz_b[0] + matriz_b[1] + matriz_b[2]
suma = 0
for i in range(0,len(join_arrays_b)):
    suma = join_arrays_b[i] + suma





# CASE TWO 2
def promedium_matriz(matriz):
    denominador = 0
    sum = 0
    join_arrays = []
    for j in range(0,len(matriz)):
        join_arrays += matriz[j]
        denominador += len(matriz[j]) 
    for n in range(0,len(join_arrays)):
        sum += join_arrays[n]
    sum = round(sum,0)
    result = sum/denominador

    return(round(result,1))

if __name__ == "__main__":
    
    matriz_b = [
        [2.2,4.5,5.3],
        [3.2,9.9,12.7]
    ]
    
    print(promedium_matriz(matriz_b))