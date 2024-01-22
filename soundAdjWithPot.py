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

value =0

a0=analogio.AnalogIn(board.GP27)


value =int(a0.value/650)
perc=0
for i in range(100):
    cc.send(ConsumerControlCode.VOLUME_DECREMENT)
for y in range(value):
    cc.send(ConsumerControlCode.VOLUME_INCREMENT)
    perc=perc+1


while True:
    value =int(a0.value/650)
    
    if(perc < value):
        for c in range(value-perc):
            cc.send(ConsumerControlCode.VOLUME_INCREMENT)
            perc=perc+1
    if(perc > value):
        for c in range(perc-value):
            cc.send(ConsumerControlCode.VOLUME_DECREMENT)
            perc=perc-1

    time.sleep(0.1)
