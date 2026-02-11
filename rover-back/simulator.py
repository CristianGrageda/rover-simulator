import time
from rover import Rover

rover = Rover()
TICK = 1

def run():
    while True:
        rover.update(TICK)
        time.sleep(TICK)

if __name__ == "__main__":
    print("🛰️ Rover simulator started")
    run()
