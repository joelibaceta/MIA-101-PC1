def calcular_sumas_subconjuntos(n, arreglo):
    """
    Calcula las sumas posibles de los subconjuntos de un arreglo de n elementos.
    """
    sumas = set()
    for i in range(1, 2**n):
        suma = 0
        for j in range(n):
            if i & (1 << j):
                suma += arreglo[j]
        sumas.add(suma)
    sumas = sorted(sumas)
    return sumas

# Ejemplo
n = 4
arreglo = [1, 2, 5, 10]

sumas = calcular_sumas_subconjuntos(n, arreglo)
print("Las sumas posibles son:", sumas)

# Probando la función con el ejemplo
assert sumas == [1, 2, 3, 5, 6, 7, 8, 10, 11, 12, 13, 15, 16, 17, 18]