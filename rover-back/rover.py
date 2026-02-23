import math
import random
from enum import Enum


class RoverStatus(Enum):
    NOMINAL = "NOMINAL"
    WARNING = "WARNING"
    SAFE = "SAFE"
    ERROR = "ERROR"


class Rover:

    # Initial state of rover
    def __init__(self):
        self.x = 0.0
        self.y = 0.0
        self.direction = 0.0
        self.speed = 0.5

        self.battery = 100.0
        self.temperature = 20.0
        self.status = RoverStatus.NOMINAL

    # Update rover status every x amount of time (position, battery, temperature)
    def update(self, delta_time):
        if self.status == RoverStatus.NOMINAL:
            rad = math.radians(self.direction)
            self.x += math.cos(rad) * self.speed * delta_time
            self.y += math.sin(rad) * self.speed * delta_time

        self.battery -= 0.2 * delta_time
        self.temperature += random.uniform(-0.1, 0.3)

        self.apply_rules()

    def apply_rules(self):
        if self.temperature > 90:
            self.status = RoverStatus.ERROR
        elif self.battery < 5:
            self.status = RoverStatus.SAFE
        elif self.battery < 20:
            self.status = RoverStatus.WARNING
        else:
            self.status = RoverStatus.NOMINAL

    # Returns rover telemetry in its current state
    def telemetry(self):
        return {
            "position": {
                "x": round(self.x, 2),
                "y": round(self.y, 2),
            },
            "battery": round(self.battery, 2),
            "temperature": round(self.temperature, 2),
            "status": self.status.value
        }
