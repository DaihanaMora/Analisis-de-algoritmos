def isAnagram(self, s: str, t: str) -> bool:
    """
    Verifica que ambas cadenas tengan la misma longitud.
    Ordena ambas cadenas y compara los resultados.

    Complejidad:
    Tiempo: O(n log n), debido al costo del ordenamiento con sorted()
    Espacio: O(n), por las estructuras temporales creadas al ordenar.
    """
    if len(s) != len(t):
        return False
    
    return sorted(s) == sorted(t)
