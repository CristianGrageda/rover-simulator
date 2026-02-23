# uvicorn api_control:app --port 8000

from fastapi import FastAPI, WebSocket
import websockets
import asyncio
import json

app = FastAPI()

SIM_WS = "ws://127.0.0.1:8001/ws/telemetry"

@app.websocket("/ws/telemetry")
async def telemetry_proxy(ws: WebSocket):
    await ws.accept()
    async with websockets.connect(SIM_WS) as sim_ws:
        while True:
            data = await sim_ws.recv()
            await ws.send_text(data)