class Engine:
    def __init__(self):
        self.running = False

    def start(self):
        if not self.running:
            self.running = True
            print("Engine started.")
        else:
            print("Engine is already running.")

    def stop(self):
        if self.running:
            self.running = False
            print("Engine stopped.")
        else:
            print("Engine is already stopped.")

class Car:
    def __init__(self):
        self.engine = Engine()

    def start_engine(self):
        self.engine.start()

    def stop_engine(self):
        self.engine.stop()

# Demonstrating how Car controls the Engine
my_car = Car()

# Starting the engine
my_car.start_engine()  # Output: Engine started.

# Trying to start the engine again
my_car.start_engine()  # Output: Engine is already running.

# Stopping the engine
my_car.stop_engine()  # Output: Engine stopped.

# Trying to stop the engine again
my_car.stop_engine()  # Output: Engine is already stopped.
