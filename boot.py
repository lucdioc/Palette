# Bout de code � placer dans boot.py pour connecter automatiquement le
# Lopy � chaque red�marrage

import machine
from network import WLAN
wlan = WLAN() # get current object, without changing the mode

if machine.reset_cause() != machine.SOFT_RESET:
    wlan.init(mode=WLAN.STA)
    # configuration below MUST match your home router settings!!
    #wlan.ifconfig(0,'dhcp')
wlan.ifconfig(config=('192.168.1.150', '255.255.255.0', '192.168.1.1', '192.168.1.1'))


if not wlan.isconnected():
    # change the line below to match your network ssid, security and password
    wlan.connect('TLReseau', auth=(WLAN.WPA2, 'm0nr3s3@u@m01'), timeout=5000)
    while not wlan.isconnected():
        machine.idle() # save power while waiting