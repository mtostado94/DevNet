#!/usr/bin/env python3

import requests
import json
from tabulate import *
from Solicitudes_APIC_EM import *

requests.packages.urllib3.disable_warnings()

def main():
    print(''' 
        SOLICITUDES
        1. Ver Hosts.
        2. Ver dispositivos de Red.
        3. Ver las Intefaces.
        4. Ver localizaciones.
        5. Salir.
        ''')
    op = int(input("Elige una opción: "))
    return op 
    

while True:
    try:
        opcion = main()
    
        if opcion >0 and opcion < 6:
            if opcion == 1:
                print_host()
            elif opcion == 2:
                getNetworkDevices()
            elif opcion == 3:
                interfaces()
            elif opcion == 4:
                location()    
            elif opcion == 5:
                break
        else:
            print("Opción incorrecta, vuelve a elegir")

    except ValueError:
        print("Opción incorrecta, vuelve a elegir")