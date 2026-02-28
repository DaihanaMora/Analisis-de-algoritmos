def isAnagram(self, s: str, t: str) -> bool:
    """
    Verifica que ambas cadenas tengan la misma longitud.
    Cuenta la frecuencia de cada carácter en la primera cadena.
    Resta las frecuencias usando la segunda cadena.
    Si todas las frecuencias coinciden, son anagramas.

    Complejidad:
    Tiempo: O(n), ya que se recorre cada cadena una sola vez.
    Espacio: O(k), donde k es el número de caracteres distintos.
    """
    if len(s) != len(t):
        return False

    frecuencia = {}

    for c in s:
        frecuencia[c] = frecuencia.get(c, 0) + 1

    for c in t:
        if c not in frecuencia:
            return False
        frecuencia[c] -= 1
        if frecuencia[c] < 0:
            return False

    return True