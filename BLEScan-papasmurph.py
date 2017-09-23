from network import Bluetooth
import pycom
import time
import gc

pycom.heartbeat(False)
timeSleep = 0.01

bluetooth = Bluetooth()

def new_adv_event(event):
    if event.events() == Bluetooth.NEW_ADV_EVENT:
        anydata = True
        while anydata:
            device = bluetooth.get_adv()
            if device != None:
                rssi = device.rssi
                data = [b for b in device.data]
                if data[5] == 0x4c and data[6] == 0x00 and data[7] == 0x02 and data[8] == 0x15:
                    majorid = data[25] * 256 + data[26]
                    minorid = data[27] * 256 + data[28]
                    power = data[29]
                    if power > 127:
                        power -= 256

                    pycom.rgbled(0x000800)
                    print("iBeacon: " + str(rssi) + '/' + str(power) + ' (' + str(rssi - power) + ') ' + str(majorid) + '/' + str(minorid))            
                else:
                    pycom.rgbled(0x000008)

                time.sleep(timeSleep)
                pycom.rgbled(0x000000)
            else:
                anydata = False
            
bluetooth.callback(trigger = Bluetooth.NEW_ADV_EVENT, handler = new_adv_event)

while True:
    if not bluetooth.isscanning():
        print("Restarting scan")
        bluetooth.deinit()
        bluetooth.init()
        bluetooth.start_scan(10)

    time.sleep(1)
