#alarma PIR
import machine
import utime


led_ext = machine.Pin(15, machine.Pin.OUT)
zumbador = machine.Pin(14, machine.Pin.OUT)
sensor_pir_1 = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_DOWN)

def sensor_alarma(pin):
    utime.sleep_ms(100)
    if pin.value():
        print('Alarma, Alarma! Movimiento detectado!')
        for veces in range(20):
            led_ext.toggle()
            zumbador.value(1)
            utime.sleep_ms(100)
        zumbador.value(0)
sensor_pir_1.irq(trigger=machine.Pin.IRQ_RISING, handler=sensor_alarma)

while True:
    led_ext.toggle()
    utime.sleep(1)
