#/usr/bin/env python3
import modulo_RESNETCONF

def main():
    print(''' OPCIONES:
        1. Crear interfaz loopback
        2. Ver interfaces.
        3. Borrar interfaz.
        4. Tabla de routing.
        5. Salir''')
    op = int(input("Elige una opción: "))
    return op 


while True:
    try:
        opcion = main()
    
        if opcion >0 and opcion < 6:
            if opcion == 1:
                modulo_RESNETCONF.crear_interfaz()
            elif opcion == 2:
                modulo_RESNETCONF.interfaces()
            elif opcion == 3:
                modulo_RESNETCONF.borrar_interfaz()
            elif opcion == 4:
                modulo_RESNETCONF.routing()  
            elif opcion == 5:
                break
        else:
            print("Opción incorrecta, vuelve a elegir")

    except ValueError:
        print("Opción incorrecta, vuelve a elegir")