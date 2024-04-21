import sixteen

def solicitar_dimension(filas_columnas: str) -> int:
    """
    Valida la entrada de las filas o columnas, pasando por todos los casos posibles de
    ingresos erróneos por parte del usuario.

    PRECONDICIONES:
        - `filas_columnas` es un string que indica al usuario si debe ingresar filas o
        columnas.
    
    POSTCONDICIONES:
        - La función devuelve `tira_entero`, que es el número validado ingresado por el
        usuario como entero.
    """
    while True:
        tira = input(f"Ingrese la cantidad de {filas_columnas} del juego: ")
        if tira.isdigit(): 
            tira_entero = int(tira)
            if 1 < tira_entero < 10:
                break
            else:
                print("El número ingresado no está entre 1 y 10")
                continue
        print("No ingresó un número entero")
        continue
    return tira_entero 

def precondiciones() -> list[list[int]]:
    """
    Predispone el entorno de juego: solicita número de filas y columnas; crea el tablero;
    verifica que no esté ordenado y lo muestra por pantalla.
    
    POSTCONDICIONES:
        - La función devuelve el tablero creado como una lista de lista de enteros.
    """
    filas = solicitar_dimension("filas")
    columnas = solicitar_dimension("columnas")
    tablero = sixteen.crear_tablero(filas, columnas)     
    print("\nSIXTEEN\n")
    while sixteen.esta_ordenado(tablero): 
        sixteen.mezclar_tablero(tablero)
    sixteen.mostrar_por_pantalla(tablero)
    return tablero

def solicitar_entrada(tablero: list[list[int]]) -> list[int, str]: #Salvo que el usuario quiera salir, en ese caso devuelve lista vacia
    """
    Valida todos los casos posibles de entrada como movimiento por el usuario hasta que ingrese: una
    rotación aceptada ("n, mov"), o "q" para salir, o "m" para mezclar el tablero. Estos dos últimos 
    casos cuentan con una reconfirmación en caso de que haya apretado por error la tecla.

    PRECONDICIONES:
        - `tablero` es una lista de lista de enteros de cualquier dimensión.
    
    POSTCONDICIONES:
        - En caso de que el usuario quiera abandonar el juego, la función devuelve una lista vacia.
        Caso contrario, devuelve una lista de dos elementos: un entero en la posicion [0] y un string
        en la posición [1]. El string debe ser uno de los `posibles_movimientos` y el entero debe
        concordar con la fila/columna asignada al movimiento.
    """
    while True:
        entrada = input("\nq para salir; m para mezclar \nMovimientos: w(arriba); s(abajo); a(izquierda); d(derecha) \nIngrese --> n, mov: ")
        partes = entrada.split(",")
        movimiento = []
        posibles_movimientos = ["w", "s", "a", "d"]
        if len(partes) == 2 and partes[0].isdigit() and ((partes[1] in posibles_movimientos[0:2] and int(partes[0]) < len(tablero[0])) or (partes[1] in posibles_movimientos[2:] and int(partes[0]) < len(tablero))):
            movimiento.append(int(partes[0]))
            movimiento.append(partes[1])
            break
        elif entrada == "q": #Opción de salida
            confirmacion = input("Estas seguro de que queres abandonar? [S/n]: ")
            if confirmacion == "S":
                break
        elif entrada == "m": #Opción de mezclar tablero
            confirmacion = input("A continuación se mezclará el tablero, deseas continuar? [S/n]: ")
            if confirmacion == "S":
                sixteen.mezclar_tablero(tablero)
                sixteen.mostrar_por_pantalla(tablero)
        else:
            print("\nNo ingresó una opción válida, compruebe la existencia de la fila/columna o el movimiento")
    return movimiento

def aplicar_rotaciones(tablero: list[list[int]], movimiento: list[int, str], contador_movimientos: int) -> int:
    """
    Realiza los movimientos respectivos al tablero, aumenta en una unidad el contador de movimientos
    y muestra por pantalla el tablero luego de aplicarle el movimiento.

    PRECONDICIONES:
        - `tablero` es una lista de lista de enteros de cualquier dimensión; `movimiento` es una lista
        de dos elementos, el primero un entero y el segundo un string ambos deben ser validados previamente;
        `contador_movimientos` es un entero.
    
    POSTCONDICIONES:
        - La función devuelve la variable `contador_movimientos`, que es un entero, incrementada en una unidad
    """
    if movimiento[1] == "w":
        sixteen.rotar_arriba(tablero, movimiento[0])
        contador_movimientos += 1
        sixteen.mostrar_por_pantalla(tablero)
    elif movimiento[1] == "s":
        sixteen.rotar_abajo(tablero, movimiento[0])
        contador_movimientos += 1
        sixteen.mostrar_por_pantalla(tablero)
    elif movimiento[1] == "a":
        sixteen.rotar_izquierda(tablero, movimiento[0])
        contador_movimientos += 1
        sixteen.mostrar_por_pantalla(tablero)
    elif movimiento[1] == "d":
        sixteen.rotar_derecha(tablero, movimiento[0])
        contador_movimientos += 1
        sixteen.mostrar_por_pantalla(tablero)
    return contador_movimientos


def main():
    tablero = precondiciones()    
    contador_movimientos = 0
    while True:
        if sixteen.esta_ordenado(tablero):
            break
        movimiento = solicitar_entrada(tablero)
        if movimiento == []:
            return
        contador_movimientos = aplicar_rotaciones(tablero, movimiento, contador_movimientos)
    print(f"\nFELICITACIONES, GANASTE!!!\nMovimientos: {contador_movimientos}")
    sixteen.mostrar_por_pantalla(tablero)
main()