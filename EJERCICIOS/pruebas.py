from ncclient import manager

con = manager.connect(host='192.168.56.101', port=830 , username='cisco', password='cisco123!', hostkey_verify=False)

print("Informacion  de capabilities")

for capability in con.server_capabilities:
    print(capability)