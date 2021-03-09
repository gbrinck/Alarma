#alarma PIR
import machine
import utime

sensor_pir_1 = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_DOWN)

def sensor_alarma(pin):
    utime.sleep_ms(100)
    if pin.value():
        print('Alarma, Alarma! Movimiento detectado!')
        
sensor_pir_1.irq(trigger=machine.Pin.IRQ_RISING, handler=sensor_alarma)
  