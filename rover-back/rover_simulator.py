# uvicorn rover_simulator:app --port 8001

from fastapi import FastAPI, WebSocket
import asyncio
from rover import Rover

app = FastAPI()
rover = Rover()

@app.websocket("/ws/telemetry")
async def telemetry_ws(ws: WebSocket):
    await ws.accept()
    try:
        while True:
            rover.update(1)
            await ws.send_json(rover.telemetry())
            await asyncio.sleep(1)
    except Exception:
        await ws.close()