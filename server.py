from fastapi import FastAPI
import multiprocessing
from HelloLED import rainbow, flash, setColor, passthrough, turn_single_on

app = FastAPI()
app.p = multiprocessing.Process(target=rainbow)
app.p.start()

def kill_process():
    if(app.p != None):
        app.p.kill()

@app.get("/rainbow")
def start_rainbow():
    kill_process()
    app.p = multiprocessing.Process(target=rainbow)
    app.p.start()
    return {"Tree": "rainbow"}

@app.get("/flash")
def start_rainbow():
    kill_process()
    app.p = multiprocessing.Process(target=flash)
    app.p.start()
    return {"Tree": "flash"}

@app.get("/color")
def stop(r: int = 0, g: int = 0, b: int = 0):
    kill_process()
    setColor((g,r,b))
    return {"Tree": "Your Color!"}

@app.get("/stop")
def stop():
    kill_process()
    setColor((0,0,0))
    return {"Tree": "Stop"}

@app.get("/red")
def red():
    kill_process()
    setColor((0,255,0))
    return {"Tree": "Red"}

@app.get("/passthrough")
def start_passthrough():
    kill_process()
    app.p = multiprocessing.Process(target=passthrough)
    app.p.start()
    return {"Tree": "passthrough"}

@app.get("/turn_on")
def stop(i: int = 0):
    kill_process()
    setColor((0,0,0))
    turn_single_on(i)
    return {"Tree": "on!"}