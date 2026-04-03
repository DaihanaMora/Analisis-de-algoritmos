## Punto 1

### Enlace al problema en LeetCode: 
 https://leetcode.com/problems/longest-increasing-subsequence/
 
### Código de la solución:
```
class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        if not nums:
            return 0
        
        tails = []
        
        for num in nums:       
            left, right = 0, len(tails)
            
            while left < right:
                mid = (left + right) // 2
                if tails[mid] < num:
                    left = mid + 1
                else:
                    right = mid
            
            if left == len(tails):
                tails.append(num)
            else:
               
                tails[left] = num
                
        return len(tails)
```
### Pantallazo o comprobante de Accepted:  
![Accepted Leetcode Punto 1](Punto1.png)

### Estado DP:
       Estado DP: tails[i] representa el valor más pequeño posible en el que puede terminar una subsecuencia estrictamente creciente de longitud i + 1. 
       Al mantener el valor final más pequeño para cada longitud posible, maximizamos las oportunidades de que los elementos restantes del arreglo puedan extender dichas subsecuencias. Por ejemplo, si tenemos las secuencias [2, 5, 7] y [1, 3, 4], ambas de longitud 3, el estado tails[2] almacenará el valor 4, ya que es un final más "prometedor" para encontrar números mayores a futuro que el 7

       Complejidad tiempo:  O(n log n). El bucle externo recorre los $n$ elementos del arreglo, y la búsqueda binaria interna toma un tiempo de log n.
       
       Complejidad espacio: O(n), ya que en el peor de los casos (una lista estrictamente creciente), el arreglo tails tendrá el mismo tamaño que nums.

