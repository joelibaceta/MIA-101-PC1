import serial

def crear_tablero_n_diagonal(n):
    """
    Crea un tablero 'n-diagonal' de tamaño n x (n+1) siguiendo el patrón cíclico diagonal.
    """
    tablero = [[0] * (n + 1) for _ in range(n)]  # Crear una matriz vacía
    numero = 1  # Número inicial para rellenar
    i, j = 0, 0  # Coordenadas iniciales

    # Rellenar el tablero siguiendo el patrón
    while numero <= n * (n + 1):
        tablero[i][j] = numero
        numero += 1
        # Moverse a la siguiente casilla diagonal
        i += 1
        j += 1
        if i >= n:  # Si excede el límite inferior, regresar al principio
            i = 0
        if j >= n + 1:  # Si excede el límite derecho, regresar al principio
            j = 0

    return tablero


def eliminar_menor_por_fila(tablero):
    """
    Elimina el menor elemento de cada fila del tablero.
    """
    nuevo_tablero = []
    for fila in tablero:
        menor = min(fila)
        nueva_fila = [x for x in fila if x != menor]  # Crear fila sin el menor elemento
        nuevo_tablero.append(nueva_fila)
    return nuevo_tablero


# Ejemplo con n = 4
n = 4
tablero = crear_tablero_n_diagonal(n)
nuevo_tablero = eliminar_menor_por_fila(tablero)

# Mostrar los resultados
import pandas as pd

# Tablero original
tablero_df = pd.DataFrame(tablero)
tools.display_dataframe_to_user(name="Tablero 'n-diagonal'", dataframe=tablero_df)

# Tablero después de eliminar el menor de cada fila
nuevo_tablero_df = pd.DataFrame(nuevo_tablero)
tools.display_dataframe_to_user(name="Tablero sin menor elemento de cada fila", dataframe=nuevo_tablero_df)