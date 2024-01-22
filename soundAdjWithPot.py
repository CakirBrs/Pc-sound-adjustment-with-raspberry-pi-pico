import digitalio
import analogio
import board
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode
import time
keyboard = Keyboard(usb_hid.devices)
cc = ConsumerControl(usb_hid.devices)
onceki =0
simdiki =0

a0=analogio.AnalogIn(board.GP27)
print(a0.value)


simdiki =int(a0.value/650)
perc=0
for i in range(100):
    cc.send(ConsumerControlCode.VOLUME_DECREMENT)
for y in range(simdiki):
    cc.send(ConsumerControlCode.VOLUME_INCREMENT)
    perc=perc+1
    
print("simdiki")
print(simdiki)

while True:
    #print(a0.value/650)
    simdiki =int(a0.value/650)
    
    if(perc < simdiki):
        for c in range(simdiki-perc):
            cc.send(ConsumerControlCode.VOLUME_INCREMENT)
            perc=perc+1
    if(perc > simdiki):
        for c in range(perc-simdiki):
            cc.send(ConsumerControlCode.VOLUME_DECREMENT)
            perc=perc-1
    
    
    #onceki=simdiki
    
    time.sleep(0.1)