#alarma PIR dos sectores
import machine
import utime


led_ext = machine.Pin(15, machine.Pin.OUT)

sensor_pir_1 = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_DOWN)
sensor_pir_2 = machine.Pin(17, machine.Pin.IN, machine.Pin.PULL_DOWN)

def sensor_alarma(pin):
    utime.sleep_ms(100)
    if pin is sensor_pir_1:
        print('Alarma, movimiento detectado en el dormitorio!')
    elif pin is sensor_pir_2:
        print('Alarma, movimiento detectado en la cocina!')
    
                
sensor_pir_1.irq(trigger=machine.Pin.IRQ_RISING, handler=sensor_alarma)
sensor_pir_2.irq(trigger=machine.Pin.IRQ_RISING, handler=sensor_alarma)

while True:
    led_ext.toggle()
    utime.sleep(1)
