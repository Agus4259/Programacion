def mostrar(num):
    return num

def par(num):
    calculo_sobra = num % 2
    if calculo_sobra == 0:
        return "True"
    else:
        return "False"
    

def  restar1(numero : int, numero_a :int)->int:
    return numero - numero_a

def restar2()->int:
    return 20 -1

def restar3(numero_b : int, numero_d : int):
    return numero_b - numero_d

def restar4():
    return 2 - 1 

def realizarDescuento(num : int):
        return num - (num * 5/100)


def s_sumar(num_a,num_b):
        return num_a + num_b
        
def r_restar(num_c,num_d):
        return num_c + num_d

def calculo_impuestos_nacional(valor_ventas_nacionales,iva = 21):
    return valor_ventas_nacionales* (1 / (1 + (iva / 100)))

def calculo_impuestos_exportaciones(valor_exportaciones,retenciones= 15):
    return valor_exportaciones* (1- (retenciones / 100))


def calcular_salario(hrs_trabajadas,):
    salario = hrs_trabajadas * 10 + ((hrs_trabajadas * 10))
    return salario


def calcular_años_antig(salario, años_antig):
    return salario + ((salario * 3/100)*años_antig)

def calcular_product(artef_producidos,hrs_trabajadas):
    return artef_producidos / hrs_trabajadas

def mostrar_datos(nombre,edad,hrs_trabajadas,artef_producidos,años_antig,productividad,salario,salario_cn_incr):
    return print (f"""Su nombre es {nombre}
                      Su edad es {edad}  
                      Usted ha trabajado {hrs_trabajadas} horas
                      Usted ha producido {artef_producidos}  artefactos
                      Usted ha trabajado {años_antig} años
                      Usted ha sido un {productividad}% productivo
                      Su salario es{salario}
                      Su salario con incremento por años de antiguedad es {salario_cn_incr}""")