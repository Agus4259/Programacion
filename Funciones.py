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


def carga_aleatoria(matriz : list):
    seguir = "s"
    while seguir == "s":
        fila =  int(input(" Ingrese una fila: "))
        columna =  int(input(" Ingrese una columna: "))
        numero =  int(input(" Ingrese una numero: "))
        matriz[fila][columna] = numero
        
        seguir = input("Queire seguir ingresando? s/n")
        if seguir != "s":
            break
    
    return matriz

#matriz_nueva = mostrar_matriz(matriz_numerica)

def buscar_matriz(matriz : list, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                print(f"{valor} se encontro en fila {i} y en columna {j}")


def suma_matrices(matriz_1 : list, matriz_2 : list):
    matriz_resp = []
    if len(matriz_1[i]) != len(matriz_2[i]):
            print("Error, deben de tener mismo orden y tamaño")
            return None
    
    matriz_resp = crear_matriz(len(matriz_1), len(matriz_2[0]),len(matriz_1))

    for i in range(len(matriz_1)):
        for j in range(len(matriz_1)[i]):
            matriz_resp[i][j] = matriz_1[i][j] +  matriz_2 [i][j]

#arrays unidimencionales

def modificar_pares(array_num:list):
    """_summary_

    Args:
        array_num (list): _description_
    """
    for i in range(len(array_num)):
        if array_num[i] % 2 == 0:
            array_num[i] = array_num[i] * 10
    #no tiene sentido retornar una lista porque las listas son mutables, adentro y afuera de la funcion
    return array_num

def crear_array(valor,cant_elementos):
    """crea un array/lista

    Args:
        valor (_list_): tipo de elementos en la lista
        cant_elementos (_type_): cantidad de elementos en la lista

    Returns:
        _list_: lista nueva con el valor y cantidad de elementos que se quizo
    """
    array = [valor] * cant_elementos
    return array



    

def cargar_nombre_part(lista:list) -> list:
    """carga los nombres de cada participante

    Args:
        lista (list): lista con nombres
    
    Returns:
        _list_: lista con nombres
    """
    for i in range(len(lista)):
        nombre = input("Ingrese un nombre: ")
        while len(nombre) < 3 and nombre != str :
             nombre = input("Error, el nombre debe de tener mas de 3 caracteres(letras),ingrese un nombre: ")
        lista[i] = nombre

    return lista


""""

for fil in range(len(matriz)):
        for col in range(len(matriz[fil])):
            matriz[0][col] = int(input(f"Ingrese  un numero para columna {col}: "))
"""

def cargar_nota_jurado2(matriz:list) ->list:
    """_summary_

    Args:
        matriz (list): _description_
    """

    numero = int(input(f"De quien es la nota que desea cargar del jurado 1?\n0(1er participante)\n1(2do participante)\n2(3erparticipante)\n3(4to participante)\n4(5to participante)5(6to participante)\n: "))
    matriz[2] [numero] = int(input(f"Ingrese  un numero entre el 1 y el 10: "))
    while matriz[2] [numero] > 10  or  matriz[2] [numero] < 1:
        matriz[2] [numero] = int(input(f"Error, la nota tiene que ser un numero entre el 1 y el 10, ingrese  un numero: "))
    return matriz





matriz_nombre = ["Tomas","Agustin"]
matriz = [[1,0],[1,0],[1,0]]





def cargar_nota_jurado(matriz:list) -> list:
    """carga nota de cada jurado a cada participante

    Args:
        matriz (list): lista/matriz

    Returns:
        list: matriz con los puntajes de cada jurado a cada participante
    """
    if type(matriz) != list:
        print("Error, debe ser tipo lista")
        return None
    
    for fil in range(len(matriz)):
        for col in range(len(matriz[0])):
            nota = int(input(f"Cargar nota del jurado {fil +1} del participante {col + 1} entre el 1 y el 10: "))
            while nota > 10  or  nota < 1:
                nota = int(input(f"Error,cargar nota de participante {fil +1} del jurado {col + 1} entre el 1 y el 10: "))
            matriz [fil] [col] = nota

    return matriz


def mostrar_puntaje(array_nombre:list,array_notas_jurado:list,indice_part:int) -> list:
    """_summary_

    Args:
        array_nombre (list): _description_
        array_notas_jurado (list): _description_
        indice_part (_type_): _description_

    Returns:
        list: _description_
    """
    if type(array_nombre) != list:
        print("Error, debe ser tipo lista")
        return None
    
    if type(array_notas_jurado) != list:
        print("Error, debe ser tipo lista")
        return None
    
   
    if type(indice_part) != int:
        print("Error, debe ser tipo int")
        return None

    print(f"Nombre: {array_nombre[indice_part]}")
    for i in range(len(array_notas_jurado[0])):
        print(f"Nota de Jurado {i + 1}:  {array_notas_jurado [indice_part] [i] }")

def mostrar_puntaje_todos(array_nombre:list,array_notas_jurado:list) -> list:
    """_summary_

    Args:
        array_nombre (list): _description_
        array_notas_jurado (list): _description_
        indice_part (_type_): _description_

    Returns:
        list: _description_
    """
    if type(array_nombre) != list:
        print("Error, debe ser tipo lista")
        return None
    
    if type(array_notas_jurado) != list:
        print("Error, debe ser tipo lista")
        return None

    for i in range(len(array_nombre)):
        mostrar_puntaje(array_nombre,array_notas_jurado,i)
        print("")

def calcular_promedio(acumulador:int, contador:int):
    """calcula promedio

    Args:
        acumulador (int): suma de elementos
        contador (int): cantidad de elementos sumados

    Returns:
        _type_: int
    """
    if contador != 0:
        promedio = acumulador / contador
    else:
        promedio = None
    
    return promedio

def suma_elementos_matriz(matriz:int):
    suma = 0
    """suma los elementos de una matriz

    Args:
        matriz (int): elementos de tipo int o float
    """
    for fil in range(len(matriz)):
        for col in range(len(matriz[fil])):
            if type(matriz[fil] [col]) == int or type(matriz[fil] [col]) == float:
                suma += matriz[fil] [col]
    
    return suma

def sumar_fila(matriz_num:int, indice_fila):
    """_summary_

    Args:
        matriz_num (int): _description_
    """
    suma_fila = 0
    for col in range(len(matriz_num[0])):
        if type(matriz_num[indice_fila] [col]) == int or type(matriz_num[indice_fila] [col]) ==   float:
            suma_fila += matriz_num[indice_fila] [col]

    return suma_fila

#
#mostrar_matriz(matriz_nombre)
#mostrar_matriz(matriz)

array_nombre = ["Tomas","Agus","Bian"]
array_notas_jurados = [[1,1,1],[15,15,15],[4,4,4]]

#cargar_nombre_part(array_nombre)
#cargar_nota_jurado(array_notas_jurados1)
#mostrar_puntaje(array_nombre,array_notas_jurados,0)
#mostrar_matriz(array_notas_jurados)
#mostrar_matriz(array_notas_jurados1)

#mostrar_puntaje(array_nombre,array_notas_jurados,1)

def part_promedio(array_nombre:list,matriz_notas:list,promedio:float):
    """_summary_

    Args:
        array_nombre (list): _description_
        matriz_notas (list): _description_
        promedio (float): _description_
    """
    for fil in range(len(matriz_notas)):  
        suma_notas = sumar_fila(matriz_notas,fil)
        promedio_notas = calcular_promedio(suma_notas,3)
        
        if promedio_notas > promedio:
            mostrar_puntaje(array_nombre,matriz_notas,fil)
            print(f"El promedio de los puntajes es{promedio_notas}")
            print("")
        else:
            promedio_notas = "Error"
            print(promedio_notas)
    
 
def jurado_promedio(matriz_notas:list):
    """_summary_

    Args:
        matriz_notas (list): _description_
    """
    for fil in range(len(matriz_notas)):  
        suma_notas = sumar_fila(matriz_notas,fil)
        promedio_notas = calcular_promedio(suma_notas,3)
        print(f"Promedio de puntajes del Jurado {fil + 1}:  {promedio_notas}")
    



#jurado_estricto(array_notas_jurados)







    
#print(f"{numero_minimo} {numero_maximo}")

def buscar_min_array(array:list):
    """_summary_

    Args:
        array (list): _description_

    Returns:
        _type_: _description_
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


#jurado_estricto = array_notas_jurados[indice]

def jurado_estricto(matriz_nota_jurado:list):
    suma_notas_fila_1 = sumar_fila(matriz_nota_jurado,0)
    suma_notas_fila_2 = sumar_fila(matriz_nota_jurado,1)
    suma_notas_fila_3 = sumar_fila(matriz_nota_jurado,2)
    promedio_notas_fila_1 = calcular_promedio(suma_notas_fila_1,3)
    promedio_notas_fila_2 = calcular_promedio(suma_notas_fila_2,3)
    promedio_notas_fila_3 = calcular_promedio(suma_notas_fila_3,3)
    promedio_jurados = [promedio_notas_fila_1,promedio_notas_fila_2,promedio_notas_fila_3]
    indice = buscar_min_array(array_notas_jurados)
    print(f"El jurado {indice + 1} es el mas estricto con promedio de {promedio_jurados[indice]} y las notas que asigno fueron {matriz_nota_jurado[indice]}")

def buscar_participante(array_nombre:list,array_notas_jurados:list):
    """busca participantes y muestra sus datos

    Args:
        array_nombre (list): _description_
        array_notas_jurados (list): _description_
    """
    buscar_nombre = input("Ingrese nombre del participante que desea buscar: ")
    for i in range(len(array_nombre)):
        if buscar_nombre == array_nombre[i]:
            sumar_filas = sumar_fila(array_notas_jurados,i)
            promedio_punt = calcular_promedio(sumar_filas,3)
            print(f"Participante encontrado")
            mostrar_puntaje(array_nombre,array_notas_jurados,i)
            print(f"El promedio de los puntajes de {buscar_nombre} es de {promedio_punt} ")
        elif buscar_nombre != array_nombre[i]:
            continue
        else:
            print("Error")

#len(array_notas_jurados[jurado])
#array_notas_jurados[jurado]
jurado_estricto(array_notas_jurados)