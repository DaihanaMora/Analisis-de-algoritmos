class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        """
        Se tuliza  dos ciclos for. El primero toma un número 
        y el segundo lo compara con todos los que vienen después. 
        Si se encuentra uno igual, mando True. Si termino todo y no vi nada, False.

        Complejidad (Big O):
        - Tiempo: O(n²) porque al tener un for dentro de otro for, si la lista crece, 
          el tiempo sube al cuadrado. Es lento para listas muy largas.
        - Espacio: O(1) porque no creé ninguna estructura extra (como un set o mapa), 
          solo usé la memoria de la lista que ya me dieron.

        Casos:
        - Mejor caso: Que los dos primeros números sean el duplicado (acaba rápido).
        - Peor caso: Que no haya duplicados, porque el código tiene que hacer 
          todas las comparaciones hasta el final.
        
        """
    
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    return True
        return False