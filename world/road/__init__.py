class Road:
    def __init__(self):
        print("Road created")
    
    def set_name(self, name):
        self._name = name

    def set_length(self, length):
        self._length = length

    def set_lanes(self, lanes):
        self._lanes = lanes

    def set_speed_limit(self, speed_limit):
        self._speed_limit = speed_limit

    def name(self) -> str:
        return self._name