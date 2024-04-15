import sixteen

def main():
    while True: #Ciclo while que valida la entrada de número de filas
        filas = input("Ingrese la cantidad de filas(alto) del juego: ")
        if filas.isdigit(): 
            filas_entero=int(filas)
            if 1<filas_entero<10:
                break
            else:
                print("El número ingresado no está entre 1 y 10")
                continue
        print("No ingresó un número entero")
        continue
    
    while True: #Ciclo while que valida la entrada de número de columnas
        columnas = input("Ingrese la cantidad de columnas(ancho) del juego: ")
        if columnas.isdigit(): 
            columnas_entero=int(columnas)
            if 1<columnas_entero<10: 
                break
            else:
                print("El número ingresado no está entre 1 y 10")
                continue
        print("No ingresó un número entero")
        continue
    
    tablero=sixteen.crear_tablero(filas_entero, columnas_entero) #Se crea el tablero ordenado
    
    print("\nSIXTEEN\n")

    while sixteen.esta_ordenado(tablero)==True: #Mezcla el tablero ordenado hasta que ya no lo esté
        sixteen.mezclar_tablero(tablero)
    
    sixteen.mostrar_por_pantalla(tablero) #Se muestra el tablero mezclado
    
    contador_movimientos=0 #Contador de movimientos que se muestra cuando el usuario gana el juego
    
    while True: #Ciclo while para contemplar todas las situaciones de juego
        if sixteen.esta_ordenado(tablero)==True: #Verifica que haya ganador después de cada movimiento
            print(f"\nFELICITACIONES, GANASTE!!!\n Movimientos: {contador_movimientos}")
            sixteen.mostrar_por_pantalla(tablero)
            break
        entrada=input("\nq para salir; m para mezclar \nMovimientos: w(arriba); s(abajo); a(izquierda); d(derecha) \nIngrese --> n, mov: ")
        partes=entrada.split(",")
        movimiento=[]
        if len(partes) == 2 and partes[0].isdigit(): #Condicional para validar la entrada de la fila/columna y movimiento
            movimiento.append(int(partes[0]))
            movimiento.append(partes[1])
        elif entrada == "q": #Opción de salida
            confirmacion = input("Estas seguro de que queres abandonar? [S/n]: ")
            if confirmacion == "S":
                break
            continue
        elif entrada == "m": #Opción de mezclar tablero
            confirmacion = input("A continuación se mezclará el tablero, deseas continuar? [S/n]: ")
            if confirmacion == "S":
                sixteen.mezclar_tablero(tablero)
                sixteen.mostrar_por_pantalla(tablero)
            continue         
        else: 
            print("\nNo ingresó una opción válida, compruebe la existencia de la fila/columna o el movimiento")
            continue
        
        if movimiento[1] == "w": #Se interpretan los distintos movimientos, si no concuerdan las letras vuelve al comienzo del while
            sixteen.rotar_arriba(tablero, movimiento[0])
            contador_movimientos+=1
            sixteen.mostrar_por_pantalla(tablero)
        elif movimiento[1] == "s":
            sixteen.rotar_abajo(tablero, movimiento[0])
            contador_movimientos+=1
            sixteen.mostrar_por_pantalla(tablero)
        elif movimiento[1] == "a":
            sixteen.rotar_izquierda(tablero, movimiento[0])
            contador_movimientos+=1
            sixteen.mostrar_por_pantalla(tablero)
        elif movimiento[1] == "d":
            sixteen.rotar_derecha(tablero, movimiento[0])
            contador_movimientos+=1
            sixteen.mostrar_por_pantalla(tablero)

main()