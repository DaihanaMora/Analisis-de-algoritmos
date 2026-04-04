## Punto 1

### Enlace al problema en LeetCode: 
 https://leetcode.com/problems/longest-increasing-subsequence/
 
### Código de la solución:
```python
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

## Punto 2

### Enlace al problema en LeetCode: 
 https://leetcode.com/problems/word-break/
 
### Código de la solución:
```python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break               
        return dp[n]
```
### Pantallazo o comprobante de Accepted:  
![Accepted Leetcode Punto 2](Punto2.png)

### Análisis de Complejidad (Big O) : 
    Tiempo: O(n^2.k) tenemos un bule externo que recorre la cadena de n, 
    un bucle interno que busca el punto de corte de j (n) , la operacion de slicing s[j:i] y 
    la búsqueda en el conjunto toman O(k) donde k es la longitud de la palabra 
    (en Python, el slicing de strings es O(k)).
    
    Espacio: O(n+m.k) O(n) para el arreglo dp.
    O(m.k)para almacenar el diccionario en un set, donde m es el número de palabras y k su longitud promedio.
### Estado DP : 
    dp[i]: Representa específicamente si la subcadena que termina justo antes del índice i es procesable.
    Implementación eficiente: Usamos break en el bucle interno: en cuanto encontramos un punto de corte j 
    que hace que el prefijo sea válido, no necesitamos probar otros cortes para esa i específica.
### Problemas en una y dos dimensiones, y patrones típicos:
    Dimensión: Es un problema de 1D (una dimensión). Aunque usamos dos índices (i, j), el estado se representa en un 
    arreglo lineal dp[i] que rastrea el progreso a lo largo de la cadena.
    
    Patrón de Partición: A diferencia de "Decode Ways" donde los saltos eran fijos (1 o 2), aquí el "salto" es variable. 
    Es un patrón típico donde debemos decidir dónde "cortar" la cadena para que los fragmentos sean válidos.
    
    Restricciones: El uso de un set para el diccionario es una restricción de eficiencia necesaria para evitar una 
    complejidad O(n^2. m) si buscáramos en una lista.

## Punto 3

### Enlace al problema en LeetCode: 
https://leetcode.com/problems/decode-ways/
 
### Código de la solución: 
```python
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1 
        for i in range(2, n + 1):
            if s[i-1] != '0':
                dp[i] += dp[i-1]
            two_digit = int(s[i-2:i])
            if 10 <= two_digit <= 26:
                dp[i] += dp[i-2]            
        return dp[n]
```
### Pantallazo o comprobante de Accepted:  
![Accepted Leetcode Punto 3](Punto3.png)   

### Análisis de Complejidad (Big O) :
    Tiempo: Tiempo: O(n)Recorremos la cadena una sola vez. En cada paso, las operaciones de conversión a entero y comparación 
    son constantes ya que el tamaño del substring es máximo 2.
    
    Espacio: Espacio: O(n) Utilizamos un arreglo dp de tamaño n + 1
    Se podría optimizar a O(1) usando solo dos variables para guardar dp[i-1] y dp[i-2].
### Estado DP : 
    dp[i]:representa el acumulado de caminos válidos encontrados hasta la longitud i
### Problemas en una y dos dimensiones, y patrones típicos:
    Dimensión:Dimensión: Problema de 1D. El estado depende únicamente de la posición actual en la cadena.
    
    Patrón de Restricción: El dígito '0' es el principal obstáculo. Un '0' no puede decodificarse solo,
    y solo es válido si está precedido por '1' o '2'. Si hay un '0' que no cumple esto (ej. "30" o "05"), 
    la cadena es inválida.
   
## Punto 5

### Enlace al problema en Leetcode: 
https://leetcode.com/problems/partition-equal-subset-sum/

### Codigo de la solucion:

```python
from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        total = sum(nums)
        
        # Si la suma es impar, no se puede dividir en dos partes iguales
        if total % 2 != 0:
            return False
        
        target = total // 2
        
        dp = [False] * (target + 1)
        dp[0] = True
        
        for num in nums:
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]
        
        return dp[target]        
```
### Pantallazo o comprobante de Accepted:  
![Accepted Leetcode Punto 5](Punto5.png)

### Análisis de Complejidad (Big O):

**Tiempo:** O(n*target) -> Se recorren todos los numeros del arreglo y para cada uno, iteramos hasta `target`.

Donde: 
* `n` es la cantidad de elementos
* `target=sum(nums)/2`

**Espacio:** O(target) -> Se utiliza un arreglo `dp` dew tamaño `target+1`. (Sol. de espacio respecto a una solucion 2D)

### Estado DP:

`dp[j]`: Indica si es posible formar una suma `j` usando algunos elementos del arreglo.

