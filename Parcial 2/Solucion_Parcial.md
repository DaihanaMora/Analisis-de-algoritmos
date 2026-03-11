# Análisis de Algoritmos

Material de introducción al análisis de algoritmos, complejidad computacional y programación competitiva.

---

## ¿Qué es la Complejidad Big O?

**Big O** (notación O grande) es una forma de describir **cuánto crece el tiempo o el espacio** que necesita un algoritmo cuando el tamaño de la entrada crece.

### Idea principal

- No medimos segundos ni megabytes exactos.
- Medimos **cómo escala** el algoritmo: si duplicamos la entrada, ¿el tiempo se duplica, se cuadruplica o casi no cambia?

### Notación

Se escribe **O( f(n) )**, donde **n** es el tamaño de la entrada (por ejemplo, cantidad de elementos en un arreglo).

| Notación   | Nombre        | Ejemplo típico                    | Comportamiento al crecer n |
|-----------|----------------|------------------------------------|----------------------------|
| **O(1)**  | Constante      | Acceso a un índice en un arreglo   | No depende de n            |
| **O(log n)** | Logarítmica | Búsqueda binaria                  | Crece muy lento            |
| **O(n)**  | Lineal         | Recorrer un arreglo una vez       | Crece proporcional a n     |
| **O(n log n)** | Linealítmica | Merge sort, muchos sorts eficientes | Entre lineal y cuadrático |
| **O(n²)** | Cuadrática     | Dos ciclos anidados sobre n       | Crece rápido               |
| **O(2ⁿ)** | Exponencial    | Recursión sin memoización típica   | Crece muy rápido           |

### Reglas prácticas

1. **Despreciar constantes**: O(2n) → O(n), O(500) → O(1).
2. **Despreciar términos menores**: O(n² + n) → O(n²).
3. **Peor caso**: Big O suele referirse al **peor caso** de tiempo o espacio.

Con Big O podemos comparar algoritmos y elegir el más adecuado según el tamaño de los datos.

---

## Introducción al Análisis de Algoritmos

El **análisis de algoritmos** consiste en evaluar:

- **Tiempo**: cuántas operaciones básicas se ejecutan (en función del tamaño de la entrada).
- **Espacio**: cuánta memoria adicional se usa (variables, estructuras, recursión).

### Objetivos

1. **Predecir rendimiento** sin implementar en todos los entornos.
2. **Comparar** distintas soluciones al mismo problema.
3. **Detectar cuellos de botella** y saber si una solución escalará bien.

### Cómo se analiza

1. Identificar **operaciones básicas** (comparaciones, asignaciones, accesos a memoria).
2. Expresar su cantidad en función de **n** (tamaño de la entrada).
3. Simplificar usando la notación Big O (quedarse con el término dominante y sin constantes).

Así pasamos de “cuenta exacta de operaciones” a una clase de complejidad como O(n) u O(n²), que es lo que suele usarse en la práctica y en programación competitiva.

---

## ¿Qué es la Programación Competitiva?

La **programación competitiva** es un tipo de competición donde se resuelven problemas algorítmicos bajo **límites de tiempo y memoria** estrictos.

### Características

- Problemas con **entrada/salida** bien definida y casos de prueba automáticos.
- Soluciones que deben ser **correctas** y además **eficientes** (complejidad adecuada).
- Uso de **Big O** para decidir si una idea cabe en tiempo (y memoria) antes de implementar.

### Habilidades que se desarrollan

- Pensar en **complejidad** (tiempo y espacio).
- Elegir **estructuras de datos** (arreglos, mapas, conjuntos, pilas, colas).
- Reducir un problema a **patrones** conocidos (búsqueda, ordenamiento, dos punteros, etc.).

### Plataformas habituales

- LeetCode, Codeforces, AtCoder, HackerRank, SPOJ, entre otras.

El ejercicio **Two Sum** es un clásico de entrevistas y de programación competitiva; a continuación se presenta con solución directa y optimizada, y su análisis de complejidad.

---

## Ejercicio: Two Sum

### Enunciado

Dado un arreglo de enteros `nums` y un entero `target`, devolver **índices** de dos números que sumen `target`.  
Puedes asumir que existe exactamente una solución y no debes usar el mismo elemento dos veces.

**Ejemplo:**

- Entrada: `nums = [2, 7, 11, 15]`, `target = 9`
- Salida: `[0, 1]` (porque `nums[0] + nums[1] = 2 + 7 = 9`)

---

### Solución 1: Fuerza bruta (normal)

Recorrer todos los pares de índices `(i, j)` con `i < j` y comprobar si `nums[i] + nums[j] == target`.

```python
def two_sum_brute_force(nums: list[int], target: int) -> list[int]:

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
```

**Complejidad:**

- **Tiempo:** O(n²). Hay dos ciclos anidados que en total revisan O(n²) pares.
- **Espacio:** O(1). Solo variables de índices y constantes.

Funciona bien para **n** pequeño; para **n** grande suele dar “Time Limit Exceeded” en jueces online.

---

### Solución 2: Hash map (optimizada)

En un solo recorrido guardamos en un diccionario **valor → índice**. Para cada `nums[i]` calculamos `complemento = target - nums[i]`. Si `complemento` ya está en el diccionario, esos dos índices son la respuesta.

```python
def two_sum_optimized(nums: list[int], target: int) -> list[int]:
    visto = {}  # valor -> índice
    for i, num in enumerate(nums):
        complemento = target - num
        if complemento in visto:
            return [visto[complemento], i]
        visto[num] = i
    return []
```

**Complejidad:**

- **Tiempo:** O(n). Un solo recorrido; cada búsqueda e inserción en el diccionario es O(1) en promedio.
- **Espacio:** O(n). En el peor caso guardamos casi todos los elementos en `visto`.

---

### Comparación y análisis de complejidad

| Criterio   | Fuerza bruta | Hash map   |
|-----------|--------------|------------|
| Tiempo    | O(n²)        | O(n)       |
| Espacio   | O(1)         | O(n)       |
| Uso típico| n pequeño    | n grande   |

- Para **n grande**, la solución con hash map es la estándar: evita el límite de tiempo.
- La fuerza bruta es más fácil de entender y no usa memoria extra; sirve para verificar la lógica o cuando **n** es muy pequeño.

Este ejemplo ilustra cómo el **análisis de complejidad (Big O)** guía la elección del algoritmo en problemas de programación competitiva y en entrevistas técnicas.

---

## Resumen

1. **Big O** describe cómo crece el tiempo o el espacio de un algoritmo con el tamaño de la entrada.
2. El **análisis de algoritmos** usa Big O para comparar y predecir el rendimiento.
3. En **programación competitiva** se exige que las soluciones sean correctas y eficientes.
4. **Two Sum** se puede resolver en O(n²) con fuerza bruta o en O(n) con un hash map; la versión optimizada es la recomendada para entradas grandes.
