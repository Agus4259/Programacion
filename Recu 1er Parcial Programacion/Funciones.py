#Arrays bidimensionales/matrices


def mostrar_matriz(matriz : list):

    if type(matriz) != list:
        print("Error, debe ser tipo lista")
        return None
    #accede a filas
    for fil in range(len(matriz)):
        #acede a columnas
        for col in range(len(matriz[fil])):
            print((matriz[fil][col]), end = " ")
        
        print("")

def crear_matriz(cant_filas : int, cant_columnas : int, valor_inicial : any) -> list: #inicializar matriz
    """crea una matriz nueva

    Args:
        cant_filas (int):cantidad de filas
        cant_columnas (int):cantidad de columnas
        valor_inicial (any): valor/tipo de los elementos en las columnas

    Returns:
        list: matriz
    """
    matriz= []
    for _ in range(cant_filas):
        fila = [valor_inicial] * cant_columnas

        matriz += [fila]

    return matriz


def cargar_matriz_sec(matriz : list):
    for fil in range(len(matriz)):
        for col in range(len(matriz[fil])):
            matriz[fil][col] = int(input(f"Ingrese un numero para fila {fil}  y un numero para columna {col}: "))
    
    return matriz




#matriz_nueva = mostrar_matriz(matriz_numerica)




#arrays unidimencionales

def crear_array(valor, cant_elementos):
    """crea un array/lista

    Args:
        valor (_list_): tipo de elementos en la lista
        cant_elementos (_type_): cantidad de elementos en la lista

    Returns:
        _list_: lista nueva con el valor y cantidad de elementos que se quizo
    """
    array = [valor] * cant_elementos
    return array



    

def cargar_nombre_part(lista : list) -> list:
    """recorre una lista/matriz de elementos de tipo str y va modificando sus elementos

    Args:
        lista (list): lista/matriz de elementos de tipo str
    
    Returns:
        _list_: lista/matriz con nombres
    """
    for i in range(len(lista)):
        nombre = input("Ingrese un nombre: ")
        while type(nombre) != str:
            nombre = input("Error 1, el nombre debe de tener mas de 3 caracteres(letras),ingrese un nombre: ")
            #while len(nombre) < 3:
            #nombre = input("Error 2, el nombre debe de tener mas de 3 caracteres(letras),ingrese un nombre: ")
        
        lista[i] = nombre

    return lista


""""

for fil in range(len(matriz)):
        for col in range(len(matriz[fil])):
            matriz[0][col] = int(input(f"Ingrese  un numero para columna {col}: "))
"""

def cargar_nota_jurado2(matriz : list) ->list:
    """_summary_

    Args:
        matriz (list): _description_
    """

    numero = int(input(f"De quien es la nota que desea cargar del jurado 1?\n0(1er participante)\n1(2do participante)\n2(3erparticipante)\n3(4to participante)\n4(5to participante)5(6to participante)\n: "))
    matriz[2] [numero] = int(input(f"Ingrese  un numero entre el 1 y el 10: "))
    while matriz[2] [numero] > 10  or  matriz[2] [numero] < 1:
        matriz[2] [numero] = int(input(f"Error, la nota tiene que ser un numero entre el 1 y el 10, ingrese  un numero: "))
    return matriz





#matriz_nombre = ["Tomas","Agustin"]
#matriz = [[1,0],[1,0],[1,0]]


def validar_lista(matriz:list):
    if type(matriz) != list:
        print("Error, debe ser tipo lista")
        return None


   
#num = "a"
#print(f"num vale {num}")
#num_int = 1
#print(f"num_int vale {num_int}")
#num  = num_int
#print(f"num vale {num}")

def cargar_nota_jurado(matriz : list) -> list:
    """recorre una lista/matriz y va modificando sus elementos

    Args:
        matriz (list): lista/matriz

    Returns:
        list:Cada puntaje que dio e cada jurado a cada participante
    """
    validar_lista(matriz)
    
    for fil in range(len(matriz)):
        for col in range(len(matriz[0])):
            nota = int(input(f"Cargar nota del jurado {fil +1} del participante {col + 1} entre el 1 y el 10: "))
            
            while type(nota) == int and nota > 10  or  nota < 1:
                nota = int(input(f"Error,cargar nota de participante {fil +1} del jurado {col + 1} entre el 1 y el 10: "))
            matriz [fil] [col] = nota
    print("")

  

  


def print_puntaje_jurado(matriz : list):
    """Muestra puntaje que dio cada jurado

    Args:
        matriz (list): lista donde se cargo los puntajes de cada jurado
    Returns: Print con los puntajes de cada jurado a cada participante
    """
    for fil in range(len(matriz)):
            for col in range(len(matriz[0])):
                print("")
                print(f"Puntaje {col + 1} del Jurado {fil + 1}:  {matriz[fil][col]}")
                print("")

#matriz[fil]

def mostrar_puntaje(array_nombre:list,array_notas_jurado:list,indice_part) -> list:
    """recore la lista de nombres y de puntajes  y para mostrar el participánte y las notas que le puso cada jurado

    Args:
        array_nombre (list): lista con nombres
        matriz_notas (list): lista/matiz con las notas que le asigno cada jurado a cada participante
        indice_part (_type_): dato int para ubicar en la lista  a cual participante se mostrara su puntaje

    Returns:
        list:muestra el puntaje del  participante y de los  jurados que le pusieron su puntaje junto al puntaje que le puso cada respectivo jurado
    """
    if type(array_nombre) != list:
        print("Error, debe ser tipo lista")
        return None
    
    if type(array_notas_jurado) != list:
        print("Error, debe ser tipo lista")
        return None
    
    for fil in range(len(array_notas_jurado[0])):
            print(f"Nombre: {array_nombre[fil]}")
            print(f"Puntaje  del Jurado {fil + 1}:  {array_notas_jurado  [indice_part][fil]}")

def mostrar_puntaje_todos(array_nombre : list, array_notas_jurado : list) -> list:
    """recore la lista de nombres y de puntajes  y las va mostrando acorde al participánte y jurado que le correspnda

    Args:
        array_nombre (list): lista con nombres
        matriz_notas (list): lista/matiz con las notas que le asigno cada jurado a cada participante

    Returns:
        _type_: muestra el puntaje de todos los participantes y de cual jurado le puso su puntaje
    """
    if type(array_nombre) != list:
        print("Error, debe ser tipo lista")
        return None
    
    if type(array_notas_jurado) != list:
        print("Error, debe ser tipo lista")
        return None

    for i in range(len(array_nombre)):
        print(f"Nombre: {array_nombre[i]}")
        mostrar_puntaje(array_nombre,array_notas_jurado,i)
        print("")

#matriz_nota = [[1,2],[3,4]]
#array_nombre = ["tomas","agus"]
#mostrar_puntaje_todos(array_nombre,matriz_nota)


def calcular_promedio(acumulador : int, contador : int):
    """calcula promedio

    Args:
        acumulador (int): suma de elementos
        contador (int): cantidad de elementos sumados

    Returns:
        _type_: dato float/int
    """
    if contador != 0:
        promedio = acumulador / contador
    else:
        promedio = None
    
    return promedio

def suma_elementos_matriz(matriz : int):
    suma = 0
    """suma los elementos de una matriz

    Args:
        matriz (int): elementos de tipo int o float
     Returns:
        _type_: dato int
    """
    for fil in range(len(matriz)):
        for col in range(len(matriz[fil])):
            if type(matriz[fil] [col]) == int or type(matriz[fil] [col]) == float:
                suma += matriz[fil] [col]
    
    return suma

def sumar_fila(matriz_num : list, indice_fila : int):
    """suma los elementos de una fila en una matriz

    Args:
        matriz_num (lista): lista/matriz con numeros
        indice_fila (int): indice de  la fila de los elementos de esta que se quieren sumar
    Returns:
        _type_: dato int
    """
    suma_fila = 0
    for col in range(len(matriz_num[0])):
        if type(matriz_num[indice_fila] [col]) == int or type(matriz_num[indice_fila] [col]) ==   float:
            suma_fila += matriz_num[indice_fila] [col]

    return suma_fila

#
#mostrar_matriz(matriz_nombre)
#mostrar_matriz(matriz)

#array_nombre = ["Tomas","Agus","Bian"]
array_notas_jurados = [[1,1,1],[2,2,2],[5,5,5]]

def part_promedio (array_nombre : list, matriz_notas : list, promedio : int):
    """da el nombre y el promedio de los puntajes de los participantes que superen cierto valor que se determina

    Args:
        array_nombre (list): lista con nombres
        matriz_notas (list): lista/matiz con las notas que le asigno cada jurado a cada participante
        promedio (int): valor con el que se compara para ver si el promedio supero este valor o no
    Returns:
        _type_: da el nombre y el promedio de los puntajes de los participantes que superen cierto valor que se determina
    """
    promedio_bandera = False
    for fil in range(len(matriz_notas)):  
        nota_1 = matriz_notas [0] [fil]
        nota_2 = matriz_notas [1] [fil]
        nota_3 = matriz_notas [2] [fil]
        suma_notas = nota_1 + nota_2 + nota_3 
        promedio_notas = calcular_promedio(suma_notas,3)
        contador_promedio += promedio_notas 

        if promedio_notas > promedio:
            promedio_bandera = True
            print(array_nombre[fil])
            print("")
            print(f"El promedio de los puntajes es {promedio_notas}")
            print("")   
        else:
            continue
    
    if promedio_bandera != True:
        print(f"Noy hay ningun participante que supere el promedio de {promedio}")
    else:
        print(f"Tarea finalizada")
    
    
    
    
    
    
    
#part_promedio(array_nombre,array_notas_jurados,4)
    
 
def jurado_promedio(matriz_notas : list):
    """da el promedio de los puntos que asigno cada jurado

    Args:
        matriz_notas (list): lista/matriz con las notas que asingo cada jurado
    Returns:
        _type_: da el promedio de los puntos que asigno cada jurado
    """
    for fil in range(len(matriz_notas)):  
        suma_notas = sumar_fila(matriz_notas,fil)
        promedio_notas = calcular_promedio(suma_notas,3)
        print(f"Promedio de puntajes del Jurado {fil + 1}:  {promedio_notas}")

def buscar_min_array (array : list):
    """busca el dato mas chico de una lista

    Args:
        array (list): lista con datos int/float

    Returns:
        _type_: indice en caso de una lista o el dato de ese indice en caso de ser usada en una matriz
    """
    indice = None
    bandera = False

    for  i in range(len(array)):
        if bandera == False:
            minimo  = array[i]
            indice = i
            bandera = True
        else:
            if array[i] < minimo:
                minimo = array[i]
                indice = i

    return indice

    





def jurado_estricto (matriz_nota_jurado : list):
    """dice el jurado que a calificado con menor puntaje demostrado segun su promedio de puntaje asignados

    Args:
        matriz_nota_jurado (list): lista/matriz con los puntajes de cada jurado
    Returns:
        _type_: jurado mas estricto con su promedio de puntaje asignados y los puntajes que dio
    """
    for i in range(len(matriz_nota_jurado)):
        suma_notas_fila_1 = sumar_fila(matriz_nota_jurado,i - i )
        suma_notas_fila_2 = sumar_fila(matriz_nota_jurado,i - 1)
        suma_notas_fila_3 = sumar_fila(matriz_nota_jurado,i)
    promedio_notas_fila_1 = calcular_promedio(suma_notas_fila_1,3)
    promedio_notas_fila_2 = calcular_promedio(suma_notas_fila_2,3)
    promedio_notas_fila_3 = calcular_promedio(suma_notas_fila_3,3)
    promedio_jurados = [promedio_notas_fila_1,promedio_notas_fila_2,promedio_notas_fila_3]
    indice = buscar_min_array(matriz_nota_jurado)
    print(f"El jurado {indice + 1} es el mas estricto con promedio de {promedio_jurados[indice]}")

def buscar_participante (array_nombre : list , array_notas_jurados : list):
    """busca participantes y muestra sus datos

    Args:
        array_nombre (list): lista con nombres/datos str
        array_notas_jurados (list): lista con puntajes/datos int
    Returns:
        _type_: nombre del participante con sus puntajes y promedio de puntajes
    """
    buscar_nombre = input("Ingrese nombre del participante que desea buscar: ")
    for j in range(len(array_nombre)):
        if buscar_nombre == array_nombre[j]:
            buscar_nombre = array_nombre[j]
            print(f"Se encontro a {buscar_nombre}")
            print("")
            for i in range(len(array_notas_jurados)):
                indice = j
        
                print(f"Puntaje del Jurado {i +1}: {array_notas_jurados [i][indice]} ")
        else:
            continue
       

#len(array_notas_jurados[jurado])
#array_notas_jurados[jurado]
#jurado_estricto(array_notas_jurados)

def mostrar_puntaje_part (array_nombres : list, array_jurado_puntajes : list):
    """muestra los nombres y puntajes de cada participante

    Args:
        array_nombres (list): lista de nombres
        array_jurado_puntajes (list): matriz de los puntajes de los jurados
    Returns: nombre y puntaje de cada participante
    """
    for j in range(len(array_nombres)):
        print("")
        print(f"nombre: {array_nombres[j]}")
        print("")
        for i in range(len(array_jurado_puntajes)):    
            indice = j
        
            print(f"Puntaje del Jurado {i +1}: {array_jurado_puntajes [i][indice]} ")
    print("")


def promedio_general_puntajes (matriz_nota : list, matriz_nombre : list):
    """saca el promedio general del puntaje de todos los participantes

    Args:
        matriz_nota (list): matriz con puntajes
        matriz_nombre (list): lista de nombres

    Returns: numero del promedio general
    """
    total = len(matriz_nombre)
    for i in range(len(matriz_nota)):
        suma_notas_fila_1 = sumar_fila(matriz_nota,i - i )
        
        suma_notas_fila_2 = sumar_fila(matriz_nota,i - 1)
        
        suma_notas_fila_3 = sumar_fila(matriz_nota,i)
        
    total_puntaje = suma_notas_fila_1 + suma_notas_fila_2 + suma_notas_fila_3
    promedio_puntajes_gen = calcular_promedio(total_puntaje,total)
    return promedio_puntajes_gen


#array_notas_jurados = [[1,1,1],[15,15,15],[4,4,4]]

#print(promedio_general_puntajes(array_notas_jurados,array_nombre ))





#print(ord("Tomas"[0]) < ord("Agus"[0]))
array_nombre = ["tomas","agus","bian","kari","ajus"]

#for  i in range(len(array_nombre)):
    #primero = " "
    #segundo = " "
    #tercero = " "
    #cuarto = " "
    #quinto = " "
   
    #bandera = False
    #if ord(mid[0]) < ord(minimo[0]) and ord(mid[0]) < ord(max[0]):
        #primero = mid
    #elif ord(mid[0]) < ord(minimo[0]) or ord(mid[0]) < ord(max[0]):
        #segundo = mid
    #else:
        #tercero = mid
        
    
    #if ord(minimo[0]) < ord(mid[0]) and ord(minimo[0]) < ord(max[0]):
        #primero = minimo
    #if ord(minimo[0]) < ord(mid[0]) or ord(minimo[0]) < ord(max[0]):
        #segundo = minimo
    #else:
        #tercero = minimo
           
    
    #if ord(max[0]) < ord(minimo[0]) and ord(max[0]) < ord(mid[0]):
        #primero = max
    #elif ord(max[0]) < ord(minimo[0]) or ord(max[0]) < ord(mid[0]):
        #segundo = max
    #else:
        #tercero = max

def buscar_participante_2 (array_nombre : list, nombre_buscado : str , array_notas_jurados : list):
    """busca participantes y muestra sus datos

    Args:
        array_nombre (list): lista con nombres/datos str
        array_notas_jurados (list): lista con puntajes/datos int
    Returns:
        _type_: nombre del participante con sus puntajes y promedio de puntajes
    """
    
    for j in range(len(array_nombre)):
        if nombre_buscado == array_nombre[j]:
            buscar_nombre = array_nombre[j]
            print(f"{buscar_nombre}")
            print("")
            for i in range(len(array_notas_jurados)):
                contador_promedio  = 0
                nota_1 = array_notas_jurados [0] [j]
                nota_2 = array_notas_jurados [1] [j]
                nota_3 = array_notas_jurados [2] [j]
                suma_notas = nota_1 + nota_2 + nota_3 
                promedio_notas = calcular_promedio(suma_notas,3)
                contador_promedio += promedio_notas 
                indice = j
        
                print(f"Puntaje del Jurado {i +1}: {array_notas_jurados [i][indice]} ")
            print(f"Promedio de puntaje: {promedio_notas}")
        else:
            continue            
    
#print(f"{primero}, {segundo}, {tercero}")
lista = [ ] 
lista_2 = [ ]  
#for i in range(len(array_nombre)):
    #comp = array_nombre[i]   
    #if ord(array_nombre[i][0]) >= ord(comp[0]):
        #minimo = array_nombre[i]
        #print(array_nombre[i])
    #elif ord(array_nombre[i][0]) > ord(comp[0]) and ord(array_nombre[i][0]) < ord(comp[0]) :
        #print(array_nombre[i])
array_nombre = ["tomas","agus","bian","kari","fabi"]
array_notas_jurados = [[1,2,3,4,5],[15,16,17,18,19],[5,6,7,8,9]]
def ordenar_alfabeticamente(lista : list)->list:
    """Ordena los nombres de la a la z comparando su valor ascii

    Args:
        lista (list): lista de nombres

    Returns:
        list: lista ordenada alfabeticamente
    """
    if type(lista) != list:
        print("Debe ser una lista")
        return None
    
    menores_ord = []
    iguales_ord = []
    mayores_ord = []
    if len(lista) > 1:

        pivote = lista[0]

        for i in range(len(lista)):
            lista_nueva = [lista[i]]
            if ord(lista[i][0]) < ord(pivote[0]):
                menores_ord += lista_nueva
            elif ord(lista[i][0]) == ord(pivote[0]):
                iguales_ord += lista_nueva
            else:
                mayores_ord += lista_nueva

        return ordenar_alfabeticamente(menores_ord) + iguales_ord + ordenar_alfabeticamente(mayores_ord)
    else:
        return lista





#for i in range(len(nueva_lista)):
    #print(nueva_lista[i])

def mostrar_nombres_alfabeticamente(array_nombre : list, matriz_jurado : list):
    """muestra los participantes y sus datos en orden alfabetico

    Args:
        array_nombre (list): lista de nombres
        matriz_jurado (list): lista de los puntajes de los jurados asignados a cada participante
    Returns: nombre, puntaje y promedio de puntaje de cada participante en orden alfabetico
    """
    nueva_lista = ordenar_alfabeticamente(array_nombre)
    for i in range(len(array_nombre)):
        buscar_participante_2(array_nombre,nueva_lista[i],matriz_jurado)
        print("")
        
#mostrar_nombres_alfabeticamente(array_nombre, array_notas_jurados)

nombre_buscado = 0
""""
for j in range(len(array_nombre)):
    if nombre_buscado == array_nombre[j]:
        buscar_nombre = array_nombre[j]
        print(f"{buscar_nombre}")
        print("")
        for i in range(len(array_notas_jurados)):
            contador_promedio  = 0
            nota_1 = array_notas_jurados [0] [j]
            nota_2 = array_notas_jurados [1] [j]
            nota_3 = array_notas_jurados [2] [j]
            suma_notas = nota_1 + nota_2 + nota_3 
            promedio_notas = calcular_promedio(suma_notas,3)
            contador_promedio += promedio_notas 
            indice = j

"""

def almacenar_promedio_punt_part(array_nombre : list, array_notas_jurados : list):
    """calcula y guarda promedio de puntajes de cada paricipante en una lista

    Args:
        array_nombre (list): lista de nombres de los participantes
        array_notas_jurados (list): lista de los jurados hacia cada participante

    Returns:
        _type_: _lista de promedio de puntajes de cada participante
    """
    lista_promedio_puntajes = crear_array(1,5)
    for j in range(len(array_nombre)):
        for i in range(len(array_notas_jurados)):
            nota_1 = array_notas_jurados [0] [j]
            nota_2 = array_notas_jurados [1] [j]
            nota_3 = array_notas_jurados [2] [j]
            suma_notas = nota_1 + nota_2 + nota_3 
            promedio_notas = calcular_promedio(suma_notas,3)
            
            lista_promedio_puntajes[j] = promedio_notas

    return lista_promedio_puntajes


lista_puntajes = almacenar_promedio_punt_part(array_nombre,array_notas_jurados)




def ordenar_puntajes(lista : list)->list:
    """Ordena promedios de participantes de mayor a menor

    Args:
        lista (list): lista de promedio de puntajes de cada participante

    Returns:
        list: lista ordenada de mayor a menor
    """
    if type(lista) != list:
        print("Debe ser una lista")
        return None
    
    menores_ord = []
    iguales_ord = []
    mayores_ord = []
    if len(lista) > 1:

        pivote = lista[0]

        for i in range(len(lista)):
            lista_nueva = [lista[i]]
            if lista[i] < pivote:
                menores_ord += lista_nueva
            elif lista[i] == pivote:
                iguales_ord += lista_nueva
            else:
                mayores_ord += lista_nueva
        
        return ordenar_puntajes(mayores_ord) + iguales_ord + ordenar_puntajes (menores_ord)
    else:
        return lista

mayores = ordenar_puntajes(lista_puntajes)
print(ordenar_puntajes(lista_puntajes))
def buscar_participante_3 (array_nombre : list, mayores : list, lista_puntajes : list):
    """busca promedio de puntaje y muestra de quien es

    Args:
        array_nombre (list): lista con nombres/datos str
        mayores(list): lista ordenada de mayor a menor de promedio de puntajes de cada párticipante
    Returns:
        _type_: muestra nombre y su promedio de puntaje del participante con mayor nota
    """
    
    
    for j in range(len(lista_puntajes)):
        if mayores == lista_puntajes[j]:
            mayores  = lista_puntajes[j]
            print(f"{array_nombre[j]}\nPromedio puntaje: {lista_puntajes[j]}")
            print("")
        elif j != 2:
            continue
            


def mostrar_part_mayor_prom(array_nombre : list, array_notas_jurados : list):
    """muestra a los 3 participantes con mayor promedio de puntajes y sus nombres

    Args:
        array_nombre (list): lista de nombres de los participantes
        array_notas_jurados (list): lista de los jurados hacia cada participante
    Returns: print de los nombres y promedio de puntajes de los 3 participantes con mayor promedio
    """
    lista_puntajes = almacenar_promedio_punt_part(array_nombre,array_notas_jurados)
    mayores = ordenar_puntajes(lista_puntajes)
    
    print("Participantes con mayor promedio de puntajes son:")          
    
    for i in range(len(mayores)):
        if i != 3:
            buscar_participante_3(array_nombre,mayores[i],lista_puntajes)
        else:
            break
    
mostrar_part_mayor_prom(array_nombre,array_notas_jurados)