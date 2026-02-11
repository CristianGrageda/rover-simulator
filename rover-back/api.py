from fastapi import FastAPI
import threading
import time
from rover import Rover

app = FastAPI()
rover = Rover()
TICK = 1

def simulator_loop():
    while True:
        rover.update(TICK)
        time.sleep(TICK)

@app.on_event("startup")
def start_simulator():
    thread = threading.Thread(target=simulator_loop, daemon=True)
    thread.start()

@app.get("/telemetry")
def get_telemetry():
    return rover.telemetry()
