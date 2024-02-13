from machine import TouchPad, Pin
import time



def makeTouchPad(pin):
    return TouchPad(Pin(pin))

def calibratePad(pad):
    return pad.read()
    
pins = [27, 12,13,14,33,32]
pads = list(map(makeTouchPad, pins))


print("Calibrating touch pads...")
print("Ready")
cali = list(map(calibratePad, pads))
threshold = 0.8

swipe = -1
count = 0
while True:
    for pad in pads:
        index = pads.index(pad)
        if(pad.read() < cali[index]*0.8):
            if(index == 5):
                print("Left")
            elif (index ==4):
                print("Right")
            else:
                print(index+1)
            time.sleep(0.1)
            if swipe + 1 == index:
                swipe = index
            if swipe == 3:
                count = count + 1
                print("SWIPE Left #" + str(count))
                swipe = -1
            
    time.sleep(0.05)    
