# rainbow.py
import spidev
import time

DELAY = 0.04
LED_COUNT = 2
 
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
    spi.writebytes([0xA2, 255, 255, 255, 255])
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
        # BOOSTER_SETRAINBOW HUE (2 Bytes), SATURATION, VALUE, von der ersten (0) bis
        # zur letzten LED in 10-er Schritten, BOOSTER_SHOW
        # spi.writebytes([0xA7, i & 0xFF, i >> 8, 255, 100, 0, LED_COUNT - 1, 10, 0xB2])  
        clear()
        time.sleep(DELAY)
        print(".")
except KeyboardInterrupt:
    clear()
    spi.close()
