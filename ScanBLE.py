import binascii
import socket
from network import Bluetooth

#initialisations
bluetooth = Bluetooth()
tampon=[]
bluetooth.stop_scan()

# Fonction de scannage

bluetooth.start_scan(20)
while bluetooth.isscanning():
	adv=bluetooth.get_adv()
	if adv!=None:
		data=adv.mac
		tampon.append(data)








cartographie=list(set(tampon))
#print(cartographie)

# Fonction de publication sur port TCP
# Ici, connexion sur port 1881 de mon ordinateur portable dont l'adresse sur le réseau local est 192.168.1.102
# Le port 1881 a été ouvert aux connexion TCP dans le pare-feu Windows et Node-RED écoute ce port (noeud TCP en mode listen)
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM,socket.IPPROTO_TCP)
addr=('192.168.1.102',1881)
s.connect(addr)
s.send(cartographie[0])