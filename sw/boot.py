from network import WLAN, STA_IF, AP_IF
from time import sleep_ms
import secrets
import machine
import utime
import time

def try_connection(timeout = 12):

    while not wlan.isconnected() and timeout > 0:
        print('.', end='')
        sleep_ms(500)
        timeout = timeout - 1
    return wlan.isconnected();


print("Starting up")
WLAN(AP_IF).active(False) # Disable AP access point
wlan = WLAN(STA_IF)
wlan.active(True)
ssid = ''
# Only for deep sleep ?
# print('connecting to last AP', end='')
# print(try_connection(3))
if not wlan.isconnected():
    ap_list = wlan.scan()
    ## sort APs by signal strength
    ap_list.sort(key=lambda ap: ap[3], reverse=True)
    ## filter only trusted APs
    ap_list = list(filter(lambda ap: ap[0].decode('UTF-8') in
              secrets.wifi.aps.keys(), ap_list))
    for ap in ap_list:
        essid = ap[0].decode('UTF-8')
        if not wlan.isconnected():
            ssid = essid
            print('connecting to "', essid, end='"')
            wlan.connect(essid, secrets.wifi.aps[essid])
            print(try_connection())


# Update the time
from ntptime import settime
settime()
utime.sleep_ms(1000)

import gc
gc.collect()


print(wlan.ifconfig()[0])
print(ssid)
import webrepl
webrepl.start()

