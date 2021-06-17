from machine import Pin

led = Pin(25, Pin.OUT)
# Turn led on
led.value(1)
# Turn led off
led.value(0)
