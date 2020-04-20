from math import sqrt

def menu():
    print(''' 
        CALCULADORA:
        1.Sumar.
        2.Restar.
        3.Multiplicar.
        4.Dividir.
        5.Exponenciales.
        6.Raiz cuadrara.
        7.Salir.
        ''')
    op = int(input("Elige una opción: "))
    return op

def suma(x, y):
    return x + y

def resta(x , y):
    return x - y

def multi(x, y):
    return x * y

def division(x, y):
    if y == 0:
        print( "No se puede dividir por 0")
    else:
        return x / y

def exponenciales(x,y):
    return x ** y


def raiz(x):
    return sqrt(x)

while True:
 
    try: 
        opcion = menu() 
        if opcion == 6:
            c = eval(input("Introduce Número para hayar su raiz: "))
            resultado = raiz(c)
            print(f"La raiz cuadrada de  {c} es:{resultado}")
        elif opcion == 7:
            print(f"saliendo...")
            break  
        elif opcion < 6 and opcion >0: 
            1
            a= eval(input("Introduce primer operando: "))
            b= eval(input("Introduce segundo operando: "))

            if opcion == 1:
                resultado = suma(a, b)
                print(f"El resultado de {a} más {b} es igual a: {resultado} ")

            elif opcion == 2: 
                resultado = resta(a, b)	
                print(f"El resultado de {a} menos {b} es igual a: {resultado} ")
            elif opcion == 3: 
                resultado = multi(a, b)
                print(f"El resultado de {a} por {b} es igual a: {resultado} ")
            elif opcion == 4: 
                resultado = division(a, b)
                print(f"El resultado de {a} entre {b} es igual a: {resultado} ")
            elif opcion == 5:
                resultado = exponenciales(a, b)
                print(f"El resultado de {a} elevado a {b} es igual a: {resultado} ")

        else:
            print("No valido, introduce una de las 7 opciones")

  
    except ValueError:
        print ("No valido, introduce una de las 7 opciones") 