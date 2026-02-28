"""
Complejidad:
- Tiempo: O(n²) en el peor caso, porque cada eliminación (pop) cuesta O(n)
  y puede realizarse hasta n veces.
- Espacio: O(n), debido a la conversión del string en lista mutable.

El algoritmo simula eliminaciones reales, lo que introduce desplazamientos
internos en la lista y aumenta el costo total.
"""

n = int(input())
s = input().strip()

count = 0
for i in range(1, n):
    if s[i] == s[i - 1]:
        count += 1

print(count)