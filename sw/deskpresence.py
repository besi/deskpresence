import time
from machine import Pin

motion = Pin(33, Pin.IN)

def on_motion(pin):
    print("motion detected: "  + str(time.time()%100))
    
    
    
# motion.irq(on_motion)
while True:
    print(motion.value())
    time.sleep_ms(500)