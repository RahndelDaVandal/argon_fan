# fan_control.py
import RPi.GPIO as GPIO
from smbus2 import SMBus, i2c_msg

GPIO.setwarnings(False)

rev = GPIO.RPI_REVISION
if rev == 2 or rev == 3:
    bus = SMBus(1)
else:
    bus = SMBus(0)

fan_addr = 0x1a

def set_fan(addr:int, speed:int) -> None:
    bus.write_byte(addr, speed)
    print(f'set FanSpeed={speed}')

#bus.close()
#GPIO.cleanup()
