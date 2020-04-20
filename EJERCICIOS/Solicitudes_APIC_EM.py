import requests
import json
from tabulate import *
requests.packages.urllib3.disable_warnings()

def get_ticket():
    url = "https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/ticket"
    headers = {
    
        'Content-Type': 'application/json'
    }

    body_json = {
        "password": "Xj3BDqbU",
	    "username": "devnetuser"

    }
    resp=requests.post(url, json.dumps(body_json), headers=headers, verify=False)
    status = resp.status_code # statuys code property of resp object
    response_json = resp.json()
    serviceTicket = response_json["response"]["serviceTicket"]
    #print("El ticket de servicio es: ", serviceTicket)
    return serviceTicket

def print_host():
    url = "https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/host"
    ticket = get_ticket()
    headers = {

    'Content-Type': 'application/json',
    'X-Auth-Token': ticket
    }
    resp = requests.get(url, headers=headers, verify=False)
    response_json = resp.json()
    HostList = []
    counter = 0

    for item in response_json["response"]:
        counter += 1
        host = [
            counter,
            item["hostType"],
            item["hostIp"],
            item["hostMac"]
            ]
        HostList.append(host)

    tableHeader = ["Number","Name","IP","MAC"]
    print("HOSTS:")
    print(tabulate(HostList,tableHeader))


def getNetworkDevices():
    url = "https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/network-device"
    ticket = get_ticket()
    headers = {
        
        'Content-Type': 'application/json',
        'X-Auth-Token': ticket
    }

    resp = requests.get(url,headers=headers,verify=False)
    response_json = resp.json()
    deviceList = []
    for item in response_json['response']:
        devices = [
            item["hostname"],
            item["family"],
            item["macAddress"],
            item["softwareVersion"]
            ]
        deviceList.append(devices)
    tableHeader = ["NAME","FAMILY","MAC","VERSION"]
    print("DEVICES:")
    print(tabulate(deviceList,tableHeader))        

def interfaces():
    url = "https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/interface"
    ticket = get_ticket()
    headers = {
        
        'Content-Type': 'application/json',
        'X-Auth-Token': ticket
    }
    resp = requests.get(url,headers=headers,verify=False)
    response_json = resp.json()
    interfaceList = []
    for item in response_json['response']:
        interfaces = [
            item["className"],
            item["status"],
            item["interfaceType"],
            item["macAddress"],
            item["ipv4Address"],
            item["ipv4Mask"]
            ]
        interfaceList.append(interfaces)
    tableHeader = ["NAME","STATUS","INT-TYPE","MAC","IP","MASK"]
    print("INTERFACES:")
    print(tabulate(interfaceList,tableHeader))


def location():
    url = "https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/location"
    ticket = get_ticket()
    headers = {

    'Content-Type': 'application/json',
    'X-Auth-Token': ticket
    }
    resp = requests.get(url,headers=headers,verify=False)
    response_json = resp.json()
    locationList = []
    for item in response_json['response']:
        locations = [
            item["locationName"],
            item["id"],
            item["geographicalAddress"]
        ]
        locationList.append(locations)
    tableHeader = ["LOCATIONS","ID","GEOGRAPHICAL ADDRESS"]
    print("INTERFACES:")
    print(tabulate(locationList,tableHeader))




