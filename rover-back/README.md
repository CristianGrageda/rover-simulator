This project simulates a rover and streams telemetry via WebSockets.
The simulator can later be replaced by real hardware.

The project is started with the following commands:
uvicorn rover_simulator:app --port 8001
uvicorn rover_control:app --port 8000

Comunicacion:
rover.py: Tiene la funcionalidad de ser un rover teniendo un estado que varia dependiendo de ciertos parametros (temperatura, bateria, posicion), estos datos se actualizan aleatoriamente cada x tiempo mediante un metodo simulador que puede utilizar quien lo consuma.
rover_simulator.py: Tiene la funcionalidad de exponer la telemetria del rover (consumiendo rover.py) a traves de websockets mientras la actualiza cada x tiempo.
api_control.py: Obtiene la telemetria expuesta por rover_simulator y la reexpone a traves de websockets. Por ahora solo hace eso, mas adelante tendra logica para controlar el rover.

# Rover Simulation Project 🛰️

This project simulates a planetary rover and streams its telemetry in real time using WebSockets.
The simulator is designed to be easily replaceable by real hardware in the future, without changing the control or visualization layers.

---

## 🚀 How to run the project

The system is composed of two independent services.

### 1. Rover Simulator
Exposes rover telemetry via WebSockets and updates the rover state periodically.

```bash
uvicorn rover_simulator:app --port 8001
```

### 2. Rover Control API

Consumes telemetry from the simulator and re-exposes it via WebSockets.
In the future, this service will also be responsible for sending control commands to the rover.

```bash
uvicorn rover_control:app --port 8000
```

## 🔌 Communication & Architecture

The project is structured around clear responsibilities:

### rover.py

- Represents the rover domain model.

- Maintains the rover state (position, battery, temperature, status).

- Updates its state based on simulation logic.

- Has no knowledge of networking or APIs.

### rover_simulator.py

- Owns the simulation loop.

- Periodically updates the rover state.

- Exposes rover telemetry via WebSockets.

- Acts as a stand-in for future real hardware.

### api_control.py

- Connects to the rover simulator via WebSockets.

- Re-exposes telemetry to external clients (UI, dashboards, etc.).

- Will later include rover control logic (movement, commands, safety checks).

## 🧠 Design Goals

- Clear separation of responsibilities

- Decoupled architecture

- Real-time telemetry streaming

- Hardware-agnostic design

This architecture allows the simulator to be replaced by real rover hardware with minimal changes to the rest of the system.

## 📊 Mission Control UI
(Coming soon)