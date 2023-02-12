# TreeAdressableLED
This script starts a webserver to run various LED programm patterns on a addressable rgb fairy light strip. Each endpoint ends the current programm and starts a new programm.
1. Requires uvicorn and rpi-ws281x from https://pypi.org/project/rpi-ws281x/1.1.1/ to adress strip LEDs
2. Raspberry GPIO configuration in [HelloLED.py](https://github.com/TimKond/TreeAdressableLED/blob/main/HelloLED.py)
3. Start app.py

Endpoints:
  - /rainbow
  - /flash
  - /color
  - /stop
  - /passthrough
  - /turn_on
