"""
Problema resuelto por medio de fuerza bruta. 
Se itera sobre la cadena y se eliminan los caracteres repetidos adyacentes, contando cuántos se han eliminado. 
El proceso se repite hasta que no queden caracteres repetidos adyacentes.

COMPLEJIDAD: O(n^2) en el peor caso, cuando todos los caracteres son iguales. 
Porque cada eliminación puede requerir recorrer la cadena nuevamente. 
"""

n = int(input())
s = list(input().strip())

i = 0
removed = 0

while i < len(s) - 1:
    if s[i] == s[i + 1]:
        s.pop(i)
        removed += 1
        if i > 0:
            i -= 1
    else:
        i += 1

print(removed)