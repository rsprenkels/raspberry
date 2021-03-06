# rainbow.py
import spidev
import time

DELAY = 1.0
LED_COUNT = 64
 
spi = spidev.SpiDev()
 
def initSPI():
    # open /dev/spidev0.1 (CS1 Pin wird verwendet)
    spi.open(0, 1)  
    spi.mode = 0b00
    time.sleep(DELAY)
    return
 
def initLEDs():
    # BOOSTER_INIT mit der Anzahl der LEDs und 24/32 bits pro LED
    spi.writebytes([0xB1, LED_COUNT, 32])
    time.sleep(DELAY)
    return
 
 
def clear():
    # BOOSTER_SETRGBW, BOOSTER_SETALL, BOOSTER_SHOW
    spi.writebytes([0xA2, 10, 0, 10, 0])
    time.sleep(DELAY)
    spi.writebytes([0xA5])
    time.sleep(DELAY)
    spi.writebytes([0xB2])
    time.sleep(DELAY)
    return
 
i = 0
initSPI()
initLEDs()
clear()
 
try:
    while True:
        i += 1
        val = (i % 50) + 2
        spi.writebytes([0xA2, val, 0, 0, 0])
        # time.sleep(DELAY)
        spi.writebytes([0xA5])
        # time.sleep(DELAY)
        spi.writebytes([0xB2])
        time.sleep(DELAY)
        print(val)
except KeyboardInterrupt:
    clear()
    spi.close()
