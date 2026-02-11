from fastapi import FastAPI
import time
import threading
from rover import Rover

app = FastAPI()
rover = Rover()
TICK = 1

def simulator_loop():
    while True:
        rover.update(TICK)
        time.sleep(TICK)

@app.on_event("startup")
def start_sim():
    threading.Thread(target=simulator_loop, daemon=True).start()

@app.get("/telemetry")
def telemetry():
    return rover.telemetry()

@app.post("/command/move")
def move(direction: str):
    #rover.move(direction)
    return {"status": "ok", "direction": direction}

@app.post("/command/stop")
def stop():
    #rover.stop()
    return {"status": "stopped"}


# uvicorn rover_simulator:app --port 8001