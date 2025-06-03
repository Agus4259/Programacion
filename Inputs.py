from Funciones import *

""""
Una academia de baile organiza una competencia abierta para definir a su nuevo o nueva 
representante nacional. La competencia cuenta con un jurado compuesto por tres personas, 
cada una de las cuales puntúa a los participantes del 1 al 10. 

Se requiere un sistema que permita: 
-Registrar los nombres de los participantes (5 en total) 
-Registrar las puntuaciones que cada jurado otorga a cada participante 
-Procesar y mostrar diferentes informaciones relevantes a partir de los datos cargados 
-Cada participante debe almacenar la siguiente información: 
--Nombre del participante 
--Puntuación del Jurado 1 
--Puntuación del Jurado 2
--Puntuación del Jurado 3 

Se requiere lo siguiente:  
1. Cargar participantes: Ingresar los nombres de cinco participantes. Cada nombre 
debe tener al menos 3 caracteres y solo contener letras y espacios. listo
2. Cargar puntuaciones: Ingresar la puntuación de cada jurado para cada participante. 
Las puntuaciones deben estar entre 1 y 10. listo
3. Mostrar puntuaciones: Mostrar para cada participante: nombre, puntajes individuales 
y promedio general. Usar formato claro y ordenado. listo
4. Participantes con promedio mayor a 4: Mostrar los que hayan tenido un promedio 
de puntuación mayor a 4. Si no hay ninguno, mostrar mensaje de error. listo
5. Participantes con promedio mayor a 7: Mostrar los que hayan tenido un promedio 
de puntuación mayor a 7. Si no hay ninguno, mostrar mensaje de error. listo
6. Promedio de cada jurado: Mostrar el promedio de puntuaciones otorgadas por cada 
jurado. listo
7. Jurado más estricto: Indicar cuál jurado otorgó los puntajes promedio más bajos.listo 
8. Buscar participante por nombre: Permitir ingresar un nombre y mostrar sus datos si 
existe. Si no existe, mostrar mensaje de error.

"""

bandera_carga_notas = False
bandera_carga_nombre = False

import os
from Funciones import *

array_nombre = crear_array("",5)
array_notas_jurados = crear_matriz(5,3,0)

while True:
    print("1. Cargar nombre de participante\n2. Cargar puntaje de los Jurados \n3.Mostrar Puntaje Participante \n4.Mostrar Puntaje de todos los Participante \n5. Mostrar participantes que su promedio de puntajes es mayor a 4\n6. Mostrar participantes que su promedio de puntajes es mayor a 7\n7. Mostrar promedio de Puntajes de los jurados\n8.Mostrar Jurado mas estricto\n9.Buscar participante\n10.Salir")

    opcion = int(input("Su opcion: "))
    while opcion > 10 or opcion < 1:
        opcion = int(input("Reingrese su opcion (1-7): "))
    if opcion == 1:
        print("CARGANDO NOMBRES")
        cargar_nombre_part(array_nombre)
        print("NOMBREs CARGADOs CORRECTAMENTE")
        bandera_carga_nombre = True
    elif opcion == 2:
        print("CARGANDO NOTAS DE JURADOS ")
        cargar_nota_jurado(array_notas_jurados)
        print("NOTAs CARGADAs CORRECTAMENTE")
        mostrar_matriz(array_notas_jurados)
        bandera_carga_notas = True
    elif opcion == 3:
        if bandera_carga_notas != True and bandera_carga_nombre != True:
            print("Error, cargue primero los nombres y las notas")
        else:
            indice_part = int(input("Ingrese indice del participante que desea ver el puntaje:\n0(1er participante)\n1(2do participante)\n2(3erparticipante)\n3(4to participante)\n4(5to participante)5(6to participante)\n: "))
            mostrar_puntaje(array_nombre,array_notas_jurados,indice_part)
    elif opcion == 4:
        if bandera_carga_notas != True and bandera_carga_nombre != True:
            print("Error, cargue primero los nombres y las notas")
        else:
           mostrar_puntaje_todos(array_nombre,array_notas_jurados)
           print(f"Porcentaje general:{suma_elementos_matriz(array_notas_jurados)}")
    elif opcion == 5:
        if bandera_carga_notas != True and bandera_carga_nombre != True:
            print("Error, cargue primero los nombres y las notas")
        else:
            part_promedio(array_nombre,array_notas_jurados,4)
            buscar_min_array(array_notas_jurados)
    elif opcion == 6:
        if bandera_carga_notas != True and bandera_carga_nombre != True:
            print("Error, cargue primero los nombres y las notas")
        else:
            part_promedio(array_nombre,array_notas_jurados,7)
    elif opcion == 7:
        jurado_promedio(array_notas_jurados)
    elif opcion == 8:
        if bandera_carga_notas != True and bandera_carga_nombre != True:
            print("Error, cargue primero los nombres y las notas")
        else:
            jurado_estricto(array_notas_jurados)
    elif opcion == 9:
        if bandera_carga_notas != True and bandera_carga_nombre != True:
            print("Error, cargue primero los nombres y las notas")
        else:
            buscar_participante(array_nombre,array_notas_jurados)
    elif opcion == 10:
        print("Saliendo...")
        break

    input("Toque cualquier boton para continuar...")
    os.system("clear")