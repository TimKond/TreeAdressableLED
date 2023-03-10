import time
from rpi_ws281x import *
import argparse
import colorsys

# LED strip configuration:
LED_COUNT      = 150      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

# Create NeoPixel object with appropriate configuration.
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
# Intialize the library (must be called once before other functions).
strip.begin()

def setColor(color):
    if isinstance(color, int):
        for i in range(strip.numPixels()):
	        strip.setPixelColor(i, color)
        strip.show()
    elif isinstance(color, list):
        for i in range(len(color)):
	        strip.setPixelColor(i, color[i])
        strip.show()
    elif isinstance(color, tuple):
        r,g,b = color
        c = Color(r,g,b)
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, c)
        strip.show()

def turn_single_on(i):
    strip.setPixelColor(i, Color(255,255,255))
    strip.show()


def rainbow():
    TIMER = 30
    pos = 0.0
    pos_delta = 0.01
    colors = [Color(0,0,0) for led in range(LED_COUNT)]
    while True:
        r,g,b = colorsys.hsv_to_rgb(pos, 1.0, 1.0)
        colors.insert(0, Color(int(r*255),int(g*255),int(b*255)))
        colors.pop()
        pos += pos_delta
        setColor(colors)
        time.sleep(TIMER/1000.0) 

def flash():
    TIMER = 30
    pos = 0.0
    pos_delta = 0.01
    colors = [Color(0,0,0) for led in range(LED_COUNT)]
    while True:
        for _ in range(5):
            r,g,b = colorsys.hsv_to_rgb(pos, 1.0, 1.0)
            colors.insert(0, Color(int(r*255),int(g*255),int(b*255)))
            colors.insert(0, Color(0,0,0))
            colors.pop()
            colors.pop()
            pos += pos_delta
            setColor(colors)
            time.sleep(TIMER/1000.0) 
        for _ in range(5):
            r,g,b = colorsys.hsv_to_rgb(pos, 1.0, 1.0)
            colors.insert(0, Color(0,0,0))
            colors.insert(0, Color(int(r*255),int(g*255),int(b*255)))
            colors.pop()
            colors.pop()
            pos += pos_delta
            setColor(colors)
            time.sleep(TIMER/1000.0) 


def passthrough():
    TIMER = 30
    count = 0.0
    colors = [Color(0,0,0) for led in range(LED_COUNT)]
    while True:
        if count == 25:
            colors.insert(0, Color(0,255,0))
            colors.pop()
            count = 0
        else:
            colors.insert(0, Color(0,0,0))
            colors.pop()
        setColor(colors)
        count += 1
        time.sleep(TIMER/1000.0) 


