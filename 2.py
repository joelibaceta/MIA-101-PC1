import math

def calcular_serie(x, n):
    """
    Calcula el valor de la serie para los valores dados de x y n:
    S = x^(2n+1)/3! - x^(2n-1)/5! + x^(2n-3)/7! - ...
    """

    signo = 1  # Controla el signo de cada término (+ o -)
    suma = 0  # Almacena el resultado de la serie

    # Generación de la serie
    for k in range(n):  # La serie tiene n términos
        # Calcular el exponente: 2n + 1 - 2k
        exponente = 2 * n + 1 - 2 * k
        
        # Calcular la potencia x^exponente sin usar el operador de potencia
        potencia = 1
        for _ in range(exponente):
            potencia *= x
        
        # Calcular el factorial (3 + 2k)! sin usar funciones de factorial
        factorial = 1
        for i in range(1, 3 + 2 * k + 1):
            factorial *= i
        
        # Agregar el término a la suma, considerando el signo
        suma += signo * (potencia / factorial)
        
        # Cambiar el signo para el siguiente término
        signo *= -1
    
    return suma

# Prueba del algoritmo con x = 2 y n = 5
x = 2
n = 5
resultado = calcular_serie(x, n)

print(f"El resultado de la serie para x = {x} y n = {n} es: {resultado}")