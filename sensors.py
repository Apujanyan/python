import itertools
from abc import ABC, abstractmethod
from sys import getsizeof


# Abstract base class Sensor
class Sensor(ABC):
    @abstractmethod
    def read_data(self) -> None:
        ...


# Sensor classes with __slots__
class TemperatureSensor(Sensor):
    __slots__ = ('__location', '__sensor_id')
    __sensor_id_counter = itertools.count()

    def __init__(
            self,
            location: str,
    ) -> None:
        self.location = location
        self.__sensor_id = next(self.__sensor_id_counter)

    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError("The location must be string!")
        elif value == '':
            raise ValueError("The location cannot be an empty string!")
        self.__location = value

    @property
    def sensor_id(self) -> int:
        return self.__sensor_id

    def read_data(self) -> None:
        print(f"Sensor type: {self.__class__.__name__}")
        print(f"Current location: {self.location}")
        print(f"Sensor ID: {self.sensor_id}\n")


class LightSensor(Sensor):
    __slots__ = ('__location', '__sensor_id')
    __sensor_id_counter = itertools.count()

    def __init__(
            self,
            location: str,
    ) -> None:
        self.location = location
        self.__sensor_id = next(self.__sensor_id_counter)

    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError("The location must be string!")
        elif value == '':
            raise ValueError("The location cannot be an empty string!")
        self.__location = value

    @property
    def sensor_id(self) -> int:
        return self.__sensor_id

    def read_data(self) -> None:
        print(f"Sensor type: {self.__class__.__name__}")
        print(f"Current location: {self.location}")
        print(f"Sensor ID: {self.sensor_id}\n")


class HumiditySensor(Sensor):
    __slots__ = ('__location', '__sensor_id')
    __sensor_id_counter = itertools.count()

    def __init__(
            self,
            location: str,
    ) -> None:
        self.location = location
        self.__sensor_id = next(self.__sensor_id_counter)

    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError("The location must be string!")
        elif value == '':
            raise ValueError("The location cannot be an empty string!")
        self.__location = value

    @property
    def sensor_id(self) -> int:
        return self.__sensor_id

    def read_data(self) -> None:
        print(f"Sensor type: {self.__class__.__name__}")
        print(f"Current location: {self.location}")
        print(f"Sensor ID: {self.sensor_id}\n")


# Sensor classes without __slots__
class TemperatureSensorWoutSl(Sensor):
    __sensor_id_counter = itertools.count()

    def __init__(
            self,
            location: str
    ) -> None:
        self.location = location
        self.__sensor_id = next(self.__sensor_id_counter)

    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError("The location must be string!")
        elif value == '':
            raise ValueError("The location cannot be an empty string!")
        self.__location = value

    @property
    def sensor_id(self) -> int:
        return self.__sensor_id

    def read_data(self) -> None:
        print(f"Sensor type: {self.__class__.__name__}")
        print(f"Current location: {self.location}")
        print(f"Sensor ID: {self.sensor_id}\n")


class LightSensorWoutSl(Sensor):
    __sensor_id_counter = itertools.count()

    def __init__(
            self,
            location: str,
    ) -> None:
        self.location = location
        self.__sensor_id = next(self.__sensor_id_counter)

    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError("The location must be string!")
        elif value == '':
            raise ValueError("The location cannot be an empty string!")
        self.__location = value

    @property
    def sensor_id(self) -> int:
        return self.__sensor_id

    def read_data(self) -> None:
        print(f"Sensor type: {self.__class__.__name__}")
        print(f"Current location: {self.location}")
        print(f"Sensor ID: {self.sensor_id}\n")


class HumiditySensorWoutSl(Sensor):
    __sensor_id_counter = itertools.count()

    def __init__(
            self,
            location: str,
    ) -> None:
        self.location = location
        self.__sensor_id = next(self.__sensor_id_counter)

    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError("The location must be string!")
        elif value == '':
            raise ValueError("The location cannot be an empty string!")
        self.__location = value

    @property
    def sensor_id(self) -> int:
        return self.__sensor_id

    def read_data(self) -> None:
        print(f"Sensor type: {self.__class__.__name__}")
        print(f"Current location: {self.location}")
        print(f"Sensor ID: {self.sensor_id}\n")


class SensorMananger:
    def __init__(self) -> None:
        self.__sensors = []

    @property
    def sensors(self):
        return self.__sensors

    def add_sensor(self, sensor: Sensor) -> None:
        if not isinstance(sensor, Sensor):
            raise TypeError("Invalid sensor type`!")
        self.__sensors.append(sensor)

    def remove_sensor(self, candidate: Sensor) -> None:
        for sensor in self.__sensors:
            if candidate == sensor:
                self.__sensors.pop(self.__sensors.index(sensor))
                break
        else:
            raise LookupError("Cannot find sensor!")

    def read_data(self) -> None:
        for sensor in self.sensors:
            sensor.read_data()


def main() -> None:
    t = TemperatureSensor('s')
    h = HumiditySensor('tt')
    lll = LightSensor('ll')

    t_ws = TemperatureSensorWoutSl('65')
    h_ws = HumiditySensorWoutSl('sss')
    l_ws = LightSensorWoutSl('ggg')

    print("With slots")
    print('TemperatureSensor: ', getsizeof(t))
    print('HumiditySensor: ', getsizeof(h))
    print('LightSensor: ', getsizeof(lll))

    print("Without slots")
    print('TemperatureSensor: ', getsizeof(t_ws))
    print('HumiditySensor: ', getsizeof(h_ws))
    print('LightSensor: ', getsizeof(l_ws))


if __name__ == '__main__':
    main()
