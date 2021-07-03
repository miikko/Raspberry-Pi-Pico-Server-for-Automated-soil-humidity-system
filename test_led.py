from machine import Pin, Timer

gp_pin_num = 25
led = Pin(gp_pin_num, Pin.OUT)
tim = Timer()

def tick(_):
    global led
    led.toggle()
    print("Toggle LED")

tim.init(freq=1, mode=Timer.PERIODIC, callback=tick)
