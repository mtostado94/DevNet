#/usr/bin/env python3
from ncclient import manager
import xml.dom.minidom, xmltodict
from tabulate import *
from netmiko import ConnectHandler

con = manager.connect(host="192.168.56.101",port=830,username="cisco",password="cisco123!",hostkey_verify=False)
sshCli = ConnectHandler(device_type='cisco_ios', host='192.168.56.101', port=22, username='cisco', password='cisco123!')


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

    try:
        netconf_reply = con.edit_config(target="running", config=netconf_data)
        interfaces()
    except:
        print("Algo ha fallado, intentalo de nuevo.")

def interfaces():
    netconf_filter = """
    <filter>
        <interfaces-state xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces"/>
    </filter>
    """

    netconf_reply = con.get(filter=netconf_filter)


    netconf_reply_dict = xmltodict.parse(netconf_reply.xml)
    try:
        for interface in netconf_reply_dict["rpc-reply"]["data"]["interfaces-state"]["interface"]:
            
                print("Name: {} MAC: {} Input: {} Output: {}".format(
                    interface["name"],
                    interface["phys-address"],
                    interface["statistics"]["in-octets"],
                    interface["statistics"]["out-octets"]
                    )
                )
    except TypeError:
        print("Solo hay una interfaz, crear primero una interfaz nueva.")

def borrar_interfaz():

    loop =int(input("Introduce el número de Loopback a borrar: "))

    config_commands = [f'no int loopback {loop}'] 

    output = sshCli.send_config_set(config_commands)
    output = sshCli.send_command("show ip int brief")
    print("IP interface status and configuration:\n{}\n".format(output))

def routing():
    output = sshCli.send_command("show ip route")
    print(output)

