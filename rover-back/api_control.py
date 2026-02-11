from fastapi import FastAPI
import requests

SIM_URL = "http://127.0.0.1:8001"

app = FastAPI()

@app.get("/telemetry")
def get_telemetry():
    r = requests.get(f"{SIM_URL}/telemetry")
    return r.json()

@app.post("/move")
def move(direction: str):
    r = requests.post(f"{SIM_URL}/command/move", params={"direction": direction})
    return r.json()

@app.post("/stop")
def stop():
    r = requests.post(f"{SIM_URL}/command/stop")
    return r.json()

# uvicorn api_control:app --port 8000