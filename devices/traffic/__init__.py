class TrafficDetector:
    def __init__(self):
        self._sensors = []

    def add_sensor(self, sensor):
        self._sensors.append(sensor)

    def show_sensors(self):
        for s in self._sensors:
            print(s)