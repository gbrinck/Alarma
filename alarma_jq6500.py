#alarma PIR
import machine
import utime


led_ext = machine.Pin(15, machine.Pin.OUT)
zumbador = machine.Pin(14, machine.Pin.OUT)
jq6500 = machine.Pin(13, machine.Pin.OUT)
sensor_pir_1 = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_DOWN)

def sensor_alarma(pin):
    utime.sleep_ms(100)
    if pin.value():
        print('Alarma, Alarma! Movimiento detectado!')
        jq6500.value(0)
        utime.sleep(5)
        jq6500.value(1)
        
sensor_pir_1.irq(trigger=machine.Pin.IRQ_RISING, handler=sensor_alarma)

while True:
    led_ext.toggle()
    utime.sleep(1)
