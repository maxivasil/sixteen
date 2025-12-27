"""
Logica del juego Sixteen
"""
import random


def crear_tablero(n_filas: int, n_columnas: int) -> list[list[int]]:
    """
    Crea un tablero ordenado, con dimensiones `n_filas` por `n_columnas`.

    El tablero estará representado como una lista de listas de enteros. El
    primer número en la posición `[0][0]` será un 1, el de la izquierda será un
    2, y así sucesivamente hasta completar todos los casilleros, sin repetir
    los números, hasta llegar al número `n_filas * n_columnas`.

    PRECONDICIONES:
        - `n_filas` y `n_columnas` son enteros positivos mayor a uno y menores
        a diez.

    POSTCONDICIONES:
        - la función devuelve un nuevo tablero ordenado de enteros que se puede
        utilizar para llamar al resto de las funciones del módulo.

    EJEMPLO:
        >>> crear_tablero(4, 5)
        [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
        ]
    """
    tablero = []
    for f in range(n_filas):
        fila = []
        for c in range(n_columnas):
            fila.append(c+((f*n_columnas)+1))
        tablero.append(fila)
    return tablero


def rotar_izquierda(tablero: list[list[int]], fila: int) -> bool:
    """Rota la fila del tablero, indicada por el índice `fila`, hacia la
    izquierda.

    Por ejemplo, con `fila=1` y `tablero` como a la izquierda, al finalizar
    la función se modificará el tablero para que quede como en la derecha.
    [[1, 2, 3],           [[1, 2, 3],
     [4, 5, 6],    ==>     [5, 6, 4],
     [7, 8, 9]]            [7, 8, 9]]

    PRECONDICIONES:
        - `tablero` es una lista de lista de enteros de cualquier dimensión.

    POSTCONDICIONES:
        - Si `fila` es un índice de filas válido, la función realiza la
        rotación modificando el tablero y devuelve `True`.
        Caso contrario, no modifica el tablero y devuelve `False`."""
    if fila>(len(tablero)-1) or fila<0:
        return False
    aux = tablero[fila][0]
    for numero in range(len(tablero[fila])-1):
        tablero[fila][numero] = tablero[fila][numero+1]
    tablero[fila][-1] = aux
    return True


def rotar_derecha(tablero: list[list[int]], fila: int) -> bool:
    """Rota la fila del tablero, indicada por el índice `fila`, hacia la
    derecha.

    Por ejemplo, con `fila=1` y `tablero` como a la izquierda, al finalizar
    la función se modificará el tablero para que quede como en la derecha.
    [[1, 2, 3],           [[1, 2, 3],
     [4, 5, 6],    ==>     [6, 4, 5],
     [7, 8, 9]]            [7, 8, 9]]

    PRECONDICIONES:
        - `tablero` es una lista de lista de enteros de cualquier dimensión.

    POSTCONDICIONES:
        - Si `fila` es un índice de filas válido, la función realiza la
        rotación modificando el tablero y devuelve `True`.
        Caso contrario, no modifica el tablero y devuelve `False`."""
    if fila>(len(tablero)-1) or fila<0:
        return False
    aux = tablero[fila][-1]
    for numero in range(len(tablero[fila])-1):
        tablero[fila][-numero-1] = tablero[fila][-numero-2]
    tablero[fila][0] = aux
    return True


def rotar_arriba(tablero: list[list[int]], columna: int) -> bool:
    """Rota la columna del tablero, indicada por el índice `columna`, hacia
    arriba.

    Por ejemplo, con `columna=1` y `tablero` como a la izquierda, al finalizar
    la función se modificará el tablero para que quede como en la derecha.
    [[1, 2, 3],           [[1, 5, 3],
     [4, 5, 6],    ==>     [4, 8, 6],
     [7, 8, 9]]            [7, 2, 9]]

    PRECONDICIONES:
        - `tablero` es una lista de lista de enteros de cualquier dimensión.

    POSTCONDICIONES:
        - Si `columna` es un índice de columnas válido, la función realiza la
        rotación modificando el tablero y devuelve `True`.
        Caso contrario, no modifica el tablero y devuelve `False`."""
    if columna>(len(tablero[0])-1) or columna<0:
        return False
    aux = tablero[0][columna]
    for numero in range(len(tablero)-1):
        tablero[numero][columna] = tablero[numero+1][columna]
    tablero[-1][columna] = aux
    return True


def rotar_abajo(tablero: list[list[int]], columna: int) -> bool:
    """Rota la columna del tablero, indicada por el índice `columna`, hacia
    abajo.

    Por ejemplo, con `columna=1` y `tablero` como a la izquierda, al finalizar
    la función se modificará el tablero para que quede como en la derecha.
    [[1, 2, 3],           [[1, 8, 3],
     [4, 5, 6],    ==>     [4, 2, 6],
     [7, 8, 9]]            [7, 5, 9]]

    PRECONDICIONES:
        - `tablero` es una lista de lista de enteros de cualquier dimensión.

    POSTCONDICIONES:
        - Si `columna` es un índice de columnas válido, la función realiza la
        rotación modificando el tablero y devuelve `True`.
        Caso contrario, no modifica el tablero y devuelve `False`."""
    if columna>(len(tablero[0])-1) or columna<0:
        return False
    aux = tablero[-1][columna]
    for numero in range(len(tablero)-1):
        tablero[-numero-1][columna] = tablero[-numero-2][columna]
    tablero[0][columna] = aux
    return True


def esta_ordenado(tablero: list[list[int]]) -> bool:
    """
    Indica si los elementos del tablero se encuentran ordenados de izquierda a
    derecha, arriba a abajo, con el primer elemento siendo un 1 y cada elemento
    subsecuente incrementando su valor por uno.
    Por ejemplo, todo tablero que devuelva `crear_tablero` empieza ordenado.

    PRECONDICIONES:
        - `tablero` es una lista de lista de enteros de cualquier dimensión.
        - Los elementos de `tablero` no tienen números repetidos.
    """
    filas = len(tablero)
    columnas = len(tablero[0])
    return tablero == crear_tablero(filas, columnas)


def mezclar_tablero(tablero: list[list[int]]):
    """
    Realiza ITERACIONES_RANDOM movimientos aleatorios al juego, siendo un
    movimiento cualquiera de las cuatro rotaciones sobre cualquier índice
    respectivo.

    PRECONDICIONES:
        - `tablero` es una lista de lista de enteros de cualquier dimensión.
    """
    filas = len(tablero)
    columnas = len(tablero[0])
    z = 100
    for i in range(z):
        eleccion = random.choice([rotar_abajo, rotar_arriba, rotar_derecha, rotar_izquierda])
        if eleccion == rotar_abajo or eleccion == rotar_arriba:
            eleccion(tablero, random.randint(0, columnas-1))
        else:
            eleccion(tablero, random.randint(0, filas-1))


def mostrar_por_pantalla(tablero: list[list[int]]):
    """
    Muestra por pantalla de manera estética el tablero para
    el usuario.

    PRECONDICIONES:
        - `tablero` es una lista de lista de enteros de cualquier dimensión.
    """
    print("    |", end="")
    for c in range(len(tablero[0])):
            print(f"{c:<2}", end=" ")
    print("\n")
    print("----+" + "---" * len(tablero[0]))
    for i, fila in enumerate(tablero):
        print(f"{i:<2}", end="  |")
        for valor in fila:
            print (f"{valor:<2}", end=" ")
        print("\n")