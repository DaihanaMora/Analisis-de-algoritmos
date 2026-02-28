class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        """
        se utilizo el has set
        Tiempo : O(n) se recorre la lista una vez
        Espacio: O(n) para el peor caso se almacena todos los elementos en el set
        Utilizamos el set para obtener que la busqueda de elementos sea de tiempo
        constante 0(1); si al iterar se encuentra un número que  ya existe en el set,
        se confirma el duplicado
        """
        vistos = set()
        
        for numero in nums:
            
            if numero in vistos:
                return True
           
            vistos.add(numero)
            
        return False