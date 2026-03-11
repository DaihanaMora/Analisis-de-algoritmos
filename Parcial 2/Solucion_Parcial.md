
##### Punto 1 ####

# Enlace al problema en LeetCode: https://leetcode.com/problems/assign-cookies/
# Código de la solución :
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

# Pantallazo o comprobante de Accepted:  Adjunto con nombre Punto1.png
# análisis de complejidad:
        Complejidad tiempo: O(nlogn + mlogm) El tiempo total depende principalmente de ordenar los dos arreglos (niños y galletas). 
        Después de ordenar, solo se recorren las listas una vez para hacer los emparejamientos, lo cual es un proceso lineal que no aumenta 
        el orden de complejidad

        Complejidad espacio: O(1) Es espacio constante porque la memoria que usa nuestro código no crece si el problema se hace más grande. 
        Solo utilizamos un par de variables (contadores) para llevar el control, sin crear listas o estructuras adicionales.

# justificación greedy: 
        Elegir g[child_i] y s[cookie_j] más pequeño posible garantiza que conservamos las galletas de mayor tamaño 
        para los casos donde son estrictamente necesarias maximizando así el número total de niños satisfechos sin necesidad de
        explorar otras combinaciones.

##### Punto 2 ####

# Enlace al problema en LeetCode: [https://leetcode.com/problems/assign-cookies/](https://leetcode.com/problems/non-overlapping-intervals/)
# Código de la solución :
class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        if not intervals:
            return 0  
        intervals.sort(key=lambda x: x[1])
        count_removed = 0
        last_end = intervals[0][1]
        for i in range(1, len(intervals)):
            current_start = intervals[i][0]
            current_end = intervals[i][1]
            if current_start < last_end:
                count_removed += 1
            else:
                last_end = current_end
        return count_removed

# Pantallazo o comprobante de Accepted:  Adjunto con nombre Punto2.png
# análisis de complejidad:
        Complejidad tiempo: O(nlogn) La mayor parte del trabajo ocurre al ordenar los intervalos según su tiempo de finalización. 
        Una vez ordenados, el algoritmo simplemente los compara uno por uno en una sola pasada para identificar cuáles se solapan.

        Complejidad espacio: O(1) El uso de memoria es mínimo y fijo. Solo necesitamos guardar el conteo de intervalos eliminados y el tiempo de fin del último intervalo aceptado. 
        No importa cuántosintervalos recibamos, el consumo de memoria extra será siempre el mismo.

# justificación greedy: 
        Al elegir el intervalo que termina más pronto, dejamos el máximo tiempo libre restante para acomodar otros intervalos. 
        Cualquier otra elección (elegir un intervalo que termine después) solo podría reducir las opciones para los intervalos futuros. Por lo tanto, 
        la elección local de "terminar lo antes posible" asegura que no estamos bloqueando de forma innecesaria intervalos que vienen después.
