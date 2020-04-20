#/usr/bin/env python3
from ncclient import manager
import xml.dom.minidom
import xmltodict
from tabulate import *

con = manager.connect(host="192.168.56.101",port=830,username="cisco",password="cisco123!",hostkey_verify=False)

def main():
    print(''' OPCIONES:
        1. Ver interfaces
        2. Crear interfaz loopback
        3. Borrar interfaz
        5. Salir''')
    op = int(input("Elige una opción: "))
    return op 


def interfaces():
    netconf_filter = """
    <filter>
        <interfaces-state xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces"/>
    </filter>
    """

    netconf_reply = con.get(filter=netconf_filter)


    netconf_reply_dict = xmltodict.parse(netconf_reply.xml)

    for interface in netconf_reply_dict["rpc-reply"]["data"]["interfaces-state"]["interface"]:
        print("Name: {} MAC: {} Input: {} Output: {}".format(
            interface["name"],
            interface["phys-address"],
            interface["statistics"]["in-octets"],
            interface["statistics"]["out-octets"]
            )
        )


def crear_interfaz():

    name =str(input("Introduce el número de Loopback a crear: "))
    desc = str(input("Introduce una descripción: "))
    ip4 = str(input("Introduce una ip(Ejemplo: 5.5.5.5): "))
    masc = str(input("Introduce su Mascara de Subred(Ejemplo: 255.255.255.0): "))

    netconf_data = f"""
    <config> <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <interface>
            <Loopback>
                <name>{name}</name>
                <description>{desc}</description>
                <ip>
                    <address>
                        <primary>
                            <address>{ip4}</address>
                            <mask>{masc}</mask>
                        </primary>
                    </address>
                </ip>
            </Loopback>    
        </interface>
    </native></config>    
    """

    #Recoger informacion del dispositivo

    netconf_reply = con.edit_config(target="running", config=netconf_data)

    #printamos configuración

    print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
    interfaces()

def borra_interfaz():
    name =str(input("Introduce el número de Loopback a crear: "))


while True:
    try:
        opcion = main()
    
        if opcion >0 and opcion < 6:
            if opcion == 1:
                interfaces()
            elif opcion == 2:
                crear_interfaz()
            elif opcion == 3:
                borrar_interfaz()
            elif opcion == 4:
                pass    
            elif opcion == 5:
                break
        else:
            print("Opción incorrecta, vuelve a elegir")

    except ValueError:
        print("Opción incorrecta, vuelve a elegir")