import os, sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from devices.traffic import TrafficDetector
from world.road import Road


def main():
    r = Road()
    r.set_name("I-10")
    print(r.name())

    device = TrafficDetector()
    device.add_sensor("Detection-Zone-1")
    device.show_sensors()


if __name__ == "__main__":
    main()