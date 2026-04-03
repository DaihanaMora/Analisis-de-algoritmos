## Punto 1

### Enlace al problema en LeetCode: 
 https://leetcode.com/problems/assign-cookies/
 
### Código de la solución:
```
class Solution(object):
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        child_i = 0
        cookie_j = 0
        while child_i < len(g) and cookie_j < len(s):
            if s[cookie_j] >= g[child_i]:
                child_i += 1 
            cookie_j += 1
        return child_i
```
### Pantallazo o comprobante de Accepted:  
![Accepted Leetcode Punto 1](Punto1.png)

### Estado DP:
       Estado DP: tails[i] representa el valor más pequeño posible en el que puede terminar una subsecuencia estrictamente creciente de longitud i + 1. 
       Al mantener el valor final más pequeño para cada longitud posible, maximizamos las oportunidades de que los elementos restantes del arreglo puedan extender dichas subsecuencias. Por ejemplo, si tenemos las secuencias [2, 5, 7] y [1, 3, 4], ambas de longitud 3, el estado tails[2] almacenará el valor 4, ya que es un final más "prometedor" para encontrar números mayores a futuro que el 7

       Complejidad tiempo:  O(n log n). El bucle externo recorre los $n$ elementos del arreglo, y la búsqueda binaria interna toma un tiempo de log n.
       
       Complejidad espacio: O(n), ya que en el peor de los casos (una lista estrictamente creciente), el arreglo tails tendrá el mismo tamaño que nums.

